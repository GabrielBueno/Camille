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

    }
};

const url = src => src ? "url(" + src + ")" : "none";

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
    data.state.categorizing = true;
    console.log(data.state.categorizing);

    window.setTimeout(() => data.state.categorizing = false, 2000);
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