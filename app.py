import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_args
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# Create instance of Flask
app = Flask(__name__)

# Set up configurations for MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# Set up secret key
app.secret_key = os.environ.get("SECRET_KEY")

# Create an instance of PyMongo
mongo = PyMongo(app)

# Code Snippet 1: Edb83 - Pagination
# https://github.com/Edb83/self-isolution/blob/master/app.py
# Pagination  recipes per page
PER_PAGE = 9


# Pagination
def paginated(recipes):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE

    return recipes[offset: offset + PER_PAGE]


def pagination_args(recipes):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    total = len(recipes)

    return Pagination(page=page, per_page=PER_PAGE,
                      css_framework='bootstrap4', total=total)
# /End code snippet


# Index
@app.route("/")
@app.route("/index")
def index():
    """
    Home page displays the last 6 recipes added
    """
    latest_recipes = mongo.db.recipes.find().sort('_id', DESCENDING).limit(6)
    return render_template(
        "index.html", latest_recipes=latest_recipes, title="Home")


# Recipes
@app.route("/all_recipes")
def all_recipes():
    """
    Displays all recipes, paginated to 9 per page
    """
    recipes = list(mongo.db.recipes.find())
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    return render_template(
        "all_recipes.html", recipes=recipes_paginated,
        pagination=pagination, title="All Recipes")


# Search Recipes
@app.route("/search_recipes")
def search_recipes():
    """
    Search the recipes collection and return results
    Paginated 9 per page
    """
    query = request.args.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    return render_template(
        "all_recipes.html", recipes=recipes_paginated,
        pagination=pagination, title="Search Results")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Register a new user and add them to the database
    """
    if request.method == "POST":

        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, please choose another")
            return redirect(url_for("register"))

        # check if email already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email already registered")
            return redirect(url_for("register"))

        register_user = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        # Add new user to the db
        mongo.db.users.insert_one(register_user)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for(
            "profile", username=session["user"]))
    return render_template("register.html", title="Register")


# Log In
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Check if username & password match existing user & Login user
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                # If invalid password match
                flash("Incorrect Username/Password")
                return redirect(url_for("login"))

        else:
            # If username doesn't exist
            flash("Incorrect Username/Password")
            return redirect(url_for("login"))

    return render_template("login.html", title="Log In")


# Profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Display recipes added by the current logged in user
    """
    # Get the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # Once session['user] cookie is truthy return their profile page
    if session["user"]:
        recipes = mongo.db.recipes.find(
            {"added_by": session["user"]}).sort("_id", -1)
        return render_template(
            "profile.html", username=username,
            recipes=recipes, title="Profile")

    return redirect(url_for("login"))


# Log Out
@app.route("/logout")
def logout():
    """
    Clears the session & redirects to login page
    """
    session.pop("user")
    flash("You are now logged out")
    return redirect(url_for("login"))


# One recipe
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """
    Displays the full recipe
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipe, title="Recipe")


# Add Recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Allows a logged in user to add a recipe
    """
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "category_name": request.form.get("category_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "recipe_url": request.form.get("recipe_url"),
            "added_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_recipe.html", categories=categories, title="Add Recipe")


# Edit Recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Allows a logged in user to edit a recipe they have added
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)

    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session["user"] == recipe["added_by"] or session["user"] == "admin":

        if request.method == "POST":
            submit_recipe = {"$set":
                             {
                                "recipe_name": request.form.get("recipe_name"),
                                "recipe_description": request.form.get(
                                    "recipe_description"),
                                "category_name": request.form.get(
                                    "category_name"),
                                "prep_time": request.form.get("prep_time"),
                                "cook_time": request.form.get("cook_time"),
                                "ingredients": request.form.getlist(
                                    "ingredients"),
                                "method": request.form.getlist("method"),
                                "recipe_url": request.form.get("recipe_url")
                             }
                             }
            mongo.db.recipes.update(
                {"_id": ObjectId(recipe_id)}, submit_recipe)
            flash("Recipe Successfully Updated")
            return redirect(url_for("profile", username=session["user"]))

        return render_template(
            "edit_recipe.html", recipe=recipe,
            categories=categories, title="Edit Recipe")

    flash("You do not have permission to do that")
    return redirect(url_for('all_recipes'))


