from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Bob Jones"}
    posts = [
        {
            'author': {'username': 'James'},
            'body': "Beautiful day in Portland"
        },
        {
            'author': {'username': 'Harold'},
            'body': "I have not watched the Avengers movie because I have been living under a rock"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/philtest')
def philtest():
    return "Hello, World! (from phil)"
