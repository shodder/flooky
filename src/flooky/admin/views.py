
from flask import Blueprint

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/ping')
def ping():
    return 'admin pong'

