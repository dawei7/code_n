"""Canonical LeetCode documentation endpoints.

The repository has no parallel algorithm-doc tree. Product overview content is
the root README, and every problem owns its reference at
``dsa/leetcode/<frontend_id:04d>_<slug>/doc.md``.
"""
from __future__ import annotations

import mimetypes
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, Response
from pydantic import BaseModel

from challenges.registry import CHALLENGE_REGISTRY
from server.app.challenge_packages import (
    is_leetcode_id,
    leetcode_doc_path,
    leetcode_package_dir,
)
from server.app.config import DSA_ROOT, LEETCODE_ROOT, OVERVIEW_DOC


router = APIRouter()


class DocIndexEntry(BaseModel):
    id: str
    name: str
    category: str
    difficulty_label: str
    elo_rating: float | None
    difficulty_estimate: int | None
    relevance_mine: int
    path: str | None
    has_doc: bool


def _find_doc_path(challenge_id: str, lang: str = "en") -> Path | None:
    if not is_leetcode_id(challenge_id):
        return None
    return leetcode_doc_path(challenge_id, lang)


@router.get("/docs/index")
def docs_index() -> list[DocIndexEntry]:
    """List registry challenges and their canonical package-doc status."""
    entries: list[DocIndexEntry] = []
    for challenge_id, challenge_cls in sorted(CHALLENGE_REGISTRY.items()):
        spec = challenge_cls()._spec
        doc = _find_doc_path(challenge_id)
        relative = None
        if doc is not None:
            try:
                relative = "dsa/leetcode/" + str(
                    doc.relative_to(LEETCODE_ROOT)
                ).replace("\\", "/")
            except ValueError:
                relative = None
        entries.append(
            DocIndexEntry(
                id=challenge_id,
                name=spec.name,
                category=spec.category,
                difficulty_label=spec.difficulty_label,
                elo_rating=spec.elo_rating,
                difficulty_estimate=spec.difficulty_estimate,
                relevance_mine=5,
                path=relative,
                has_doc=doc is not None,
            )
        )
    return entries


@router.get("/docs/overview")
def docs_overview(lang: str = "en") -> Response:
    """Return the product overview from the repository README."""
    del lang  # The overview currently has one maintained language.
    if not OVERVIEW_DOC.is_file():
        raise HTTPException(status_code=404, detail="README.md not found")
    return Response(
        content=OVERVIEW_DOC.read_text(encoding="utf-8"),
        media_type="text/markdown; charset=utf-8",
    )


@router.get("/docs/by-id/{challenge_id}")
def docs_by_id(challenge_id: str, lang: str = "en") -> Response:
    """Return one challenge's canonical package document."""
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    doc = _find_doc_path(challenge_id, lang)
    if doc is None:
        package_dir = leetcode_package_dir(challenge_id)
        package_name = (
            package_dir.name
            if package_dir is not None
            else "<frontend_id:04d>_<slug>"
        )
        package_hint = f"dsa/leetcode/{package_name}/doc.md"
        raise HTTPException(
            status_code=404,
            detail=f"No canonical doc for {challenge_id}. Contribute at {package_hint}",
        )
    return Response(
        content=doc.read_text(encoding="utf-8"),
        media_type="text/markdown; charset=utf-8",
    )


@router.get("/docs/by-id/{challenge_id}/assets/{asset_path:path}")
def leetcode_doc_asset(challenge_id: str, asset_path: str) -> FileResponse:
    """Return an asset contained by a canonical challenge package."""
    if not is_leetcode_id(challenge_id):
        raise HTTPException(status_code=404, detail="Only LeetCode package assets are supported")
    package_dir = leetcode_package_dir(challenge_id)
    if package_dir is None:
        raise HTTPException(status_code=404, detail=f"Unknown LeetCode challenge: {challenge_id}")
    assets_root = (package_dir / "assets").resolve()
    target = (assets_root / asset_path).resolve()
    try:
        target.relative_to(assets_root)
    except ValueError as exc:
        raise HTTPException(status_code=403, detail="Path traversal denied") from exc
    if not target.is_file():
        raise HTTPException(status_code=404, detail=f"Asset not found: {asset_path}")
    media_type, _encoding = mimetypes.guess_type(str(target))
    return FileResponse(target, media_type=media_type or "application/octet-stream")


@router.get("/docs/{path:path}")
def docs_raw(path: str) -> Response:
    """Return a raw markdown file below the canonical DSA root only."""
    if path != "dsa" and not path.startswith("dsa/"):
        raise HTTPException(
            status_code=404,
            detail="Only canonical dsa documentation paths are available",
        )
    relative = path.removeprefix("dsa").lstrip("/\\")
    target = (DSA_ROOT / relative).resolve()
    try:
        target.relative_to(DSA_ROOT.resolve())
    except ValueError as exc:
        raise HTTPException(status_code=403, detail="Path traversal denied") from exc
    if not target.is_file():
        raise HTTPException(status_code=404, detail=f"Doc not found: {path}")
    return Response(
        content=target.read_text(encoding="utf-8"),
        media_type="text/markdown; charset=utf-8",
    )
