from labels import labeling_strategy, num_of_labels_of_kind

import os
import random

import matplotlib.pyplot as plt
from PIL              import Image, ImageFile
from torch.utils.data import Dataset

class WikiArtDataCollection():
    ROOT = "D:\Programacao\Projetos\Camille\dataset\images\wikiart"

    def __init__(self, labeling_kind, subset_size, training_transforms, validation_transforms, validation_percent):
        self.validation_percent = validation_percent
        self.num_of_labels      = num_of_labels_of_kind(labeling_kind)
        
        # Init datasets
        label = labeling_strategy(labeling_kind)
        dirs  = [path for path in os.scandir(self.ROOT) if path.is_dir()]
        imgs  = [(file.path, label(dir.name)) for dir in dirs for file in os.scandir(dir.path)]

        imgs_by_label = {}

        for (path, label) in imgs:
            if (label not in imgs_by_label):
                imgs_by_label[label] = []

            imgs_by_label[label].append((path, label))

        subsets = []

        for label in imgs_by_label:
            imgs = imgs_by_label[label]

            random.shuffle(imgs)
            subsets.append(imgs[:subset_size])

        subset          = [img for sub in subsets for img in sub]
        validation_size = round(len(subset) * self.validation_percent / 100)

        random.shuffle(subset)

        self.training_set   = CamilleDataset(subset[:-validation_size], training_transforms)
        self.validation_set = CamilleDataset(subset[-validation_size:], validation_transforms)

    def plot(self):
        plt.hist([l for (p, l) in self.training_set.imgs],   bins=17)
        plt.hist([l for (p, l) in self.validation_set.imgs], bins=17)

        plt.show()
        
class CamilleDataset(Dataset):
    def __init__(self, imgs, transform):
        self.transform = transform
        self.imgs      = imgs

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, index):
        (path, label) = self.imgs[index]

        ImageFile.LOAD_TRUNCATED_IMAGES = True

        return (self.transform(Image.open(path)), label)

    def plot(self):
        # print(self.imgs)
        plt.hist([l for (p, l) in self.imgs], bins=17)
        plt.show()