#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:21:01 2020

@author: rashi
"""

import json
from flask import Flask,request,jsonify,Response, render_template, url_for
import base64
import numpy as np
import imageio
from matplotlib.pyplot import imshow
from keras.preprocessing import image
from types import SimpleNamespace 
import pandas as pd
import joblib
import requests

from flask import Flask
app = Flask(__name__)


@app.route('/Seeds', methods = ["POST"])
def products():
    #data = request.get_json(force = "true")
    with open("Seed.json") as f:
        file = json.load(f)
    
    
    return (file)

if __name__ == "__main__":
    app.run()
    
