
import os

from flask import Flask
from flask import jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException

from . import config
from . import admin
from . import api
from . import test


def create_app(config=config.BaseConfig):

    app = make_json_exception_app(__name__)
    app.config.from_object(config)

    register_blueprints(app)

    @app.before_request
    def before_request():
        print('Request...')


    @app.teardown_request
    def teardown_request(exception=None):
        print('End of request...')

    return app


def make_json_exception_app(name, **kwargs):
    '''
    Taken from snippet http://flask.pocoo.org/snippets/83/

    Method to make Flask app that returns all user unhandled
    exceptions as json by default
    '''
    def make_json_error(error):
        response = jsonify(message=str(error))
        response.status_code =\
            error.code if isinstance(error, HTTPException) else 500

        return response

    app = Flask(name, **kwargs)

    for code in default_exceptions.keys():
        app.register_error_handler(code, make_json_error)

    return app


def register_blueprints(app):
    '''
    Method for loading flask blueprints by convention
    The convention expects

        ares subpackage (i.e. ares.admin)
        a views.py module (i.e. ares.admin.views)
        a module level Flask blueprint instance named blueprint
        (i.e. blueprint = Blueprint('admin'...
    '''

    path = os.path.dirname(__file__)

    for _, subdirs, _ in os.walk(path):
        if len(subdirs) == 0:
            return

        for dir_name in subdirs:
            if dir_name[:2] == '__':
                continue

            name = 'ares.{}'.format(dir_name)
            mod = __import__(name)
            mod = getattr(mod, dir_name, None)
            if mod is None:
                continue

            views = getattr(mod, 'views', None)
            if views is None:
                return

            blueprint = getattr(views, 'blueprint')
            if blueprint:
                app.register_blueprint(blueprint)

