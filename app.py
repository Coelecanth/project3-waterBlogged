import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
print('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo= PyMongo(app)

@app.route("/")
@app.route("/get_fdata")
def get_fdata():
    tasks = list(mongo.db.fdata.find())
    return render_template("tasks.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in fishingLog db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

         # insert password checks here   

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' 
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in fishinLog/user db
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
    # grab the user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)
    # second username is the defined above, first is expected param

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user") 
    # similar to JS POP to remove just this cookie
    return redirect(url_for("login"))

# create new record 
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        fd_public = "on" if request.form.get("fd_public") else "off"
        task = {
            "fd_wtemp": request.form.get("fd_wtemp"),
            "cat_name": request.form.get("cat_name"),
            "fd_venue": request.form.get("fd_venue"),
            "fd_public": fd_public,
            "fd_date": request.form.get("fd_date"),
            "fd_created_by": session["user"],
            "fd_conditions": request.form.get("fd_conditions"),
            "fd_lurefly": request.form.get("fd_lurefly"),
            "fd_comment": request.form.get("fd_comment"),
            "fd_rate": request.form.get("fd_rate"),
            "fd_fish": request.form.get("fd_fish"),
            "fd_geoloc": request.form.get("fd_geoloc")
        }
        mongo.db.fdata.insert_one(task)
        flash("Task Successfully Added")
        return redirect(url_for("get_fdata"))

    categories = mongo.db.categories.find().sort("cat-name", 1)
    return render_template("add_tasks.html", categories=categories)

# Update of cuurent record  
@app.route("/edit_task/<fdata_id>", methods=["GET", "POST"])
def edit_task(fdata_id):
    if request.method == "POST":
        fd_public = "on" if request.form.get("fd_public") else "off"
        submit = {
            "fd_wtemp": request.form.get("fd_wtemp"),
            "cat_name": request.form.get("cat_name"),
            "fd_venue": request.form.get("fd_venue"),
            "fd_public": fd_public,
            "fd_date": request.form.get("fd_date"),
            "fd_created_by": session["user"],
            "fd_conditions": request.form.get("fd_conditions"),
            "fd_lurefly": request.form.get("fd_lurefly"),
            "fd_comment": request.form.get("fd_comment"),
            "fd_rate": request.form.get("fd_rate"),
            "fd_fish": request.form.get("fd_fish"),
            "fd_geoloc": request.form.get("fd_geoloc")
        }
        mongo.db.fdata.update_one({"_id": ObjectId(fdata_id)}, {"$set": submit})
        flash("Task Successfully Updated")


    task = mongo.db.fdata.find_one({"_id": ObjectId(fdata_id)})
    categories = mongo.db.categories.find().sort("cat_name", 1)
    return render_template("edit_task.html", task=task, categories=categories)


@app.route("/delete_task/<fdata_id>")
def delete_task(fdata_id):
    mongo.db.fdata.delete_one({"_id": ObjectId(fdata_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_fdata"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("cat_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "cat_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Location Added")
        return redirect(url_for("get_categories"))

    return render_template("add_categories.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "cat_name": request.form.get("category_name")
        }
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, {"$set": submit})
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_categories.html", category=category)    


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)