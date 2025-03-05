import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cycling_agent.strava import authenticate, fetch_metrics

def test_authenticate(capsys):
    authenticate()
    captured = capsys.readouterr()
    assert "Authenticating with Strava..." in captured.out

def test_fetch_metrics():
    metrics = fetch_metrics()
    assert isinstance(metrics, dict)
    assert metrics["distance"] == 30
    assert metrics["heart_rate"] == 150
    assert metrics["power"] == 180