from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {"username":"Rakka"}
    posts = [
        {
            "author": {"username":"Johny"},
            "body":"Beautiful day in Africa"
        },
        {
            "author": {"username":"Susan"},
            "body":"The Anime Movie was so cool!"
        },
        {
            "author": {"username": "Raizo"},
            "body": "The strongest ninja has arrive!"
        }

    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # If the client request a POST method.
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template("login.html", title="Sign In", form=form)


# routes flow: add decorator @app.route(url) and
#              create a func that return html string or render template