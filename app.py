import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_time_not_zero(client):
    resp = client.get('/time')
    data = json.loads(resp.data)
    assert 'time' in data
    assert data['time'] != 0
