from enum import Enum

UNDEFINED_LABEL = -1

class LabelingKind(Enum):
    SIMPLIFIED = 1
    ATOMIC     = 2

class SimpleLabel:
    EXPRESSIONISM         = 0
    ABSTRACT_ART          = 1
    CUBISM                = 2
    REALISM               = 3
    RENAISSANCE           = 4
    ART_NOUVEAU           = 5
    BAROQUE               = 6
    FAUVISM               = 7
    IMPRESSIONISM         = 8
    POST_IMPRESSIONISM    = 9
    NAIVE_ART_PRIMITIVISM = 10
    PONTILLISM            = 11
    POP_ART               = 12
    ROCOCO                = 13
    ROMANTICISM           = 14
    SYMBOLISM             = 15
    UKIYO_E               = 16

class AtomicLabel:
    ABSTRACT_EXPRESSIONISM     = 0
    ACTION_PAINTING            = 1
    MINIMALISM                 = 2
    COLOR_FIELD_PAINTING       = 3
    EXPRESSIONISM              = 4
    ANALYTICAL_CUBISM          = 5
    CUBISM                     = 6
    SYNTHETIC_CUBISM           = 7
    REALISM                    = 8
    CONTEMPORARY_REALISM       = 9
    NEW_REALISM                = 10
    EARLY_RENAISSANCE          = 11
    HIGH_RENAISSANCE           = 12
    MANNERISM_LATE_RENAISSANCE = 13
    NORTHERN_RENAISSANCE       = 14
    ART_NOUVEAU_MODERN         = 15
    BAROQUE                    = 16
    FAUVISM                    = 17
    IMPRESSIONISM              = 18
    POST_IMPRESSIONISM         = 19
    NAIVE_ART_PRIMITIVISM      = 20
    POINTILLISM                = 21
    POP_ART                    = 22
    ROCOCO                     = 23
    ROMANTICISM                = 24
    SYMBOLISM                  = 25
    UKIYO_E                    = 26

NUM_OF_SIMPLE_LABELS = SimpleLabel.UKIYO_E + 1
NUM_OF_ATOMIC_LABELS = AtomicLabel.UKIYO_E + 1

SIMPLIFIED_LABEL_DICT = {
    "Abstract_Expressionism":     SimpleLabel.ABSTRACT_ART,
    "Action_painting":            SimpleLabel.ABSTRACT_ART,
    "Minimalism":                 SimpleLabel.ABSTRACT_ART,
    "Color_Field_Painting":       SimpleLabel.ABSTRACT_ART,
    "Expressionism":              SimpleLabel.EXPRESSIONISM,
    "Analytical_Cubism":          SimpleLabel.CUBISM,
    "Cubism":                     SimpleLabel.CUBISM,
    "Synthetic_Cubism":           SimpleLabel.CUBISM,
    "Realism":                    SimpleLabel.REALISM,
    "Contemporary_Realism":       SimpleLabel.REALISM,
    "New_Realism":                SimpleLabel.REALISM,
    "Early_Renaissance":          SimpleLabel.RENAISSANCE,
    "High_Renaissance":           SimpleLabel.RENAISSANCE,
    "Mannerism_Late_Renaissance": SimpleLabel.RENAISSANCE,
    "Northern_Renaissance":       SimpleLabel.RENAISSANCE,
    "Art_Nouveau_Modern":         SimpleLabel.ART_NOUVEAU,
    "Baroque":                    SimpleLabel.BAROQUE,
    "Fauvism":                    SimpleLabel.FAUVISM,
    "Impressionism":              SimpleLabel.IMPRESSIONISM,
    "Post_Impressionism":         SimpleLabel.POST_IMPRESSIONISM,
    "Naive_Art_Primitivism":      SimpleLabel.NAIVE_ART_PRIMITIVISM,
    "Pointillism":                SimpleLabel.PONTILLISM,
    "Pop_Art":                    SimpleLabel.POP_ART,
    "Rococo":                     SimpleLabel.ROCOCO,
    "Romanticism":                SimpleLabel.ROMANTICISM,
    "Symbolism":                  SimpleLabel.SYMBOLISM,
    "Ukiyo_e":                    SimpleLabel.UKIYO_E,
}

COMPLETE_LABEL_DICT = {
    "Abstract_Expressionism":     AtomicLabel.ABSTRACT_EXPRESSIONISM,
    "Action_painting":            AtomicLabel.ACTION_PAINTING,
    "Minimalism":                 AtomicLabel.MINIMALISM,
    "Color_Field_Painting":       AtomicLabel.COLOR_FIELD_PAINTING,
    "Expressionism":              AtomicLabel.EXPRESSIONISM,
    "Analytical_Cubism":          AtomicLabel.ANALYTICAL_CUBISM,
    "Cubism":                     AtomicLabel.CUBISM,
    "Synthetic_Cubism":           AtomicLabel.SYNTHETIC_CUBISM,
    "Realism":                    AtomicLabel.REALISM,
    "Contemporary_Realism":       AtomicLabel.CONTEMPORARY_REALISM,
    "New_Realism":                AtomicLabel.NEW_REALISM,
    "Early_Renaissance":          AtomicLabel.EARLY_RENAISSANCE,
    "High_Renaissance":           AtomicLabel.HIGH_RENAISSANCE,
    "Mannerism_Late_Renaissance": AtomicLabel.MANNERISM_LATE_RENAISSANCE,
    "Northern_Renaissance":       AtomicLabel.NORTHERN_RENAISSANCE,
    "Art_Nouveau_Modern":         AtomicLabel.ART_NOUVEAU_MODERN,
    "Baroque":                    AtomicLabel.BAROQUE,
    "Fauvism":                    AtomicLabel.FAUVISM,
    "Impressionism":              AtomicLabel.IMPRESSIONISM,
    "Post_Impressionism":         AtomicLabel.POST_IMPRESSIONISM,
    "Naive_Art_Primitivism":      AtomicLabel.NAIVE_ART_PRIMITIVISM,
    "Pointillism":                AtomicLabel.POINTILLISM,
    "Pop_Art":                    AtomicLabel.POP_ART,
    "Rococo":                     AtomicLabel.ROCOCO,
    "Romanticism":                AtomicLabel.ROMANTICISM,
    "Symbolism":                  AtomicLabel.SYMBOLISM,
    "Ukiyo_e":                    AtomicLabel.UKIYO_E,
}

def _val_or_undef(dict, key):
    if (key in dict):
        return dict[key]

    return UNDEFINED_LABEL

def labeling_strategy(labeling_kind):
    if (labeling_kind == LabelingKind.SIMPLIFIED):
        return lambda str: _val_or_undef(SIMPLIFIED_LABEL_DICT, str)

    if (labeling_kind == LabelingKind.ATOMIC):
        return lambda str: _val_or_undef(COMPLETE_LABEL_DICT, str)

    raise Exception(f"Invalid labeling kind: {labeling_kind}")

def num_of_labels_of_kind(labeling_kind):
    if (labeling_kind == LabelingKind.SIMPLIFIED):
        return NUM_OF_SIMPLE_LABELS

    if (labeling_kind == LabelingKind.ATOMIC):
        return NUM_OF_ATOMIC_LABELS

    raise Exception(f"Invalid labeling kind: {labeling_kind}")

