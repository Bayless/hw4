#!/usr/bin/python
#Bayle Smith-Salzberg
#SoftDev1 pd8
#HW04 -- Big, Heavy, Wood
#2016-09-29

from flask import Flask, render_template, request, redirect,url_for,session
from hashlib import sha1
from utils import verify


app = Flask(__name__)

@app.route("/")
def logRegister():
        if 'username' in session:
            return 'logged in as ' + session['username']
        return 'you are not logged in'

@app.route("/login/",methods=['POST'])
def auth():
        retAuth = verify.authenticate(request.form['username'], request.form['password'])
        if retAuth:
                session['username']=request.form['username']
                return redirect(url_for('logRegister'))
        else:
                return 'wrong password, try again'

@app.route("/register/", methods=['POST'])
def reg():
        return redirect(url_for('logRegister'))

@app.route("/jacobo")
def js():
    return redirect("http://xkcd.com")

if __name__ == "__main__":
    app.debug = True
    app.run()
