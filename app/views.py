from app import app
from flask import render_template, redirect, request, jsonify,make_response

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

users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creatof of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}

@app.route("/profile/<username>")
def profile(username):

    user = None

    if username in users:
        user = users[username]

    return render_template("public/profile.html", username = username,user  = user)

@app.route("/multiple/<foo>/<bar>/<baz>")
def multi(foo, bar, baz):
    return "foo is {} baa is {} and baz is {}".format(foo,bar,baz)

@app.route("/json",methods = ["POST"])
def json():
    if request.is_json:
        req = request.get_json()
        response = {
            "Message": "Json received",
            "name": req.get("name")
        }

        res = make_response(jsonify(response), 200)

        return res
    else:

        res = make_response(jsonify({"message": "No json received"}), 400)

        return res

