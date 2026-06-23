"""Server route modules.

Each module owns one HTTP resource:

* ``health.py``      — ``GET /api/health``
* ``challenges.py``  — ``GET /api/challenges`` and ``GET /api/challenges/{id}``
* ``run.py``         — ``POST /api/challenges/{id}/run``
* ``debug.py``       — ``WebSocket /api/debug/ws`` for in-app debug sessions
* ``progress.py``    — ``GET /api/progress`` and ``PUT /api/progress``
* ``solutions.py``   — ``GET /api/solutions/{id}`` and ``PUT /api/solutions/{id}``

``main.py`` imports and mounts them with the ``/api`` prefix.
"""