# Delete Recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Allows a logged in user to delete a recipe they have added
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session["user"] == recipe["added_by"] or session["user"] == "admin":
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        flash("Recipe deleted")
        return redirect(url_for("profile", username=session["user"]))

    flash("You do not have permission to do that")
    return redirect(url_for('all_recipes'))


# Manage Recipes
@app.route("/manage_recipes", methods=["GET", "POST"])
def manage_recipes():
    """
    Displays all recipes for an admin user
    Paginated to 9 per page
    """
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session["user"] == "admin":
        recipes_paginated = paginated(recipes)
        pagination = pagination_args(recipes)
        return render_template(
            "manage_recipes.html", recipes=recipes_paginated,
            pagination=pagination, title="Manage Recipes")

    flash("You do not have permission to do that")
    return redirect(url_for('all_recipes'))


# Manage Categories
@app.route("/manage_categories")
def manage_categories():
    """
    Displays all categories for an admin user
    """
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session["user"] == "admin":
        return render_template(
            "manage_categories.html", categories=categories,
            title="Manage Categories")

    flash("You do not have permission to do that")
    return redirect(url_for('all_recipes'))


# Search Categories
@app.route("/search_categories", methods=["GET", "POST"])
def search_categories():
    """
    Search the categories collection and return results
    """
    query = request.form.get("query")
    categories = list(mongo.db.categories.find({"$text": {"$search": query}}))
    return render_template(
        "manage_categories.html", categories=categories,
        title="Search Categories")


# Add Category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    Allows an admin user to add a category
    """

    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session["user"] == "admin":
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.insert_one(category)
            flash("New Category Added")
            return redirect(url_for("manage_categories"))

        return render_template("add_category.html", title="Add Category")

    flash("You do not have permission to do that")
    return redirect(url_for('all_recipes'))


# Edit Category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    Allows an admin user to edit a category
    """
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session["user"] == "admin":
        if request.method == "POST":
            update_category = {"$set":
                               {
                                    "category_name": request.form.get(
                                        "category_name")
                               }
                               }
            mongo.db.categories.update(
                {"_id": ObjectId(category_id)}, update_category)
            flash("Category Updated")
            return redirect(url_for("manage_categories"))

        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
        return render_template(
            "edit_category.html", category=category, title="Edit Category")

    flash("You do not have permission to do that")
    return redirect(url_for('all_recipes'))


# Delete Category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    Allows an admin user to delete a category
    """

    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session["user"] == "admin":
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("Category Deleted")
        return redirect(url_for("manage_categories"))

    flash("You do not have permission to do that")
    return redirect(url_for('all_recipes'))


# Manage Users
@app.route("/manage_users")
def manage_users():
    """
    Displays all users for an admin user
    """

    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session["user"] == "admin":
        users = list(mongo.db.users.find().sort("username", 1))
        return render_template(
            "manage_users.html", users=users, title="Manage Users")

    flash("You do not have permission to do that")
    return redirect(url_for('all_recipes'))


# Search Users
@app.route("/search_users", methods=["GET", "POST"])
def search_users():
    """
    Search users collection and return the result
    """
    query = request.form.get("query")
    users = list(mongo.db.users.find({"$text": {"$search": query}}))
    return render_template(
        "manage_users.html", users=users, title="Search Users")


# Edit User
@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    """
    Allows an adminuser to edit a user
    """
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session["user"] == "admin":
        if request.method == "POST":
            update_user = {"$set":
                           {
                                "username": request.form.get("username"),
                                "email": request.form.get("email")
                           }
                           }
            mongo.db.users.update(
                {"_id": ObjectId(user_id)}, update_user)
            flash("User Updated")
            return redirect(url_for("manage_users"))

        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return render_template("edit_user.html", user=user, title="Edit User")

    flash("You do not have permission to do that")
    return redirect(url_for('all_recipes'))


# Delete User
@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    """
    Allows an admin user to delete a user
    """
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session["user"] == "admin":
        mongo.db.users.remove({"_id": ObjectId(user_id)})
        flash("User Deleted")
        return redirect(url_for("manage_users"))

    flash("You do not have permission to do that")
    return redirect(url_for('all_recipes'))


# Contact
@app.route("/contact")
def contact():
    """
    Displays the contact form
    """
    return render_template("contact.html", title="Contact")


# 404 Error
@app.errorhandler(404)
def not_found_error(error):
    """
    Handles a 404 error
    """
    return render_template('404.html', error=error, title="404 Error"), 404


# Set how & where to run the app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
