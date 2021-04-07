from labels import label_simple

import os
import sys
import pathlib

from fastai.basics import load_learner

_posix_path = pathlib.PosixPath
_win32_path = pathlib.WindowsPath

if (sys.platform == "win32"):
    pathlib.PosixPath = _win32_path

class Model():
    def __init__(self, name, path):
        self.name  = name
        self.path  = path
        self.model = load_learner(path)

resnet34 = Model("ResNet34", "../models/exports/resnet34.pkl")
resnet50 = Model("ResNet50", "../models/exports/resnet50.pkl")

pathlib.PosixPath = _posix_path