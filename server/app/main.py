"""FastAPI application factory.

Wires together:

* the CORS middleware (Vite dev origin, Electron scheme)
* the route modules under the ``/api`` prefix
* the exception handlers
* the on-startup registry warm (so the first /api/challenges
  request doesn't pay the import cost of the spec framework)

The factory pattern keeps ``uvicorn server.app.main:app`` working
in dev, and lets the Electron launcher's tests import the app
without binding to a port.
"""
from __future__ import annotations

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.app.config import CORS_ORIGINS, ensure_data_dirs
from server.app.routes import challenges, health, progress, run, solutions
from server.app import error_handlers


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)


def create_app() -> FastAPI:
    app = FastAPI(
        title="cOde(n) server",
        version="0.1.0",
        description="HTTP API wrapping the cOde(n) Python engine.",
    )

    # CORS — dev: Vite on 5173, prod: Electron's app:// scheme.
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routes
    app.include_router(health.router, prefix="/api")
    app.include_router(challenges.router, prefix="/api")
    app.include_router(run.router, prefix="/api")
    app.include_router(progress.router, prefix="/api")
    app.include_router(solutions.router, prefix="/api")

    # Exception handlers
    error_handlers.register(app)

    # Warm the registry at startup so the first request is fast.
    @app.on_event("startup")
    def _startup() -> None:
        ensure_data_dirs()
        # Import the registry so the spec framework runs at startup,
        # not at first request.
        from challenges.registry import CHALLENGE_REGISTRY
        logging.info("Loaded %d challenges", len(CHALLENGE_REGISTRY))

    return app


# Module-level instance for `uvicorn server.app.main:app`.
app = create_app()
