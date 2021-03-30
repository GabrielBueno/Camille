NUM_OF_LABELS = 19

class Label:
    EXPRESSIONISM         = 1
    ABSTRACT_ART          = 2
    CUBISM                = 3
    REALISM               = 4
    RENAISSANCE           = 5
    ART_NOUVEAU           = 6
    BAROQUE               = 7
    # COLOR_FIELD           = 8
    FAUVISM               = 9
    IMPRESSIONISM         = 10
    POST_IMPRESSIONISM    = 11
    # MINIMALISM            = 12
    NAIVE_ART_PRIMITIVISM = 13
    PONTILLISM            = 14
    POP_ART               = 15
    ROCOCO                = 16
    ROMANTICISM           = 17
    SYMBOLISM             = 18
    UKIYO_E               = 19
    UNDEFINED             = -1

DIR_LABELS = {
    "Abstract_Expressionism":     Label.ABSTRACT_ART,
    "Action_painting":            Label.ABSTRACT_ART,
    "Minimalism":                 Label.ABSTRACT_ART,
    "Color_Field_Painting":       Label.ABSTRACT_ART,
    "Expressionism":              Label.EXPRESSIONISM,
    "Analytical_Cubism":          Label.CUBISM,
    "Cubism":                     Label.CUBISM,
    "Synthetic_Cubism":           Label.CUBISM,
    "Realism":                    Label.REALISM,
    "Contemporary_Realism":       Label.REALISM,
    "New_Realism":                Label.REALISM,
    "Early_Renaissance":          Label.RENAISSANCE,
    "High_Renaissance":           Label.RENAISSANCE,
    "Mannerism_Late_Renaissance": Label.RENAISSANCE,
    "Northern_Renaissance":       Label.RENAISSANCE,
    "Art_Nouveau_Modern":         Label.ART_NOUVEAU,
    "Baroque":                    Label.BAROQUE,
    "Fauvism":                    Label.FAUVISM,
    "Impressionism":              Label.IMPRESSIONISM,
    "Post_Impressionism":         Label.POST_IMPRESSIONISM,
    "Naive_Art_Primitivism":      Label.NAIVE_ART_PRIMITIVISM,
    "Pointillism":                Label.PONTILLISM,
    "Pop_Art":                    Label.POP_ART,
    "Rococo":                     Label.ROCOCO,
    "Romanticism":                Label.ROMANTICISM,
    "Symbolism":                  Label.SYMBOLISM,
    "Ukiyo_e":                    Label.UKIYO_E,
}

def get_dir_label(dirname):
    if (dirname in DIR_LABELS):
        return DIR_LABELS[dirname]

    return Label.UNDEFINED

