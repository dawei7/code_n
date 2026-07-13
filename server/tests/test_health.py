"""``GET /api/health`` returns 200 with a small JSON body."""
from __future__ import annotations

from . import conftest  # noqa: F401  (sets up env vars + TestClient)


class HealthTest(conftest._Base):
    def test_health(self) -> None:
        r = self.client.get("/api/health")
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertEqual(body["status"], "ok")
        self.assertEqual(body["service"], "coden-server")
