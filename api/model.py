from labels        import label_simple
from fastai.basics import load_learner, parent_label

def label_func(fname):
    return label_simple(parent_label(fname))

model = load_learner("..\\training\\models\\resnet34.pkl")