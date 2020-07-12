from app import app
from flask import render_template, redirect, request

@app.route("/")
def index():
    return render_template("/public/index.html")

@app.route("/about")
def about():
    return "<h1 style='color: green'><strong>About</strong></h1>"

@app.route("/sign-up" , methods = ['GET','POST'])
def signup():
    if request.method == "POST":
        req = request.form

        print(req)
        return redirect(request.url)

    return render_template('/public/templates/sign_up.html')


