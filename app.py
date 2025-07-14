from flask import Flask, render_template, request
import joblib

import os
os.environ['GROQ_API_KEY'] = "gsk_j3Lh13KQksnY8M1WciM8W"

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.sealion.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    # db
    return(render_template("main.html"))

@app.route("/llama",methods=["GET","POST"])
def llama():
    return(render_template("llama.html"))

@app.route("/llama_reply",methods=["GET","POST"])
def llama_reply():
    q = float(request.form.get("q"))
    #load model
    return(render_template("llama_reply.html",r=pred))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    return(render_template("dbs.html"))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    q = float(request.form.get("q"))
    # load model
    model = joblib.load("dbs.jl")
    # make prediction
    pred = model.predict([[q]])
    return(render_template("prediction.html",r=pred))

if __name__ == "__main__":
    app.run()