#Bayle SMith-Salzberg
#SoftDev1 pd8
#HW04 -- Big, Heavy, Wood
#2016-09-29

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def temp():
    print"\n\n\n"
    print "this the apperrino"
    print app
    print "this is username"
    print request.args
    return render_template("input.html")

@app.route("/auth", methods=['POST'])
def author():
    print"\n\n\n"
    print "this the apperrino"
    print app
    print "this is username"
    if request.form['username'] == #username in csv
        "bayle" and request.form['password'] ==#password in csv
        "bss":
        return render_template("success.html")
    else if:
        return render_template("failure.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
