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
    if request.form['username'] == "bayle" and request.form['password'] == "bss":
        return render_template("success.html")#make this a template pls
    else:
        return render_template("failure.html")#make this a template pls

if __name__ == "__main__":
    app.debug = True
    app.run()
