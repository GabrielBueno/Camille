from fastai.basics import *
from fastai.vision.all import *

from labels import LabelingKind, labeling_strategy

import matplotlib.pyplot as plt

# dirs  = [path for path in os.scandir(self.ROOT) if path.is_dir()]
# imgs  = [(file.path, label(dir.name)) for dir in dirs for file in os.scandir(dir.path)]

flabel = labeling_strategy(LabelingKind.SIMPLIFIED)

def test():
    path   = "D:\Programacao\Projetos\Camille\dataset\images\wikiart"
    dblock = DataBlock(
        blocks     = (ImageBlock, CategoryBlock),
        get_items  = get_image_files,
        get_y      = flabel,
        splitter   = RandomSubsetSplitter(.3, .1),
        item_tfms  = RandomResizedCrop(128, min_scale=.35),
        batch_tfms = Normalize.from_stats(*imagenet_stats)
    )

    dloader = dblock.dataloaders(path, bs=32, shuffle=True)

    print(dloader.show_batch(show=False))
    plt.show()