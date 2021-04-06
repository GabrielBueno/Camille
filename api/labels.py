UNDEFINED_LABEL = "undef_lbl"

class SimpleLabel:
    EXPRESSIONISM         = "Expressionismo"
    ABSTRACT_ART          = "Arte abstrata"
    CUBISM                = "Cubismo"
    REALISM               = "Realismo"
    RENAISSANCE           = "Renascentismo"
    ART_NOUVEAU           = "Art Nouveau"
    BAROQUE               = "Barroco"
    FAUVISM               = "Fauvismo"
    IMPRESSIONISM         = "Impressionismo"
    POST_IMPRESSIONISM    = "Pos Impressionismo"
    NAIVE_ART_PRIMITIVISM = "Arte Naif"
    PONTILLISM            = "Pontilhismo"
    POP_ART               = "Pop-Art"
    ROCOCO                = "Rococo"
    ROMANTICISM           = "Romantismo"
    SYMBOLISM             = "Simbolismo"
    UKIYO_E               = "Ukiyo-e"
    
class AtomicLabel:
    ABSTRACT_EXPRESSIONISM     = "Expressionismo abstrato"
    ACTION_PAINTING            = "Gestualismo"
    MINIMALISM                 = "Minimalismo"
    COLOR_FIELD_PAINTING       = "Color Field"
    EXPRESSIONISM              = "Expressionismo"
    ANALYTICAL_CUBISM          = "Cubismo analitico"
    CUBISM                     = "Cubismo"
    SYNTHETIC_CUBISM           = "Cubismo sintetico"
    REALISM                    = "Realismo"
    CONTEMPORARY_REALISM       = "Realismo contemporaneo"
    NEW_REALISM                = "Novo realismo"
    EARLY_RENAISSANCE          = "Pré-Renascença"
    HIGH_RENAISSANCE           = "Alta Renascença"
    MANNERISM_LATE_RENAISSANCE = "Maneirismo"
    NORTHERN_RENAISSANCE       = "Renascimento nórdico"
    ART_NOUVEAU_MODERN         = "Art Nouveau"
    BAROQUE                    = "Barroco"
    FAUVISM                    = "Fauvismo"
    IMPRESSIONISM              = "Impressionismo"
    POST_IMPRESSIONISM         = "Pos-Impressionismo"
    NAIVE_ART_PRIMITIVISM      = "Arte Naif"
    POINTILLISM                = "Pontilhismo"
    POP_ART                    = "Pop-Art"
    ROCOCO                     = "Rococo"
    ROMANTICISM                = "Romantismo"
    SYMBOLISM                  = "Simbolismo"
    UKIYO_E                    = "Ukiyo-e"
    
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

def label_simple(parent_dir):
    return _val_or_undef(SIMPLIFIED_LABEL_DICT, parent_dir)

def label_atomic(parent_dir):
    _val_or_undef(COMPLETE_LABEL_DICT, parent_dir)

def label_func(fname):
    return label_simple(parent_label(fname))