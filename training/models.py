from dataset import WikiArtDataCollection
from labels  import LabelingKind

import torch
import torchvision.models
import torchvision.transforms as T

DEV = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def train_resnet18():
    resnet18   = torchvision.models.resnet18(pretrained=True)
    input_size = 224

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

    (t_set, v_set) = (datacol.training_set, datacol.validation_set)

    print(len(t_set))
    print(len(v_set))