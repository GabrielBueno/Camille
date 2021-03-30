from dataset import WikiArtDataCollection
from labels  import LabelingKind

import time
import copy
import gc

import torch
import torch.nn as nn
import torchvision.models
import torchvision.transforms as T

from torch.cuda.amp import GradScaler, autocast

DEVICE = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
# DEVICE = "cpu"

def train_mobilenetV3_small():
    torch.cuda.empty_cache()

    input_size    = 224
    num_of_epochs = 15
    batch_size    = 32

    means = [.485, .456, .406]
    stds  = [.229, .224, .225]

    t_transform = T.Compose([
        T.RandomResizedCrop(input_size),
        T.RandomHorizontalFlip(),
        T.ToTensor(),
        T.Normalize(means, stds)
    ])

    v_transform = T.Compose([
        T.Resize(input_size),
        T.CenterCrop(input_size),
        T.ToTensor(),
        T.Normalize(means, stds)
    ])

    datacol = WikiArtDataCollection(
        labeling_kind         = LabelingKind.SIMPLIFIED,
        training_transforms   = t_transform,
        validation_transforms = v_transform,
        validation_percent    = 20
    )

    mobilenetV3            = torchvision.models.mobilenet_v3_small(pretrained=True).to(DEVICE)
    mobilenetV3.classifier = nn.Sequential(
        nn.Linear(576, 1024, bias=True),
        nn.Hardswish(),
        nn.Dropout(.2, inplace=True),
        nn.Linear(1024, datacol.num_of_labels)
    )

    optimizer = torch.optim.SGD(mobilenetV3.parameters(), lr=.001, momentum=.9)
    criterion = torch.nn.CrossEntropyLoss()

    best_model = _train_and_eval(mobilenetV3, datacol, criterion, optimizer, epochs=num_of_epochs, batch_size=batch_size)

def train_resnet18():
    torch.backends.cudnn.enabled = False
    torch.cuda.empty_cache()

    print(DEVICE)

    input_size    = 224
    num_of_epochs = 15
    batch_size    = 1

    means = [.485, .456, .406]
    stds  = [.229, .224, .225]

    t_transform = T.Compose([
        T.RandomResizedCrop(input_size),
        T.RandomHorizontalFlip(),
        T.ToTensor(),
        T.Normalize(means, stds)
    ])

    v_transform = T.Compose([
        T.Resize(input_size),
        T.CenterCrop(input_size),
        T.ToTensor(),
        T.Normalize(means, stds)
    ])

    datacol = WikiArtDataCollection(
        labeling_kind         = LabelingKind.SIMPLIFIED,
        training_transforms   = t_transform,
        validation_transforms = v_transform,
        validation_percent    = 20
    )

    resnet18    = torchvision.models.resnet18(pretrained=True)
    resnet18.fc = torch.nn.Linear(512, datacol.num_of_labels)
    
    optimizer = torch.optim.SGD(resnet18.parameters(), lr=.001, momentum=.9)
    criterion = torch.nn.CrossEntropyLoss()

    best_model = _train_and_eval(resnet18, datacol, criterion, optimizer, epochs=num_of_epochs, batch_size=batch_size)

def _train_and_eval(model, datacol, criterion, optimizer, epochs=15, batch_size=8):
    start = time.time()

    accuracy_history = []
    # best_model       = _cp_model(model)
    best_accuracy    = 0.0

    t_dataloader = torch.utils.data.DataLoader(datacol.training_set,   batch_size=batch_size, shuffle=True, num_workers=0)
    v_dataloader = torch.utils.data.DataLoader(datacol.validation_set, batch_size=batch_size, shuffle=True, num_workers=0)

    running_loss     = 0.0
    running_corrects = 0.0

    for epoch in range(epochs):
        print(f"epoch {epoch + 1}/{epochs}")

        (t_loss, t_corrects) = _train(model, t_dataloader, criterion, optimizer)
        (v_loss, v_corrects) = _eval(model,  v_dataloader, criterion)

        epoch_t_loss = t_loss              / len(datacol.training_set)
        epoch_t_acc  = t_corrects.double() / len(datacol.training_set)
        
        epoch_v_loss = v_loss              / len(datacol.validation_set)
        epoch_v_acc  = v_corrects.double() / len(datacol.validation_set)

        print("training (loss {:.4f}) (acc {:.4f})".format(epoch_t_loss, epoch_t_acc))
        print("eval (loss {:.4f}) (acc {:.4f})".format(epoch_v_loss, epoch_v_acc))

        if (epoch_v_acc > best_accuracy):
            best_accuracy = epoch_v_acc
            # best_model    = _cp_model(model)

        accuracy_history.append(epoch_v_acc)

    print(f"\nfinished in {time.time() - start}s")
    print("best acc {:.4f}".format(best_accuracy))

    return best_model

def _train(model, dataloader, criterion, optimizer):
    model.train()
    model.to(DEVICE)

    running_loss     = 0.0
    running_corrects = 0.0

    accumulation_steps = 16
    curr_batch         = 1

    model.zero_grad()
    optimizer.zero_grad()

    for (inputs, labels) in dataloader:
        dev_inputs = inputs.to(DEVICE)
        # dev_labels = labels.to(DEVICE)
        
        outputs = model(dev_inputs)

        dev_labels = labels.to(DEVICE)
        loss    = criterion(outputs, dev_labels)

        # (_, preds) = torch.max(outputs, 1)

        (loss / accumulation_steps).backward()
        # optimizer.step()

        if (curr_batch % accumulation_steps == 0):
            optimizer.step()

            model.zero_grad()
            optimizer.zero_grad()

        del dev_inputs
        del dev_labels

        # running_loss     += loss.detach().item() * inputs.size(0)
        # running_corrects += torch.sum(preds == labels.data)

        print(curr_batch)
        curr_batch += 1

    return (running_loss, running_corrects)

def _eval(model, dataloader, criterion):
    model.eval()

    running_loss     = 0.0
    running_corrects = 0.0

    for (inputs, labels) in dataloader:
        dev_inputs = inputs.to(DEVICE)
        dev_labels = labels.to(DEVICE)

        with torch.set_grad_enabled(False):
            outputs = model(inputs)
            loss    = criterion(outputs, labels)

            (_, preds) = torch.max(outputs, 1)

            running_loss     += loss.item() * dev_inputs.size(0)
            running_corrects += torch.sum(preds == dev_labels.data)

    return (running_loss, running_corrects)

def _cp_model(model):
    # if (torch.cuda.is_available()):
    #     model.to("cpu")
    #     copied = copy.deepcopy(model.state_dict())

    #     torch.cuda.empty_cache()
    #     model.to(DEVICE)

    #     return copied

    return copy.deepcopy(model.state_dict())
