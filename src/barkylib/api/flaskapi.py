from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqla_repository import *
from baseapi import AbstractBookMarkAPI

# init from dotenv file
#from dotenv import load_dotenv
#load_dotenv()

app = Flask(__name__)

class FlaskBookmarkAPI(AbstractBookMarkAPI):
    """
    Flask 
    """
    def __init__(self) -> None:
        super().__init__()
    
    @app.route('/')
    def index(self):
        return f'Barky API'

    @app.route('/api/one/<id>')
    def one(self, id):
        return f'The provided id is {id}'

    @app.route('/api/all')
    def all(self):
        return f'all records'

    @app.route('/api/first/<property>/<value>/<sort>')
    def first(self, filter, value, sort):
        return f'the first '
        pass
    
    def many(self, filter, value, sort):
        pass
    
    def add(bookmark):
        pass

    def delete(bookmark):
        pass

    def update(bookmark):
        pass


def create_app():
    app = Flask(__name__)
    app.config.update({"TESTING": True})

    app.add_url_rule("/", "index", view_func=index_endpoint)
    app.add_url_rule(
        "/allocate", "allocate", view_func=allocate_endpoint, methods=["POST"]
    )

    return app