import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

import pytest

@pytest.fixture
def client():
    """
    Create a test client using the app context.
    """
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """
    Test the '/' route.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
