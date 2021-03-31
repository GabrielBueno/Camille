import models

import torch
import torchvision
import torchvision.transforms as T

from PIL import Image, ImageFile

from dataset import WikiArtDataCollection
from labels import LabelingKind
import fastai_testing as ftest

ftest.test()

# models.train_resnet18("./models/resnet18/test")
# models.train_mobilenetV3_small("./models/mobilenet_v3_small/test")

# input_size = 224
# means      = [.485, .456, .406]
# stds       = [.229, .224, .225]

# t_transform = T.Compose([
#         T.RandomResizedCrop(input_size),
#         T.RandomHorizontalFlip(),
#         T.ToTensor(),
#         T.Normalize(means, stds)
#     ])

# v_transform = T.Compose([
#     T.Resize(input_size),
#     T.CenterCrop(input_size),
#     T.ToTensor(),
#     T.Normalize(means, stds)
# ])

# datacol = WikiArtDataCollection(
#     labeling_kind         = LabelingKind.SIMPLIFIED,
#     training_transforms   = t_transform,
#     validation_transforms = v_transform,
#     subset_size           = 120,
#     validation_percent    = 20
# )

# datacol.plot()

# mobilenetV3            = torchvision.models.mobilenet_v3_small(pretrained=True)
# mobilenetV3.classifier = torch.nn.Sequential(
#     torch.nn.Linear(576, 1024, bias=True),
#     torch.nn.Hardswish(),
#     torch.nn.Dropout(.2, inplace=True),
#     torch.nn.Linear(1024, datacol.num_of_labels)
# )

# mobilenetV3.load_state_dict(torch.load("./models/mobilenet_v3_small/test/mobilenet_v3_small.pt"))
# mobilenetV3.to("cuda")

# print(mobilenetV3)

# img   = Image.open("D:\\Programacao\\Projetos\\Camille\\dataset\\images\\wikiart\\Fauvism\\adam-baltatu_house-on-siret-valley.jpg")
# t_img = v_transform(img).unsqueeze(0).to("cuda")
# out   = mobilenetV3(t_img)

# print(out)
# print(torch.max(out, 1))