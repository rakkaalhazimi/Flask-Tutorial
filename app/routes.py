from flask import render_template
from app import app

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