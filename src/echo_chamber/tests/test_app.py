import pytest
import json
from echo_chamber.app import create_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

# --- Passing Tests ✅ ---

def test_home_page(client):
    """Tests the home page for a successful response."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_add_endpoint_success(client):
    """Tests the /add endpoint with valid integers."""
    response = client.get('/add/5/10')
    assert response.status_code == 200
    assert response.json == {"sum": 15}

def test_add_endpoint_invalid_input(client):
    """Tests the /add endpoint with non-integer input."""
    response = client.get('/add/five/10')
    assert response.status_code == 400
    assert "error" in response.json

# --- Failing Tests ---

def test_echo_endpoint_broken_assertion(client):
    """Checks the /echo endpoint but has a broken assertion. (This will fail)"""
    payload = {'message': 'this test is designed to fail'}
    response = client.post('/echo', json=payload)
    assert response.status_code == 200
    # Intentionally broken assertion
    assert response.json['echo'] == 'this message does not match'

def test_nonexistent_page(client):
    """Tries to access a page that doesn't exist. (This will fail)"""
    response = client.get('/nonexistent')
    # This will fail because the actual status code will be 404
    assert response.status_code == 200