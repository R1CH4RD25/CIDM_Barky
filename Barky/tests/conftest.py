# pylint: disable=redefined-outer-name
import time
from pathlib import Path

import pytest
import requests
from requests.exceptions import ConnectionError
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.sql import delete, insert, select, text
from sqlalchemy.orm import sessionmaker, clear_mappers

import config
from flaskapi import create_app
from orm import mapper_registry, start_mappers


# chapter reworked to follow
# https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/#application-factories
# and
# https://flask.palletsprojects.com/en/2.2.x/testing/#testing-flask-applications
# P&G might be too fixated on Docker containers with their example.


@pytest.fixture
def in_memory_db():
    engine = create_engine(f"sqlite:///:memory:")
    mapper_registry.metadata.create_all(engine)
    return engine


@pytest.fixture
def file_sqlite_db():
    engine = create_engine(config.get_sqlite_filedb_uri())
    mapper_registry.metadata.create_all(engine)
    return engine


@pytest.fixture
def session(file_sqlite_db):
    start_mappers()
    yield sessionmaker(bind=file_sqlite_db)()
    clear_mappers()


@pytest.fixture
def flask_api(session):
    app = create_app()
    app.config.update({"TESTING": True})
    return app


@pytest.fixture
def test_client(flask_api):
    return flask_api.test_client()