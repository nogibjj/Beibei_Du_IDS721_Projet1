import numpy as np
from flask import Flask, render_template
import pickle

def guess
app = Flask(__name__)
Model = pickle.load(open("model.pkl", "rb"))


@app.route('/')
def first_line():
    print("This is the first line of the app.py file")
    return 'This is an app to predict the average wage of a country.'

@app.route('/')
def avg_wage_pred(wages, regressor):
    prediction = regressor.predict(wages)
    return prediction

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)