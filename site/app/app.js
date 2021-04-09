const data = {
    preview: {
        url:  "",
        file: null
    },
    state: {
        initializing: false,
        categorizing: false,
    },
    model: {
        id:   "r50",
        vocab: []
    },
    ui: {
        modelName: "ResNet50",
        vocab:     ""
    },
    response: {
        error:   "",
        details: "",
        pred:    "",
        probs:   []
    }
};

const apiUrl = "http://localhost:5000";

const url = (src) => src ? "url(" + src + ")" : "none";

const selectImg = () => {
    const fileSelector = document.getElementById("img-file-selector");

    fileSelector.onchange = () => { 
        if (data.preview.url) {
            URL.revokeObjectURL(data.preview.url);

            data.preview.url  = "";
            data.preview.file = null;
        }

        data.preview.file = fileSelector.files[0];
        data.preview.url  = URL.createObjectURL(data.preview.file);
    };

    fileSelector.click();
};

const getModelMetadata = () => {
    data.state.initializing = true;

    const xhr = new XMLHttpRequest();

    xhr.onreadystatechange = _ => {
        if (xhr.readyState !== 4)
            return;
        
        if (xhr.status === 200) {
            data.model.vocab = JSON.parse(xhr.response).vocab;
            
            const init = data.model.vocab.slice(0, -1)
            const last = data.model.vocab[data.model.vocab.length - 1];

            data.ui.vocab = (init.join(", ") + " e " + last).toLowerCase();

        } else {
            goToError();
        }
    };

    const url = `${apiUrl}/${data.model.id}/vocab`;

    xhr.open("get", url, true);
    xhr.send();
};

const categorize = () => {
    if (!data.preview.file)
        return;

    data.state.categorizing = true;
    
    const xhr      = new XMLHttpRequest();
    const formData = new FormData();

    formData.append("file", data.preview.file);

    xhr.onreadystatechange = _ => {
        if (xhr.readyState === 4) {
            if (xhr.status !== 200) {
                console.error(xhr.response);
                goToError();

                return;
            }

            const res = JSON.parse(xhr.response);

            data.response.error   = res.error;
            data.response.details = res.details;
            data.response.pred    = res.pred;
            data.response.probs   = res.probs;

            if (res.error) 
                console.error(res.error, res.details);

            data.state.categorizing = false;
            goToBottom();
        }
    };

    const url = `${apiUrl}/${data.model.id}/p`;

    xhr.open("post", url, true);
    xhr.send(formData);
};

const smoothScroll = (id) => {
    document
        .getElementById(id)
        .scrollIntoView({ behavior: "smooth" });
};

const goToTop    = () => smoothScroll("top-view");
const goToBottom = () => smoothScroll("bottom-view");
const goToError  = () => window.location.replace("error.html");

getModelMetadata();

const vue = new Vue({ 
    el:   "#main", 
    data: data,
    methods: {
        url,
        selectImg,
        categorize,
        goToTop,
        goToBottom
    }
});