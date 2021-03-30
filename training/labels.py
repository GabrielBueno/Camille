from enum import Enum

UNDEFINED_LABEL = -1

class LabelingKind(Enum):
    SIMPLIFIED = 1
    ATOMIC     = 2

class SimpleLabel:
    EXPRESSIONISM         = 1
    ABSTRACT_ART          = 2
    CUBISM                = 3
    REALISM               = 4
    RENAISSANCE           = 5
    ART_NOUVEAU           = 6
    BAROQUE               = 7
    FAUVISM               = 8
    IMPRESSIONISM         = 9
    POST_IMPRESSIONISM    = 10
    NAIVE_ART_PRIMITIVISM = 11
    PONTILLISM            = 12
    POP_ART               = 13
    ROCOCO                = 14
    ROMANTICISM           = 15
    SYMBOLISM             = 16
    UKIYO_E               = 17

class AtomicLabel:
    ABSTRACT_EXPRESSIONISM     = 1
    ACTION_PAINTING            = 2
    MINIMALISM                 = 3
    COLOR_FIELD_PAINTING       = 4
    EXPRESSIONISM              = 5
    ANALYTICAL_CUBISM          = 6
    CUBISM                     = 7
    SYNTHETIC_CUBISM           = 8
    REALISM                    = 9
    CONTEMPORARY_REALISM       = 10
    NEW_REALISM                = 11
    EARLY_RENAISSANCE          = 12
    HIGH_RENAISSANCE           = 13
    MANNERISM_LATE_RENAISSANCE = 14
    NORTHERN_RENAISSANCE       = 15
    ART_NOUVEAU_MODERN         = 16
    BAROQUE                    = 17
    FAUVISM                    = 18
    IMPRESSIONISM              = 19
    POST_IMPRESSIONISM         = 20
    NAIVE_ART_PRIMITIVISM      = 21
    POINTILLISM                = 22
    POP_ART                    = 23
    ROCOCO                     = 24
    ROMANTICISM                = 25
    SYMBOLISM                  = 26
    UKIYO_E                    = 27

NUM_OF_SIMPLE_LABELS = SimpleLabel.UKIYO_E
NUM_OF_ATOMIC_LABELS = AtomicLabel.UKIYO_E

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

def __val_or_undef(dict, key):
    if (key in dict):
        return dict[key]

    return UNDEFINED_LABEL

def labeling_strategy(labeling_kind):
    if (labeling_kind == LabelingKind.SIMPLIFIED):
        return lambda str: __val_or_undef(SIMPLIFIED_LABEL_DICT, str)

    if (labeling_kind == LabelingKind.ATOMIC):
        return lambda str: __val_or_undef(COMPLETE_LABEL_DICT, str)

    raise Exception(f"Invalid labeling kind: {labeling_kind}")

