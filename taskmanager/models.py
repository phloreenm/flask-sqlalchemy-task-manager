from taskmanager import db

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        return f"Category('{self.category_name}')" # noqa

class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.String(250), nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("category.id", 
        ondelete="CASCADE"), 
        nullable=False
        )

    def __repr__(self):
        return "#{0} - Task: {1} - Description: {2} - Due Date: {3}".format(
            self.id,
            self.task_name,
            self.is_urgent,
            self.due_date) # noqa
            
        # OR:
        # return f"Task('{self.task_name}', '{self.task_description}', '{self.due_date}')" # noqa