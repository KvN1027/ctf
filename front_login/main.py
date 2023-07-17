from flask import Flask, redirect, url_for, render_template,request,flash,session
import random
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY']= 'meowmeow'


@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        try:
            user = request.form["user"]
            password = request.form["password"]
            if user == "admin" and password == "this_is_p@ssw0rd" :
                return "flag"
            else  :
                return "login failed"
        except:
            return "err"
    else:
        session["iflogin"] = "no"
        return render_template("index.html",logininfo="")



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)