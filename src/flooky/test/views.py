
from flask import Blueprint

blueprint = Blueprint('test', __name__, url_prefix='/test')


@blueprint.route('/ping')
def ping():
    return 'test pong'

