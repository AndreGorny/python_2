import pytest
import requests
from sqlalchemy.orm import sessionmaker
from unittest.mock import MagicMock


@pytest.fixture()
def mock_get(monkeypatch):
    mock_object = MagicMock()
    monkeypatch.setattr(requests, "get", mock_object)
    return mock_object


@pytest.fixture()
def mock_session(monkeypatch):
    mock_object = MagicMock()
    monkeypatch.setattr(sessionmaker, "Session", mock_object)
    return mock_object
