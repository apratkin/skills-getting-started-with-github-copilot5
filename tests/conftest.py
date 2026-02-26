from fastapi.testclient import TestClient
import pytest
import copy

from src.app import app, activities


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def restore_activities():
    """Snapshot `activities` before each test and restore after test completes."""
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original)
