
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/philtest')
def philtest():
    return "Hello, World! (from phil)"
