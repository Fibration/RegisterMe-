
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Barack Obama'}
    posts = [
        {
            'author': {'username':'Jesus'},
            'body': 'wafer'
        },
        {
            'author': {'username':'Judas'},
            'body': 'hot'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
