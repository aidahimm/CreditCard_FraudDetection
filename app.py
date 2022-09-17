import numpy as np
import pickle
from flask import Flask, render_template, request
import smtplib
import os

app = Flask(__name__)
model = pickle.load(open('credit_card_fraud_v2.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predicting the results on the frontend
    '''
    int_features = [float(x) for x in request.form.values()]
    # print(int_features)
    final_features = [np.array(int_features)]
    print(final_features)
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    #Define Server Params
    server_connect = smtplib.SMTP("smtp.gmail.com", 587)
    server_connect.starttls()
    server_connect.login("sender_mail", "sender_password")

    if output == 1:
        return render_template('home.html', prediction = 'Fraud Transaction Detected')
        message = "This is a Fraud transaction"
        server_connect.sendmail("sender_mail@gmail.com", "receiver_mail@gmail.com", message)
        server_connect.quit()
    
    elif output == 0:
        return render_template('home.html', prediction = 'Valid Transaction Approved')
        message = "This is a Non-Fraud transaction"
        server_connect.sendmail("sender_mail@gmail.com", "receiver_mail@gmail.com", message)
        server_connect.quit()