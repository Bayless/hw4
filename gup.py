#Bayle SMith-Salzberg
#SoftDev1 pd8
#HW04 -- Big, Heavy, Wood
#2016-09-29

from flask import Flask, render_template, request
from hashlib import sha1

app = Flask(__name__)


@app.route("/login/")
def home():
        processForms.loadDict()
        return render_template("dn.html")

#WITHOUT hash rn
@app.route("/authenticate/", methods=['POST'])
def auth():
        retAuth = processForms.authenticate(request.form['user'], request.form['pass'])
        return render_template("auth.html", verdict=retAuth[0], reason=retAuth[1])

@app.route("/register/", methods=['POST'])
def reg():
        return render_template("dn.html", errorMsg=processForms.register(request.form['newUser'],request.form['newPass']))
@app.route("/")
def temp():
    print"\n\n\n"
    print "this the apperrino"
    print app
    print "this is username"
    print request.args
    return render_template("input.html")

@app.route("/auth", methods=['POST'])
def checkU(username):
    if file.read().find(username) != -1:
        return True
    
def author():
    print"\n\n\n"
    print "this the apperrino"
    print app
    print "this is username"
    if request.form['username'] == "bayle" and request.form['password'] == "bss":#username in csv, password in csv
        return render_template("success.html")
    else:
        return render_template("failure.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
