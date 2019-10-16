from flask import Flask
from flask import render_template, request
from forms import MyForms


app = Flask(__name__)
app.config['SECRET_KEY'] = "eu485jd54fdjas98gdfakjibiurjmnvkaiasdf541f58sj4"


items = [{"title": "Title here", "things": []}]


@app.route("/")
@app.route("/home")
def home():
    """route to signup/login"""
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """route to login """
    form = MyForms()
    return render_template("login.html", form=form)


@app.route("/signup")
def signup():
    """route to signup """
    form = MyForms()
    return render_template("signup.html", form=form)


@app.route("/todo")
def todo():
    form = MyForms()
    return render_template("delete.html", form=form)


@app.route("/title", methods=["GET", "POST"])
def title():
    form = MyForms()
    t = request.form["title"]
    items[0]["title"] = t.upper()
    return render_template("todo.html", form=form, items=items)


@app.route("/list", methods=["GET", "POST"])
def list():
    form = MyForms()
    l = request.form["todo_items"]
    items[0]["things"].append(l)
    return render_template("todo.html", form=form, items=items)


@app.route("/delete", methods=["POST"])
def delete():
    form = MyForms()
    items[0]["things"] = []
    items[0]["title"] = ""
    return render_template("todo.html", form=form, items=items)





if __name__ == "__main__":
    app.run(port=4000, debug=True)