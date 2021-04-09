import pathlib
import sys
import os
import inspect

from uuid   import uuid4
from enum   import Enum, auto
from bottle import app, get, post, request, response
from PIL    import Image

from labels import label_func
from models import resnet34, resnet50

class HttpStatus():
    Ok          = 200
    BadRequest  = 400
    Forbidden   = 403
    ServerError = 500

class Result(Enum):
    Success          = auto()
    FileNotSent      = auto()
    FileUnauthorized = auto()
    IOErr            = auto()
    PredictionErr    = auto()

def cors():
    response.headers["Access-Control-Allow-Origin"]  = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token"

## ----- Utils

def get_ext(filename):
    parts = filename.rsplit(".", 1)

    return parts[1] if len(parts) > 1 else ""

## ----- IO

def save_tmp_file(file, ext):
    try:
        temp_filename = uuid4().hex + "." + ext
        temp_path     = os.path.join("./temp", temp_filename)

        file.save(temp_path)

        return (True, (file, temp_path))
    except Exception as err:
        return (False, str(err))

def rm_file(path):
    try:
        os.remove(path)

        return (True, None)
    except Exception as err:
        return (False, str(err))

## ----- Prediction

def get_prediction(model, path):
    try:
        (label, _, probabilities) = model.predict(path)
        vocab                     = model.vocab()
        labeled_probabilities     = []

        for i in range(len(probabilities)):
            labeled_probabilities.append({ "label": vocab[i], "prob": probabilities[i].item() })

        sorted_probabilities = sorted(labeled_probabilities, key=lambda p: p["prob"], reverse=True)

        return (True, { "pred": label, "probs": sorted_probabilities })
    except Exception as err:
        return (False, str(err))

def predict_request(model, req):
    (has_file, file) = get_file_from_request(req)

    if (not has_file):
        return (Result.FileNotSent, None)

    ext = get_ext(file.filename)

    if (not authorized_filetype(ext)):
        return (Result.FileUnauthorized, None)

    (file_saved, tmp_file_result) = save_tmp_file(file, ext)

    if (not file_saved):
        return (Result.IOErr, tmp_file_result)

    (_, tmp_path)                  = tmp_file_result
    (successful_pred, pred_result) = get_prediction(model, tmp_path)

    rm_file(tmp_path)

    if (not successful_pred):
        return (Result.PredictionErr, pred_result)

    return (Result.Success, pred_result)

## ----- Request

def authorized_filetype(ext):
    return ext in ["jpg", "jpeg", "png", "gif"]


def get_file_from_request(req):
    if ("file" not in req.files):
        return (False, None)

    file = req.files["file"]

    if (file.filename == ""):
        return (False, None)

    return (True, file)

## ----- Endpoints

def build_prediction_endpoint(model):
    _err = lambda m, d: { "error": m, "details": d }

    def endpoint():
        response.content_type = "application/json"

        (result_type, result) = predict_request(model, request)

        if (result_type == Result.FileNotSent):
            response.status = HttpStatus.BadRequest
            return _err("File not sent in request")

        if (result_type == Result.FileUnauthorized):
            response.status = HttpStatus.Forbidden
            return _err("File type unauthorized")

        if (result_type == Result.IOErr):
            response.status = HttpStatus.ServerError

            print(result)
            return _err("Error on IO operation", result)

        if (result_type == Result.PredictionErr):
            response.status = HttpStatus.ServerError

            print(result)
            return _err("Error while predicting", result)

        response.status = HttpStatus.Ok
        return result

    return endpoint

def hello_world():
    return "OUT!"

def t():
    return { "a": "b" }

api = app()

# api.install(CORSPlugin())

api.add_hook("after_request", cors)

api.route("/",          "GET",  hello_world)
api.route("/p",         "POST", build_prediction_endpoint(resnet50))
api.route("/r50/p",     "POST", build_prediction_endpoint(resnet50))
api.route("/r34/p",     "POST", build_prediction_endpoint(resnet34))
api.route("/r34/vocab", "GET",  lambda: { "vocab": [l for l in resnet34.vocab()] })
api.route("/r50/vocab", "GET",  lambda: { "vocab": [l for l in resnet50.vocab()] })

api.run(port=5000)


