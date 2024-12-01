import pytest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from ResourceSemaphoreService import app  # Import your app


@pytest.fixture
def client() -> FlaskClient:
    """Fixture for setting up the Flask test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_set_resource_status(client):
    """Test the POST /resource/<resource_id>/status endpoint."""

    # Test valid status 'free'
    response = client.post('/resource/123/status', json={'status': 'free'})
    assert response.status_code == 200
    assert response.json == {"message": "Resource 123 is now free."}

    # Test valid status 'busy'
    response = client.post('/resource/124/status', json={'status': 'busy'})
    assert response.status_code == 200
    assert response.json == {"message": "Resource 124 is now busy."}

    # Test invalid status
    response = client.post('/resource/125/status', json={'status': 'inactive'})
    assert response.status_code == 400
    assert response.json == {"error": "Invalid status. Use 'free' or 'busy'."}


def test_get_resource_status(client):
    """Test the GET /resource/<resource_id>/status endpoint."""

    # Set the status for a resource using POST before testing GET
    client.post('/resource/123/status', json={'status': 'free'})

    # Test valid resource ID
    response = client.get('/resource/123/status')
    assert response.status_code == 200
    assert response.json == {"resource_id": "123", "status": "free"}

    # Test resource ID that does not exist
    response = client.get('/resource/999/status')
    assert response.status_code == 200
    assert response.json == {"resource_id": "999", "status": "unknown"}
