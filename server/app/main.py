"""FastAPI application factory.

Wires together:

* the CORS middleware (Vite dev origin, Electron scheme)
* the route modules under the ``/api`` prefix
* the exception handlers
* the on-startup registry warm (so the first /api/challenges
  request doesn't pay the import cost of the spec framework)
* the ``web/dist/`` static mount (for the Electron desktop wrapper,
  so the FastAPI server can serve the built React app at ``/``)

The factory pattern keeps ``uvicorn server.app.main:app`` working
in dev, and lets the Electron launcher's tests import the app
without binding to a port.
"""
from __future__ import annotations

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from server.app.config import CORS_ORIGINS, WEB_DIST, ensure_data_dirs
from server.app.routes import challenges, debug, docs, health, practice_export, progress, run, solutions, profiles
from server.app import error_handlers


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)


# Path to the built React app. Mounted at "/" if it exists; absent
# in Vite-only dev (the user runs `npm run dev` separately and the
# Vite proxy handles /api/* forwarding).
# The actual path comes from server.app.config.WEB_DIST, which reads
# the CODEN_WEB_DIST env var (set by the Electron launcher to the
# extraResource path) or falls back to <PROJECT_ROOT>/web/dist.


def warm_registry() -> None:
    """Prepare writable data dirs and load the challenge registry."""
    ensure_data_dirs()
    from challenges.registry import CHALLENGE_REGISTRY

    logging.info("Loaded %d challenges", len(CHALLENGE_REGISTRY))


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    warm_registry()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="cOde(n) server",
        version="0.1.0",
        description="HTTP API wrapping the cOde(n) Python engine.",
        lifespan=lifespan,
    )

    # CORS — dev: Vite on 5173, prod: Electron's app:// scheme.
    # Same-origin requests (Electron loading from this same server)
    # don't trigger CORS, so we don't need to list 127.0.0.1:*.
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routes — registered before the static catch-all so /api/*
    # always wins the match.
    app.include_router(health.router, prefix="/api")
    app.include_router(challenges.router, prefix="/api")
    app.include_router(docs.router, prefix="/api")
    app.include_router(run.router, prefix="/api")
    app.include_router(debug.router, prefix="/api")
    app.include_router(practice_export.router, prefix="/api")
    app.include_router(progress.router, prefix="/api")
    app.include_router(solutions.router, prefix="/api")
    app.include_router(profiles.router, prefix="/api")

    # Exception handlers
    error_handlers.register(app)

    # Static UI mount — only if the React build is present.
    # In the Vite-only dev workflow this is absent and the user
    # runs `npm run dev` separately.
    if WEB_DIST.is_dir() and (WEB_DIST / "index.html").is_file():
        app.mount("/", StaticFiles(directory=str(WEB_DIST), html=True), name="ui")
        logging.info("Mounted web UI from %s", WEB_DIST)
    else:
        logging.info(
            "web/dist not found at %s; UI served separately (run `npm run build` in web/ for Electron, or `npm run dev` for Vite HMR)",
            WEB_DIST,
        )

    return app


# Module-level instance for `uvicorn server.app.main:app`.
app = create_app()
