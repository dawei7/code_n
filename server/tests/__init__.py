"""Server tests package.

The tests run with stdlib ``unittest`` (no pytest) for consistency
with the engine's 142-test suite, and they use
:class:`fastapi.testclient.TestClient` to hit the FastAPI app
in-process.
"""
