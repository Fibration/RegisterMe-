import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

# load dotenv
APP_ROOT = os.path.join(os.path.dirname('config.py'), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'whatever'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False