
import pytest

from flooky.app import create_app


def test_routes_by_convention():

    app = create_app()
    blueprints = app.blueprints
    assert len(blueprints) > 0

    client = app.test_client()
    response = client.get('/ping')
    assert response.status_code == 200

    for bp in app.blueprints.values():
        url_prefix = bp.url_prefix
        response = client.get('{}/ping'.format(url_prefix))
        assert response.status_code == 200


