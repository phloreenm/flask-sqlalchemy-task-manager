from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")

@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # This checks if the method is POST; if yes, then it does the bussiness logic below:
    if request.method == "POST":
        new_category = Category(category_name=request.form.get("category_name"))
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for("categories"))
    # the GET method gets this return, to display the Add Category html page
    return render_template("add_category.html")

@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # select the specified item by id
    category = Category.query.get_or_404(category_id)
    # if method equals POST
    if request.method == "POST":
        # assign the new name from the post to the object goin go the DB
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)




