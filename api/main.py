import pathlib
import sys
import os

from uuid   import uuid4
from enum   import Enum, auto
from bottle import get, post, run, request, response

from labels import label_func
from models import resnet34, resnet50

class HttpStatus(Enum):
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

## ----- Utils

def get_ext(filename):
    parts = filename.rsplit(".", 1)

    return parts[1] if parts > 1 else ""

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

def try_to_predict(model, path):
    try:
        prediction = model.predict(path)

        return (True, prediction)
    except Exception as err:
        return (False, str(err))

def run_prediction(model, request):
    (has_file, file) = get_file_from_request(request)

    if (not has_file):
        return (Result.FileNotSent, None)

    ext = get_ext(file.filename)

    if (not authorized_filetype(ext)):
        return (Result.FileUnauthorized, None)

    (file_saved, tmp_file_result) = save_tmp_file()

    if (not file_saved):
        return (Result.IOErr, tmp_file_result)

    (_, tmp_path)                  = tmp_file_result
    (successful_pred, pred_result) = try_to_predict(tmp_path)

    if (not successful_pred):
        return (Result.PredictionErr, pred_result)

    (file_removed, rm_result) = rm_file(tmp_path)

    if (not file_removed):
        return (IOErr, rm_result)

    return (Success, pred_result)

## ----- Request

def authorized_filetype(ext):
    return ext in ["jpg", "jpeg", "png", "gif"]


def get_file_from_request(request):
    if ("file" not in request.files):
        return (False, None)

    file = request.files["file"]

    if (file.filename == ""):
        return (False, None)

    return (True, file)

## ----- Responses

def err(msg, details = ""):
    return { "error": msg, "details": details }

def ok(prediction):
    return { "prediction": prediction[0] }

## ----- Endpoints

def prediction_request(model, req, res):
    (result_type, result) = run_prediction(model, req)

    if (result_type == Result.FileNotSent):
        res.status = HttpStatus.BadRequest
        return err("File not sent in request")

    if (result_type == Result.FileUnauthorized):
        res.status = HttpStatus.Forbidden
        return err("File type unauthorized")

    if (result.type == Result.IOErr):
        res.status = HttpStatus.ServerError
        return err("Error on IO operation", result)

    if (result.type == Result.PredictionErr):
        res.status = HttpStatus.ServerError
        return err("Error while predicting", result)

    print(result)
    response.status = HttpStatus.Ok
    return ok(result)

@get("/")
def hello_world():
    return "OUT!"

@post("/p")
def default_prediction():
    return prediction_request(resnet50, request, response)

@post("/r34/p")
def predict_r34():
    return prediction_request(resnet34, request, response)
    
@post("/r50/p")
def predict_r50():
    return prediction_request(resnet50, request, response)

run(host="localhost", port="8087")