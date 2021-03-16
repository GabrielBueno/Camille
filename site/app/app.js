const data = {
    previewUrl:  "",
    previewFile: null
};

const url = src => src ? "url(" + src + ")" : "none";

const selectImg = () => {
    const fileSelector = document.getElementById("img-file-selector");

    fileSelector.onchange = () => { 
        if (data.previewUrl) {
            URL.revokeObjectURL(data.previewUrl);

            data.previewUrl  = "";
            data.previewFile = null;
        }

        data.previewFile = fileSelector.files[0];
        data.previewUrl  = URL.createObjectURL(data.previewFile);
    };

    fileSelector.click();
}

const categorize = () => {
    console.log(data.previewFile);
};

const vue = new Vue({ 
    el:   "#main", 
    data: data,
    methods: {
        url,
        selectImg,
        categorize
    }
});