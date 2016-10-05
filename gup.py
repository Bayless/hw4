#!/usr/bin/python

#Bayle SMith-Salzberg
#SoftDev1 pd8
#HW04 -- Big, Heavy, Wood
#2016-09-29

from flask import Flask, render_template, request
from hashlib import sha1
from utils import verify

app = Flask(__name__)

@app.route("/")
@app.route("/login/")
def logRegister():
        verify.makeCsv()
        return render_template("input.html")

@app.route("/authenticate/", methods=['POST'])
def auth():
        retAuth = verify.authenticate(request.form['username'], request.form['password'])
        if retAuth:
                return render_template("success.html")
        else:
                return render_template("failure.html")
@app.route("/register/", methods=['POST'])
def reg():
        return render_template("input.html", errorMsg=verify.register(request.form['usr'],request.form['pwd']))

if __name__ == "__main__":
    app.debug = True
    app.run()
