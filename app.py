import pickle
from flask import Flask, request, app, jsonify, url_for, render_template

import numpy as np
import pandas as pd


app Flask(__name__)

#loading model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', method = ['POST'])

def predict_api():
    data = request.json['data']
    print(data)
    new_data = np.array(list(data.values())).reshape(1,-1)
    print(new_data)
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])


if __name__=="__main__":
    app.run(debug=run)
