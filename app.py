#!/usr/bin/env python3

from flask import Flask, render_template, request
from joblib import load
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        name = dict(request.form)["name"]
        years = dict(request.form)["years"]
        regressor = load("./linear_regression_model.joblib")
        if years:
            prediction = regressor.predict([[float(years)]])
        else:
            prediction = 25000
    elif request.method == "GET":
        name = ""
        prediction = 25000

    result = Result(
    Name = str(name),
    YearsExperience = float(years),
    Prediction = float(prediction)
    )
    db.session.add(result)
    db.session.commit()

    return render_template("predict.html", name = name.capitalize(), salary = format(int(prediction), ','))

if __name__ == "__main__":
    app.run(debug=True)
