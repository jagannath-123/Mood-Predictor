import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from flask import Flask, url_for, render_template,request

from app import MoodPredictor

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    result=""
    if request.method=="GET":
        text=request.args.get('text', '')
        if text!="":
            result = model.predict(text)
        else:
            result="Enter some text"

    return render_template("index.html",result=result)


if __name__ == "__main__":
    model = MoodPredictor()
    app.run(debug=True)