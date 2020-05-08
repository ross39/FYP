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

@app.route('/index.html')
def returnIndex():
    return render_template("index.html")

@app.route('/charts.html')
def returnCharts():
    return render_template("charts.html")

@app.route('/BigIdeas.html')
def returnBigIdeas():
    return render_template("BigIdeas.html")

@app.route('/combat.html')
def returnCombat():
    return render_template("combat.html")

@app.route('/ModelData.html')
def returnmodelData():
    return render_template("ModelData.html")
    