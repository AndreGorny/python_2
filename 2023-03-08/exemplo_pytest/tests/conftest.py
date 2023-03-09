import pytest
import requests
from unittest.mock import MagicMock


@pytest.fixture()
def mock_get(monkeypatch):
    mock_object = MagicMock()
    monkeypatch.setattr(requests, "get", mock_object)
    return mock_object
