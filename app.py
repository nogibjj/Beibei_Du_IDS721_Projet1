import numpy as np
from flask import Flask, render_template
import pickle


app = Flask(__name__)
regressor = pickle.load(open("model.pkl", "rb"))

def guess_2022():
    test_data = np.array([55366, 58092, 61048, 61132, 61634, 61347, 62263, 63845, 63942,
        64618, 65303, 66383])
    prediction = regressor.predict(test_data)
    print("It is working!")
    return prediction


@app.route('/')
def first_line():
    print("This is the first line of the app.py file")
    return 'This is an app to predict the average wage of a country.'

# write me a function that takes in a regressor and returns a prediction
@app.route('/predict/<regressor>')
def avg_wage_pred(regressor):
    print("It is working!")
    prediction = guess_2022()
    return prediction


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)