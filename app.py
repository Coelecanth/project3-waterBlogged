import os
from functools import wraps
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

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_fdata")
def get_fdata():
    tasks = list(mongo.db.fdata.find())
    return render_template("tasks.html", tasks=tasks)


# function to test if there is a user logged - defensive programming
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # no "user" in session
        if "user" not in session:
            flash("You must log in to view this page")
            return redirect(url_for("login"))
        # user is in session
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    # find all tasks
    tasks = list(mongo.db.fdata.find())
    return render_template("tasks.html", tasks=tasks)


@app.route("/search", methods=["GET", "POST"])
def search():
    # find only the tasks the user has queried
    query = request.form.get("query")
    tasks = list(mongo.db.fdata.find({"$text": {"$search": query}}))
    return render_template("tasks.html", tasks=tasks)


# function to register a user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form.get('username').lower()
        password = request.form.get('password')
        confirm_password = request.form.get('password1')
        if password == confirm_password:
            existing_user = mongo.db.users.find_one({"username": username})
            if existing_user:
                flash("Username already exists", 'error')
                return redirect(url_for("register"))
            # Register the new user
            hashed_password = generate_password_hash(password)
            new_user = {
                "username": username,
                "password": hashed_password,
                "is_superuser": "false"
            }
            mongo.db.users.insert_one(new_user)
            # Put the new user into 'session' cookie
            session["user"] = username
            flash("Registration Successful!", 'success')
            return redirect(url_for("profile", username=username))
        else:
            flash('Passwords do not match!', 'error')
    return render_template('register.html')


# function to logon a user
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in fishinLog/user db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):  # noqa
                session["user"] = request.form.get("username").lower()  # noqa
                if existing_user["is_superuser"] == "true":
                    session["is_superuser"] = True
                    flash("Welcome, {}".format(request.form.get("username")))  # noqa
                else:
                    session["is_superuser"] = False
                    flash("Welcome, {}".format(request.form.get("username")))  # noqa
                return redirect(url_for("profile", username=session["user"], is_superuser=session["is_superuser"]))  # noqa
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
@login_required
def profile(username):
    # grab the session user's username from db
    user = mongo.db.users.find_one({"username": session["user"]})
    if user:
        return render_template("profile.html", username=user["username"],
                is_superuser=session["is_superuser"])
    return redirect(url_for("login"))


@app.route("/logout")
@login_required
def logout():
    # remove user from session cookie
    session.clear()
    flash("You have been logged out")
    # use .clear() instead of .pop() as mutiple sessions
    return redirect(url_for("login"))


# create new record
@app.route("/add_task", methods=["GET", "POST"])
@login_required
def add_task():
    if request.method == "POST":
        fd_public = "on" if request.form.get("fd_public") else "off"
        task = {
            "fd_wtemp": request.form.get("fd_wtemp"),
            "fd_cat_name": request.form.get("fd_cat_name"),
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


# Update of current record of a user
@app.route("/edit_task/<fdata_id>", methods=["GET", "POST"])
@login_required
def edit_task(fdata_id):
    task = mongo.db.fdata.find_one({"_id": ObjectId(fdata_id)})
    if session["user"].lower() == task["fd_created_by"].lower(): 
        # the session["user"] must be the user who created this task to edit
        if request.method == "POST":
            fd_public = "on" if request.form.get("fd_public") else "off"
            submit = {
                "fd_wtemp": request.form.get("fd_wtemp"),
                "fd_cat_name": request.form.get("fd_cat_name"),
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
            mongo.db.fdata.update_one({"_id": ObjectId(fdata_id)},
                {"$set": submit})
            flash("Task Successfully Updated")
        task = mongo.db.fdata.find_one({"_id": ObjectId(fdata_id)})
        categories = mongo.db.categories.find().sort("cat_name", 1)
        return render_template("edit_task.html", task=task,
            categories=categories)
    # not the correct user to edit this task
    flash("You don't have access to edit this task")
    return redirect(url_for("get_tasks"))


@app.route("/delete_task/<fdata_id>")
@login_required
def delete_task(fdata_id):
    mongo.db.fdata.delete_one({"_id": ObjectId(fdata_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_fdata"))


@app.route("/get_categories")
@login_required
def get_categories():
    if not session["is_superuser"]:
        flash("Access Denied: Superuser Access Only")
        return redirect(url_for("get_fdata"))
    categories = list(mongo.db.categories.find().sort("cat_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
@login_required
def add_category():
    if not session["is_superuser"]:
        flash("Access Denied: Superuser Access Only")
        return redirect(url_for("get_fdata"))
    if request.method == "POST":
        category = {
            "cat_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Location Added")
        return redirect(url_for("get_categories"))

    return render_template("add_categories.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
@login_required
def edit_category(category_id):
    if not session["is_superuser"]:
        flash("Access Denied: Superuser Access Only")
        return redirect(url_for("get_fdata"))
    if request.method == "POST":
        submit = {
            "cat_name": request.form.get("category_name")
        }
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, 
            {"$set": submit})
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_categories.html", category=category)


@app.route("/delete_category/<category_id>")
@login_required
def delete_category(category_id):
    if not session["is_superuser"]:
        flash("Access Denied: Superuser Access Only")
        return redirect(url_for("get_fdata"))
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
