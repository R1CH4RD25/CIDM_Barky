import pytest
import requests

from flask import url_for

from ..api.flaskapi import FlaskBookmarkAPI

LOCALHOST = 'http://127.0.0.1:5000/'


def test_api_can_connect():
    res = requests.get(LOCALHOST)
    assert res != None


def test_api_index():
    res = requests.get(LOCALHOST)
    assert res != None


@pytest.fixture
def api():
    return FlaskBookmarkAPI()


def test_index(api):
    response = requests.get(f"{LOCALHOST}/")
    # assert response.text == 'Barky API'


def test_one(api):
    response = requests.get(f"{LOCALHOST}/api/one/123")
    assert response.text == 'The provided id is 123'


def test_all(api):
    response = requests.get(f"{LOCALHOST}/api/all")
    assert response.text == 'all records'


def test_first(api):
    response = requests.get(f"{LOCALHOST}/api/first/property/value/sort")
    assert response.text == 'the first '


def test_many(api):
    response = requests.get(f"{LOCALHOST}/api/many/property/value/sort")
    # assert response.text == 'many records'
