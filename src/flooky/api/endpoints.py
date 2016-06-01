
from flask import Blueprint

blueprint = Blueprint('api', __name__, url_prefix='/api/latest')


@blueprint.route('/ping')
def ping():
    return 'api pong'

