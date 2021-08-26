import json
from flask import Flask, request, render_template
import pickle
import numpy as np
from input import input

app = Flask(__name__)
model = pickle.load(open('regressor.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict", methods=["POST"])
def predict():

    try:
        parameters =  input(request.data)
        prediction = model.predict(parameters)
        return json.dumps({"predicted_price": prediction.tolist()})
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except Exception:
        return json.dumps({"error": "PREDICTION FAILED"}), 500

