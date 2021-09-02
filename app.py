from __future__ import division, print_function
import sys
import os
import glob
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

MODEL_PATH ='tumor_detector.h5'

model = load_model(MODEL_PATH)

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    a=np.argmax(model.predict(x), axis=1)
    if a==0:
        preds="Brain Tumor"
    elif a==1:
        preds="Normal"
    return preds

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        preds = model_predict(secure_filename(f.filename), model)
        result=preds
        return result
    return None

if __name__ == '__main__':
    app.run(port=5001,debug=True)