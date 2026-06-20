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
from fastapi.responses import Response
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


def _find_doc_path(challenge_id: str, name: str, category: str, lang: str = "en") -> Optional[Path]:
    """Return the absolute path of the doc, or None if it doesn't exist.

    Uses a prefix search on the challenge ID to resolve mismatches between
    registry names and disk filenames (e.g. 'graph_02_bfs.md' vs 'graph_02_breadth-first-search.md').
    """
    cat_dir = _category_dir(category)
    if not cat_dir.is_dir():
        return None
    
    # Try finding files starting with challenge_id
    files = list(cat_dir.glob(f"{challenge_id}_*.md"))
    if not files:
        return None
        
    if lang == "de":
        de_files = [f for f in files if f.name.endswith("_de.md")]
        if de_files:
            return de_files[0]
            
    en_files = [f for f in files if not f.name.endswith("_de.md")]
    return en_files[0] if en_files else None


def _find_math_path(challenge_id: str, name: str, category: str, lang: str = "en") -> Optional[Path]:
    """Return the absolute path of the math doc, or None if it doesn't exist.
    
    Uses a prefix search on the challenge ID to resolve mismatches.
    """
    cat_dir = DOCS_ROOT / "mathematical" / category
    if not cat_dir.is_dir():
        return None
        
    files = list(cat_dir.glob(f"{challenge_id}_*.md"))
    if not files:
        return None
        
    if lang == "de":
        de_files = [f for f in files if f.name.endswith("_de.md")]
        if de_files:
            return de_files[0]
            
    en_files = [f for f in files if not f.name.endswith("_de.md")]
    return en_files[0] if en_files else None

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
def docs_overview(lang: str = "en") -> Response:
    """Return the general overview doc (docs/README.md).

    Returns the file content with ``text/markdown`` so the
    client receives the raw markdown (no JSON wrapping or
    string escaping). FastAPI's default is to JSON-encode
    ``str`` returns, which would wrap the whole doc in
    quotes and escape newlines as ``\\n`` - not what we want
    for a markdown consumer.
    """
    readme_de = DOCS_ROOT / "README_de.md"
    readme_en = DOCS_ROOT / "README.md"
    readme = readme_de if lang == "de" and readme_de.is_file() else readme_en
    if not readme.is_file():
        raise HTTPException(status_code=404, detail="docs/README.md not found")
    return Response(
        content=readme.read_text(encoding="utf-8"),
        media_type="text/markdown; charset=utf-8",
    )


@router.get("/docs/by-id/{challenge_id}")
def docs_by_id(challenge_id: str, lang: str = "en") -> Response:
    """Return the per-algorithm doc for a challenge (by challenge id).

    See :func:`docs_overview` for the media-type note.
    """
    cls = CHALLENGE_REGISTRY.get(challenge_id)
    if cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    spec = cls()._spec
    doc = _find_doc_path(challenge_id, spec.name, spec.category, lang)
    if doc is None:
        raise HTTPException(
            status_code=404,
            detail=f"No doc yet for {challenge_id} ({spec.name}). "
                   f"Contribute at docs/algorithms/{spec.category}/{challenge_id}_*.md",
        )
    return Response(
        content=doc.read_text(encoding="utf-8"),
        media_type="text/markdown; charset=utf-8",
    )


@router.get("/math/by-id/{challenge_id}")
def math_by_id(challenge_id: str, lang: str = "en") -> Response:
    """Return the per-algorithm mathematical doc for a challenge (by challenge id)."""
    cls = CHALLENGE_REGISTRY.get(challenge_id)
    if cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    spec = cls()._spec
    doc = _find_math_path(challenge_id, spec.name, spec.category, lang)
    if doc is None:
        raise HTTPException(
            status_code=404,
            detail=f"No mathematical doc yet for {challenge_id} ({spec.name}). "
                   f"Contribute at docs/mathematical/{spec.category}/{challenge_id}_*.md",
        )
    return Response(
        content=doc.read_text(encoding="utf-8"),
        media_type="text/markdown; charset=utf-8",
    )


@router.get("/docs/{path:path}")
def docs_raw(path: str) -> Response:
    """Return the raw text of any file under DOCS_ROOT.

    Path-traversal safe: the resolved absolute path must remain
    inside DOCS_ROOT. The 403 is intentional - we don't want
    ``/api/docs/../server/app/main.py`` to leak the engine source.

    Sends the file with ``text/markdown`` so the client receives
    raw markdown (not JSON-wrapped).
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
    return Response(
        content=target.read_text(encoding="utf-8"),
        media_type="text/markdown; charset=utf-8",
    )
