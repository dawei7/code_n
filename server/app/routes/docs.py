"""``GET /api/docs/*`` - the in-app algorithm reference.

Three endpoints:

* ``GET /api/docs/overview``   - returns the raw text of
  ``docs/README.md`` (the general overview + interview path).
* ``GET /api/docs/index``      - returns a JSON list of all
  263 challenges, with a ``has_doc`` flag for whether a
  per-algorithm doc exists yet.
* ``GET /api/docs/{path:path}`` - returns the raw text of a
  single per-algorithm markdown file. Path-traversal safe.

The docs are static markdown files in ``DOCS_ROOT`` (see
``server.app.config``). In dev, ``DOCS_ROOT = <repo>/docs``;
in the packaged Electron app it's ``resources/docs/``.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from challenges.registry import CHALLENGE_REGISTRY
from rate_algos import rate
from server.app.config import DOCS_ROOT


router = APIRouter()


# --- Index entry -------------------------------------------------

class DocIndexEntry(BaseModel):
    id: str
    name: str
    category: str
    difficulty_existing: int
    difficulty_mine: int
    relevance_mine: int
    path: Optional[str]  # relative to DOCS_ROOT/algorithms/, or null if no doc
    has_doc: bool


# --- Helpers -----------------------------------------------------

def _slugify(name: str) -> str:
    """Match the filename convention used in docs/algorithms/*/.

    Examples: ``"Coin Change"`` -> ``"coin-change"``,
    ``"LCS"`` -> ``"lcs"``, ``"0/1 Knapsack"`` -> ``"01-knapsack"``.
    """
    s = name.lower()
    # Replace common separators with hyphens.
    for ch in " /(),:":
        s = s.replace(ch, "-")
    # Drop apostrophes (so "Levenshtein" doesn't have a stray `'`).
    s = s.replace("'", "")
    # Collapse multiple hyphens and strip leading/trailing.
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-").strip(".")


def _category_dir(category: str) -> Path:
    """Map a category name to a docs/algorithms/{dir}/ path.

    The category names in the registry match the dir names 1:1
    (both are lowercase with underscores). This helper is here
    for the day they diverge - just edit the dict.
    """
    return DOCS_ROOT / "algorithms" / category


def _find_doc_path(challenge_id: str, name: str, category: str) -> Optional[Path]:
    """Return the absolute path of the doc, or None if it doesn't exist.

    The filename convention is ``{challenge_id}_{slug}.md`` where
    slug is the lowercased, hyphenated name.
    """
    cat_dir = _category_dir(category)
    if not cat_dir.is_dir():
        return None
    candidate = cat_dir / f"{challenge_id}_{_slugify(name)}.md"
    return candidate if candidate.is_file() else None


# --- Endpoints ---------------------------------------------------

@router.get("/docs/index")
def docs_index() -> list[DocIndexEntry]:
    """List all challenges with their ratings and a has_doc flag."""
    out: list[DocIndexEntry] = []
    for cid, cls in sorted(CHALLENGE_REGISTRY.items()):
        spec = cls()._spec
        my_d, my_r = rate(spec.name, spec.category, spec.required_complexity.value)
        doc = _find_doc_path(cid, spec.name, spec.category)
        rel = None
        if doc is not None:
            try:
                rel = str(doc.relative_to(DOCS_ROOT)).replace("\\", "/")
            except ValueError:
                rel = None
        out.append(
            DocIndexEntry(
                id=cid,
                name=spec.name,
                category=spec.category,
                difficulty_existing=spec.difficulty,
                difficulty_mine=my_d,
                relevance_mine=my_r,
                path=rel,
                has_doc=doc is not None,
            )
        )
    return out


@router.get("/docs/overview")
def docs_overview() -> str:
    """Return the general overview doc (docs/README.md).

    Returns plain text; the frontend renders it with the same
    markdown engine it uses for per-algorithm docs.
    """
    readme = DOCS_ROOT / "README.md"
    if not readme.is_file():
        raise HTTPException(status_code=404, detail="docs/README.md not found")
    return readme.read_text(encoding="utf-8")


@router.get("/docs/by-id/{challenge_id}")
def docs_by_id(challenge_id: str) -> str:
    """Return the per-algorithm doc for a challenge (by challenge id)."""
    cls = CHALLENGE_REGISTRY.get(challenge_id)
    if cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    spec = cls()._spec
    doc = _find_doc_path(challenge_id, spec.name, spec.category)
    if doc is None:
        raise HTTPException(
            status_code=404,
            detail=f"No doc yet for {challenge_id} ({spec.name}). "
                   f"Contribute at docs/algorithms/{spec.category}/{challenge_id}_*.md",
        )
    return doc.read_text(encoding="utf-8")


@router.get("/docs/{path:path}")
def docs_raw(path: str) -> str:
    """Return the raw text of any file under DOCS_ROOT.

    Path-traversal safe: the resolved absolute path must remain
    inside DOCS_ROOT. The 403 is intentional - we don't want
    ``/api/docs/../server/app/main.py`` to leak the engine source.
    """
    if not DOCS_ROOT.is_dir():
        raise HTTPException(status_code=500, detail="DOCS_ROOT does not exist")
    target = (DOCS_ROOT / path).resolve()
    try:
        target.relative_to(DOCS_ROOT.resolve())
    except ValueError:
        raise HTTPException(status_code=403, detail="Path traversal denied")
    if not target.is_file():
        raise HTTPException(status_code=404, detail=f"Doc not found: {path}")
    return target.read_text(encoding="utf-8")
