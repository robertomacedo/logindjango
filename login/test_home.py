import pytest


def test_home_status_code(CadastroView):
    resp = CadastroView.get('/')
    assert resp.status_code == 200
