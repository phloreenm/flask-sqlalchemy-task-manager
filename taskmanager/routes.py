from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    """home() function - default page"""
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)

@app.route("/categories")
def categories():
    """categories() function"""
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """ This checks if the method is POST; if yes, then it does the bussiness logic below:"""
    if request.method == "POST":
        new_category = Category(category_name=request.form.get("category_name"))
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for("categories"))
    # the GET method gets this return, to display the Add Category html page
    return render_template("add_category.html")

@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """edit_category() function"""
    # select the specified item by id
    category = Category.query.get_or_404(category_id)
    # if method equals POST
    if request.method == "POST":
        # assign the new name from the post to the object goin go the DB
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)

@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    """delete_category() function"""
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    """add_task() function"""
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        new_task = Task(
            task_name = request.form.get("task_name"),
            task_description = request.form.get("task_description"),
            is_urgent = bool(True if request.form.get("is_urgent") else False),
            due_date = request.form.get("due_date"),
            category_id = request.form.get("category_id")
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html", categories=categories)



