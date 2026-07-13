"""FastAPI exception handlers.

The engine raises its own exception types (``OperationLimitExceeded``,
``ExecutionStepLimitExceeded``) and player code can raise anything.
Those are all caught in :mod:`server.app.engine_runner` and turned
into structured ``RunResponse`` objects with ``passed=false``, so
the FastAPI layer never sees them. This module is the catch-all
for things that slip through: uncaught server-side bugs, request
validation failures, and 404s.
"""
from __future__ import annotations

import logging

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


log = logging.getLogger(__name__)


def register(app: FastAPI) -> None:
    """Attach the exception handlers to the FastAPI app."""

    @app.exception_handler(RequestValidationError)
    async def _validation_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"error": "validation", "detail": exc.errors()},
        )

    @app.exception_handler(Exception)
    async def _unhandled(request: Request, exc: Exception):
        log.exception("Unhandled error on %s %s", request.method, request.url.path)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": "internal", "type": type(exc).__name__, "message": str(exc)},
        )
