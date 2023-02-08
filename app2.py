import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

df = pd.read_csv("data/avg_wage.csv")
df['Country'] = df['Country'].astype(str)
df['Country'] = df['Country'].apply(lambda x: x.replace('\u202f', ''))
df.sort_values(by=['2020'], inplace=True, ascending=False)


app = Flask(__name__)
regressor = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def first_line():
    return 'This is an app to predict the average wage of a country.'

@app.route("/guess/<country>")
def guess_country(country):
    """
    guess the country with highest average wage in 2020
    """
    # check if the country is in the dataset
    print("Guess the country with the highest avergae income in 2020")
    if country in df['Country'].values:
        # check if the country is in the top 1
        if df.head(1)['Country'].values[0] == country:
            return "You are correct!"
        else:
            return "You are wrong"
    else:
        return "The country is not in the dataset"

@app.route("/predict/<country>")
def predict(country):
    """
    predict the average wage of a country in 2020
    """
    with open('model.pkl', 'rb') as f:
        regressor = pickle.load(f)
    if country in df['Country'].values:
        country_data = df[df['Country'] == country]
        x_pred = country_data.iloc[:, 1:-1].values
        y_pred = regressor.predict(x_pred)
        return str(y_pred[0]) + " in 2020"
    else:
        return "The country is not in the dataset"

@app.route("/")
def index2():
    return render_template("index2.html")

if __name__ == "__main__":
    app.run(debug=True)