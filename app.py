from flask import Flask, render_template, request
import os
import pandas as pd
import numpy as np
from src.mlProject.pipeline.prediction import PredictionPipeline

app = Flask(__name__) #initialise flask app

@app.route("/", methods=['GET']) #route to display the homepage
def homePage():
    return render_template("index.html")

@app.route("/train", methods=['GET'])
def training():
    os.system("python3 main.py")
    return "training successful"

@app.route("/predict", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        try:
            fixed_acidity= float(request.form["fixed_acidity"])
            volatile_acidity = float(request.form["volatile_acidity"])
            residual_sugar = float(request.form["residual_sugar"])
            citric_acid = float(request.form["citric_acid"])
            chlorides = float(request.form["chlorides"])
            free_so2 = float(request.form["free_so2"])
            total_so2 = float(request.form["total_so2"])
            sulphates = float(request.form["sulphates"])
            alcohol = float(request.form["alcohol"])
            ph = float(request.form["ph"])
            density = float(request.form["density"])

            data = [fixed_acidity, volatile_acidity, residual_sugar, citric_acid, chlorides, free_so2, total_so2,
                     sulphates, alcohol, ph, density]
            
            data = np.array(data).reshape(1,11)

            obj = PredictionPipeline()
            predict = obj.predict(data)
            return render_template("result.html", prediction = str(predict))
        except Exception as e:
            print(f"Exception is {e}")
            return "Something is wrong"
    else:
        return render_template("index.html")

                                     



if __name__ == "__main__":
    # app.run(host="0.0.0.0", port= 8080, debug = True) - remove debug while deploying
    app.run(host="0.0.0.0", port= 8080)