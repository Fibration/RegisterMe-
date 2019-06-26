import os
from dotenv import load_dotenv

# load dotenv
APP_ROOT = os.path.join(os.path.dirname('config.py'), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'whatever'