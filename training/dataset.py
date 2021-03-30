from labels import labeling_strategy

import os
import random

from PIL import Image
from torch.utils.data import Dataset

class WikiArtDataCollection():
    ROOT = "D:\Programacao\Projetos\Camille\dataset\images\wikiart"

    def __init__(self, labeling_kind, training_transforms, validation_transforms, validation_percent):
        self.validation_percent = validation_percent
        
        # Init datasets
        label = labeling_strategy(labeling_kind)
        dirs  = [path for path in os.scandir(self.ROOT) if path.is_dir()]
        imgs  = [(file.path, label(dir.name)) for dir in dirs for file in os.scandir(dir.path)]

        validation_size = round(len(imgs) * self.validation_percent / 100)

        random.shuffle(imgs)

        self.training_set   = CamilleDataset(imgs[:-validation_size], training_transforms)
        self.validation_set = CamilleDataset(imgs[-validation_size:], validation_transforms)
        
class CamilleDataset(Dataset):
    def __init__(self, imgs, transform):
        self.transform = transform
        self.imgs      = imgs

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, index):
        (path, label) = self.imgs[index]
        img           = Image.open(path)

        return (self.transform(img), label)