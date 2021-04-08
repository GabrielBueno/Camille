const data = {
    preview: {
        url:  "",
        file: null
    },
    state: {
        initializing: false,
        categorizing: false
    },
    response: {
        error:   "",
        details: "",
        pred:    "",
        probs:   []
    }
};

const apiUrl = "http://localhost:5000";
const url    = src => src ? "url(" + src + ")" : "none";

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
}

const categorize = () => {
    if (!data.preview.file)
        return;

    data.state.categorizing = true;
    
    const xhr      = new XMLHttpRequest();
    const formData = new FormData();
    const url      = `${apiUrl}/r50/p`;

    formData.append("file", data.preview.file);

    xhr.onreadystatechange = _ => {
        if (xhr.readyState === 4) {
            const res = xhr.response;

            data.error   = res.error;
            data.details = res.details;
            data.pred    = res.pred;
            data.probs   = res.probs;

            if (data.error)
                console.error(data.error, data.details);

            data.state.categorizing = false;
            goToBottom();
        }
    };

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