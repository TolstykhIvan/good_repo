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

def test_metrics_increments(client):
    # Делаем несколько запросов к /time
    for _ in range(3):
        client.get('/time')
    resp = client.get('/metrics')
    data = json.loads(resp.data)
    assert 'count' in data
    # Счётчик должен быть не меньше 3 (учитывая возможные запросы из других тестов)
    assert data['count'] >= 3
