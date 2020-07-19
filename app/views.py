from app import app
from flask import render_template, redirect, request, jsonify,make_response, flash

import os
from flask import session, url_for

from werkzeug.utils import secure_filename
from flask import send_from_directory, abort


@app.route("/")
def index():
    abort(500)
    return render_template("/public/index.html")

@app.route("/about")
def about():
    return "<h1 style='color: green'><strong>About</strong></h1>"

# @app.route("/sign-up" , methods = ['GET','POST'])
# def signup():
#     if request.method == "POST":
#         req = request.form

#         print(req)
#         return redirect(request.url)

#     return render_template('/public/sign_up.html')

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

# @app.route("/profile/<username>")
# def profile(username):

#     user = None

#     if username in users:
#         user = users[username]

#     return render_template("public/profile.html", username = username,user  = user)

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

@app.route("/guestbook")
def guestbook():
    return render_template("/public/guestbook.html")

@app.route("/guestbook/create-entry", methods = ["POST"])
def create_entry():

    req = request.get_json()
    print(req)

    res = make_response(jsonify({"message": "Json received"}), 200)

    return res


@app.route("/query")
def query():
    if request.args:
        args = request.args
        print(request.query_string)
        if "foo" in request.args:
            print(request.args.get("foo"))
        serialized = ", ".join(f'{k}: {v}'for k,v in args.items())
        return f"(Query) {serialized}", 200
    
    else:
        return "No Query receieved"

app.config["ALLOWED_IMAGE_EXT"]=["JPG","PNG","GIF","JPEG"]
app.config["MAX_FILE_SIZE"]=0.5 * 1024 * 1024


def allowed_image(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".",1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXT"]:
        return True
    
    else:
        return False

def maxFileSize(filesize):
    if int(filesize) <=app.config["MAX_FILE_SIZE"]:
        return True

    return False


@app.route("/upload_image", methods=["POST","GET"])
def upload_image():
    if request.method == "POST":
        if request.files:

            if not maxFileSize(request.cookies.get("filesize")):
                print("File Size exceeds the limit")
                return redirect(request.url)

            image = request.files["image"]
            
            if image.filename == "":
                print("No file Name present")
                return redirect(request.url)

            if not allowed_image(image.filename):
                print("File Extension is not allowed")
                return redirect(request.url)
            else:
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config["UPLOADS"],filename))

            

            return redirect(request.url)

    return render_template("/public/upload_image.html")

"""
string,
int,
float,
path,
uuid
"""

app.config["CLIENT_IMAGES"]="/home/oem/PycharmProjects/Flask_app/app/static/img/"

@app.route("/get-image/<image_name>")
def get_image(image_name):
    
    try:
        return send_from_directory(app.config["CLIENT_IMAGES"], filename = image_name
        ,as_attachment=False)
    except FileExistsError :
        abort(404)

@app.route("/cookies")
def cookies():

    cookies = request.cookies
    print(cookies.get("Flavour"))

    res = make_response("Cookies", 200)
    res.set_cookie("Flavour",
            value =  "Chocolate chip",
            max_age = 10,
            expires = None,
            path = request.path,
            domain = None,
            secure = False,
            httponly = False
            )

    return res    


app.config["SECRET_KEY"]='BNlSQffPBAZwryFH4mdHAw'

users = {
    "julian": {
        "username": "julian",
        "email": "julian@gmail.com",
        "password": "example",
        "bio": "Some guy from the internet"
    },
    "clarissa": {
        "username": "clarissa",
        "email": "clarissa@icloud.com",
        "password": "sweetpotato22",
        "bio": "Sweet potato is life"
    }
}

@app.route("/sign-in", methods = ["GET","POST"])
def sign_in():
    if request.method=="POST":
        req = request.form

        username = req.get("username")
        password = req.get("password")
        
        if not username in users:
            print("Username Not found")
            return redirect(request.url)

        else:
            user = users[username]

        if not password==user["password"]:
            print("Wrong Password")
            return redirect(request.url)

        else:
            session['USERNAME'] = user["username"]
            print("User Added to session")
            
            return redirect(url_for("profile"))


    return render_template("/public/sign_in.html")


@app.route("/profile")
def profile():

    if session.get('USERNAME', None) is not None:
        username = session.get("USERNAME")
        user = users[username]
        return render_template('/public/profile.html', user= user) 
    else:
        print("Username not found in session")
        return redirect(url_for("sign_in"))

@app.route("/sign-out")
def sign_out():
    session.pop("USERNAME",None)

    return redirect(url_for("sign_in"))

@app.route("/sign-up", methods = ["POST","GET"])
def sign_up():

    if request.method == "POST":
        req = request.form

        username = req.get("username")
        email = req.get("email")
        password = req.get("password")

        if not len(password) >=10:
            flash("Password must be at least 10 char in length", category="danger")
            return redirect(request.url)

        flash("Account Created",category="success")
        return redirect(request.url)


    return render_template("/public/sign_up.html")
