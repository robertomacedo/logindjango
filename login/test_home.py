import pytest


def test_home_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200
