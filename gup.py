#!/usr/bin/python
#Bayle Smith-Salzberg
#SoftDev1 pd8
#HW05 -- The greatest flask app in the world
#2016-10-07

from flask import Flask, render_template, request, redirect,url_for,session
from hashlib import sha1
from utils import verify
import os

app = Flask(__name__)

ranStr = os.urandom(32)#generates 32 bits of random data
app.secret_key = ranStr

@app.route("/")
def logRegister():
        verify.makeCsv()
        if 'username' in session:
                namo = session['username']
                session.pop('username', None)
                return render_template("logout.html",user=namo)
        return render_template("input.html",message='')

@app.route("/authenticate/",methods=['POST'])
def auth():
        retAuth = verify.authenticate(request.form['username'], request.form['password'])
        if retAuth:
                session['username']=request.form['username']
                return redirect(url_for('logRegister'))
        else:
                return 'wrong password, try again'

@app.route("/register/", methods=['POST'])
def reg():
        verify.register(request.form['usr'],request.form['pwd'])
        return render_template('input.html',message='You are registered!')

@app.route("/jacobo")
def js():
    return redirect("http://xkcd.com")

@app.route("/logout/", methods=['POST'])
def logOut():
        return redirect(url_for('logRegister'))

if __name__ == "__main__":
    app.debug = True
    app.run()
