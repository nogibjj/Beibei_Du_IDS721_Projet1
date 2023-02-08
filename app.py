import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

df = pd.read_csv("data/avg_wage.csv")
X = df.iloc[:, 1:-1].values

app = Flask(__name__)
regressor = pickle.load(open("model.pkl", "rb"))

def guess_2022(test_data=X[0]):
    prediction = regressor.predict(test_data)
    print("It is working!")
    return prediction


@app.route('/')
def first_line():
    print("This is the first line of the app.py file for 2022")
    return 'This is an app to predict the average wage of a country.'

def predict():
    data = request.get_json()
    country_data = data['Country']
    country_data = pd.DataFrame([country_data], columns=['Country', '2000', '2005', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])
    X = country_data.iloc[:, 1:].values
    with open('model.pkl', 'rb') as f:
        regressor = pickle.load(f)
    y_pred = regressor.predict(X)
    return jsonify({'prediction': str(y_pred[0])})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)