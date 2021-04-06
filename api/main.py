from labels import label_func

import pathlib
import sys
import os

# from flask          import Flask, request, jsonify
# from werkzeug.utils import secure_filename
from bottle        import get, post, run, request, response
from uuid          import uuid4
from fastai.basics import load_learner, parent_label

if (sys.platform == "win32"):
    pathlib.PosixPath = pathlib.WindowsPath

model = load_learner("..\\training\\models\\resnet34.pkl")

def authorized_filetype(ext):
    return ext in ["jpg", "jpeg", "png", "gif"]

def get_ext(filename):
    parts = filename.rsplit(".", 1)

    return parts[1] if parts > 1 else ""


@get("/")
def hello_world():
    return "Hello, world!"

@post("/p")
def predict():
    if ("file" not in request.files):
        response.status = 400
        return { "error": "No file in request" }

    file = request.files.get("file")

    if (file.filename == ""):
        response.status = 400
        return { "error": "No file in request" }

    ext = get_ext(file.filename)

    if (ext == "" or not authorized_filetype(ext)):
        response.status = 400
        return { "error": "Invalid file type" }

    temp_filename = uuid4().hex + "." + ext
    temp_path     = os.path.join("./temp", temp_filename)

    file.save(temp_path)

    prediction = model.predict(file)

    os.remove(temp_path)

    return { "pred": prediction[0] }

run(host="localhost", port="8087")