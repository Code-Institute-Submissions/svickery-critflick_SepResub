import os
from flask import (
    Flask, flash, render_template, redirect, 
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reviews")
def reviews():

    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    """
        Search reviews by the title and country name
    """
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    return render_template("reviews.html", reviews=reviews)



@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        session["user"] = request.form.get("username").lower()
        flash("Sign Up Complete!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
        render user profile from db
    """
    reviews = mongo.db.reviews.find()

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username, reviews=reviews)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    
    if request.method == "POST":
        movie_review = {
            "title": request.form.get("title"),
            "year": request.form.get("year"),
            "language": request.form.get("language"),
            "genre": request.form.get("genre"),
            "director": request.form.get("director"),
            "actors": request.form.getlist("actors[]"),
            "rating": request.form.get("rating"),
            "run_time": request.form.get("run_time"),
            "image": request.form.get("image"),
            "review": request.form.get("review"),
            "created_by": session["user"]
        }
        print(movie_review)

        mongo.db.reviews.insert_one(movie_review)
        flash("Movie Review Added!")
        return redirect(url_for("reviews"))

    return render_template("add_review.html")


@app.route("/edit_review/<movie_review_id>", methods=["GET", "POST"])
def edit_review(movie_review_id):
    movie_review = mongo.db.reviews.find_one({"_id": ObjectId(movie_review_id)})   

    if request.method == "POST":
        submit = {
                "title": request.form.get("title"),
                "year": request.form.get("year"),
                "language": request.form.get("language"),
                "genre": request.form.get("genre"),
                "director": request.form.get("director"),
                "actors": request.form.getlist("actors[]"),
                "rating": request.form.get("rating"),
                "run_time": request.form.get("run_time"),
                "image": request.form.get("image"),
                "review": request.form.get("review"),
                "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(movie_review_id)}, submit)
        flash("Review Successfully Updated!")
    place = mongo.db.reviews.find_one({"_id": ObjectId(movie_review_id)})
    return render_template("edit_review.html", movie_review=movie_review)


@app.route("/delete_review/<movie_review_id>")
def delete_review(movie_review_id):
    mongo.db.reviews.remove({"_id": ObjectId(movie_review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("reviews"))


@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 404


if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = False)