from flask import Flask, render_template, request
import numpy as np
import keras.models
import re 

import sys
import os

app = Flask(__name__)

#Get our initial web app up and running
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/customsearch')
def customSearch():
    return render_template("customsearch.html")

@app.route('/ModelExplained')
def ModelExplained():
    return render_template("modelsexplained.html")

@app.route('/livedata')
def LivedData():
    return render_template("livedata.html")