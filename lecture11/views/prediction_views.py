from controller.controller_prediction import PredictionController
from flask import Flask, template_rendered
import pandas as pd 

def prediction(request) :
    if request.method == "POST":
        controller = PredictionController(request)
        if controller.validate_data():
            response = controller.response
     
            return template_rendered("predict.html",context={response})
def login(self,request,name,email,password):
    controller = PredictionController(request)

    response = controller.login(name,email,password)
    return template_rendered("predict.html",context={response})

def sign_up(self,request,name,email,password):
    controller = PredictionController(request)
    response = controller.sign_up(name,email,password,request)
    return template_rendered("predict.html",context={response})



