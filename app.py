import numpy as np
import pickle
from flask import Flask, render_template, request
import smtplib
import os
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('ModelTesting/card_fraud_rf.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():

    data = pd.read_csv('ModelTesting/demo_transactions.csv')
    list = np.array(data)

    predictions = model.predict(list)

    print(predictions)

    forward_message= ('predictions are as follow:')
    return predictions.tolist()
