"""Desktop-startup regression tests for the preloaded challenge corpus."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_health_startup_preloads_the_challenge_corpus(tmp_path: Path) -> None:
    script = """
import json
import sys
from fastapi.testclient import TestClient
from server.app.main import app
from challenges.registry import CHALLENGE_REGISTRY
from engine.solutions import _CHALLENGE_TEMPLATES

with TestClient(app) as client:
    response = client.get('/api/health')
    result = {
        'status': response.status_code,
        'registry_loaded': CHALLENGE_REGISTRY.is_loaded,
        'templates_loaded': _CHALLENGE_TEMPLATES.is_loaded,
        'leetcode_module_loaded': 'challenges.algorithms.leetcode' in sys.modules,
    }
print(json.dumps(result))
"""
    env = {
        **os.environ,
        "CODEN_HOME": str(tmp_path / "user-data"),
        "PYTHONPATH": str(REPO_ROOT),
    }
    completed = subprocess.run(
        [sys.executable, "-c", script],
        cwd=REPO_ROOT,
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
        check=True,
    )
    result = json.loads(completed.stdout.strip().splitlines()[-1])

    assert result == {
        "status": 200,
        "registry_loaded": True,
        "templates_loaded": False,
        "leetcode_module_loaded": True,
    }
