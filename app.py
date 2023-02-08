import numpy as np
from flask import Flask, request, render_template
import pickle
from model import avg_wage_pred_2022


app = Flask(__name__)
Model = pickle.load(open("model.pkl", "rb"))


def avg_wage_pred_2022(features, regressor):
    prediction = regressor.predict(features)
    return prediction 


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)