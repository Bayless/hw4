#!/usr/bin/python
from hashlib import sha1

usrpwd = {}

def makeCsv():
    csv = open('data/userCsv.csv').read().strip("\n")
    if (len(csv)==0):
            return
    if "\n" in csv: # more than one entry
        csv = csv.split("\n")
        for row in csv:
            row = row.split(",")
            usrpwd[row[0]] = row[1]#1st col is user 2nd is hashed pwd
    else:
        csv = csv.split(",")
        usrpwd[csv[0]] = csv[1]

def authenticate(user,password):
    inIt = False
    #theReason=""
    passHash = sha1(password).hexdigest()#hash it
    if (user in usrpwd.keys()):
        if (passHash == usrpwd[user]):
            inIt = True
            #   else:
            #      theReason = "Incorrect password entered."
  #  else:
   #     theReason = False
    return inIt

def register(user,password):
    theError = ""
    passHash = sha1(password).hexdigest()#hash it
    if (user in usrpwd.keys()):
        theError = "This username is already registered."
    else:
        if ("," in user):
            theError = "Username has invalid character (a comma)."
        else:
            with open('data/userCsv.csv','a') as csv:
                csv.write(user + "," + passHash + "\n")#add row in csv
                theError = "Your account was successfully created!"
                usrpwd[user] = passHash#add entry in dict
    return theError
