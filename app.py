import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

df = pd.read_csv("data/avg_wage.csv")
X = df.iloc[:, 1:-1].values
df['Country'] = df['Country'].astype(str)
df['Country'] = df['Country'].apply(lambda x: x.replace('\u202f', ''))
# sort values with 2020 data
df.sort_values(by=['2020'], inplace=True, ascending=False)

app = Flask(__name__)
regressor = pickle.load(open("model.pkl", "rb"))

def guess_2022(test_data=X[0]):
    prediction = regressor.predict(test_data)
    print("It is working!")
    return prediction


@app.route('/')
def first_line():
    """
    This is the first line of the app.py file for 2020
    """
    print("This is the first line of the app.py file for 2020")
    return 'This is an app to predict the average wage of a country.'

@app.route("/predict", methods=["POST"])
def predict():
    """
    predict the average wage of a country in 2020
    """
    data = request.get_json()
    country_data = data['Country']
    country_data = pd.DataFrame([country_data], columns=['Country', '2000', '2005', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])
    X = country_data.iloc[:, 1:].values
    with open('model.pkl', 'rb') as f:
        regressor = pickle.load(f)
    y_pred = regressor.predict(X)
    return render_template(
        "index.html", prediction=str(y_pred[0]) + " in 2020")

#ask the user to guess the country with highest average wage in 2022
@app.route("/guess/<country>")
def guess_country(country):
    """
    guess the country with highest average wage in 2022
    """
    # check if the country is in the dataset
    if country in df['Country'].values:
        # check if the country is in the top 1
        if df.head(1)['Country'].values[0] == country:
            return "You are correct!"
        else:
            return "You are wrong"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)