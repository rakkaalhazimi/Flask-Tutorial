from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required # If you decorate a view with this, it will ensure that the current user is
                # logged in and authenticated before calling the actual view.
def index():
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
    return render_template("index.html", title="Home", posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()
    if form.validate_on_submit(): # If the client request a POST method.
        user = User.query.filter_by(username=form.username.data).first()
        # if the login not success
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))

        # if the login success
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)

    return render_template("login.html", title="Sign In", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

# routes flow: add decorator @app.route(url) and
#              create a func that return html string or render template