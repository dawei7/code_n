"""``GET /api/solutions/{id}`` and ``PUT /api/solutions/{id}`` — read/write the player's source.

The on-disk file is ``solutions/{id}.py`` in ``CODEN_HOME``. The
web editor saves here when the player hits ``Cmd/Ctrl+S``, and the
``POST /api/challenges/{id}/run`` endpoint reads from the editor
state (not the file), so this endpoint is the durable backup.
"""
from __future__ import annotations

import json
from pathlib import Path

from fastapi import APIRouter, HTTPException

from challenges.registry import CHALLENGE_REGISTRY
from server.app.config import SOLUTIONS_DIR
from server.app.schemas import SolutionGet, SolutionPut, SolutionVersionsGet, VersionSwitchRequest, VersionRenameRequest
from code_n.solutions import _solution_template

def _get_starter(challenge) -> str:
    spec = getattr(challenge, "_spec", None)
    if spec:
        return _solution_template(
            spec.id,
            heading=f"{spec.id}: {spec.name}",
            description=spec.description,
        )
    return ""


router = APIRouter()


def _solution_path(challenge_id: str) -> Path:
    SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)
    return SOLUTIONS_DIR / f"{challenge_id}.py"

def _version_path(challenge_id: str, version: int) -> Path:
    SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)
    return SOLUTIONS_DIR / f"{challenge_id}_v{version}.py"

def _versions_state_path() -> Path:
    SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)
    return SOLUTIONS_DIR / ".versions.json"

def _get_active_version(challenge_id: str) -> int:
    state_path = _versions_state_path()
    if state_path.exists():
        try:
            data = json.loads(state_path.read_text(encoding="utf-8"))
            val = data.get(challenge_id, 1)
            if isinstance(val, dict):
                return val.get("active", 1)
            return val
        except:
            return 1
    return 1

def _get_version_names(challenge_id: str) -> dict[int, str]:
    state_path = _versions_state_path()
    if state_path.exists():
        try:
            data = json.loads(state_path.read_text(encoding="utf-8"))
            val = data.get(challenge_id)
            if isinstance(val, dict):
                names = val.get("names", {})
                return {int(k): v for k, v in names.items()}
        except:
            pass
    return {}

def _set_active_version(challenge_id: str, version: int) -> None:
    state_path = _versions_state_path()
    data = {}
    if state_path.exists():
        try:
            data = json.loads(state_path.read_text(encoding="utf-8"))
        except:
            pass
    val = data.get(challenge_id)
    if isinstance(val, dict):
        val["active"] = version
    else:
        data[challenge_id] = {"active": version, "names": {}}
    state_path.write_text(json.dumps(data), encoding="utf-8")

def _set_version_name(challenge_id: str, version: int, name: str) -> None:
    state_path = _versions_state_path()
    data = {}
    if state_path.exists():
        try:
            data = json.loads(state_path.read_text(encoding="utf-8"))
        except:
            pass
    val = data.get(challenge_id)
    if not isinstance(val, dict):
        val = {"active": val if val else 1, "names": {}}
        data[challenge_id] = val
    val["names"][str(version)] = name
    state_path.write_text(json.dumps(data), encoding="utf-8")

def _get_existing_versions(challenge_id: str) -> list[int]:
    return list(range(1, 4))

def _clear_version_name(challenge_id: str, version: int) -> None:
    state_path = _versions_state_path()
    if state_path.exists():
        try:
            data = json.loads(state_path.read_text(encoding="utf-8"))
            if challenge_id in data and isinstance(data[challenge_id], dict) and "names" in data[challenge_id]:
                if str(version) in data[challenge_id]["names"]:
                    del data[challenge_id]["names"][str(version)]
                    state_path.write_text(json.dumps(data), encoding="utf-8")
        except:
            pass

def _get_modified_versions(challenge_id: str, starter: str) -> list[int]:
    modified = []
    active = _get_active_version(challenge_id)
    main_path = _solution_path(challenge_id)
    for i in range(1, 4):
        if i == active:
            if main_path.exists() and main_path.read_text(encoding="utf-8") != starter:
                modified.append(i)
        else:
            v_path = _version_path(challenge_id, i)
            if v_path.exists() and v_path.read_text(encoding="utf-8") != starter:
                modified.append(i)
    return modified


@router.get("/solutions/{challenge_id}")
def get_solution(challenge_id: str) -> SolutionVersionsGet:
    if challenge_id not in CHALLENGE_REGISTRY:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    
    active_version = _get_active_version(challenge_id)
    versions = _get_existing_versions(challenge_id)
    version_names = _get_version_names(challenge_id)
    
    challenge = CHALLENGE_REGISTRY[challenge_id]()
    starter = _get_starter(challenge)
    modified_versions = _get_modified_versions(challenge_id, starter)
    
    path = _solution_path(challenge_id)
    source = path.read_text(encoding="utf-8") if path.exists() else ""
    
    return SolutionVersionsGet(
        challenge_id=challenge_id,
        active_version=active_version,
        versions=versions,
        version_names=version_names,
        modified_versions=modified_versions,
        source=source
    )


@router.put("/solutions/{challenge_id}")
def put_solution(challenge_id: str, body: SolutionPut) -> SolutionGet:
    if challenge_id not in CHALLENGE_REGISTRY:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    path = _solution_path(challenge_id)
    path.write_text(body.source, encoding="utf-8")
    
    # Sync to version backup
    active_version = _get_active_version(challenge_id)
    _version_path(challenge_id, active_version).write_text(body.source, encoding="utf-8")
    
    return SolutionGet(challenge_id=challenge_id, source=body.source, exists=True)


@router.post("/solutions/{challenge_id}/versions/switch")
def switch_version(challenge_id: str, body: VersionSwitchRequest) -> SolutionVersionsGet:
    if challenge_id not in CHALLENGE_REGISTRY:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    if body.version < 1 or body.version > 3:
        raise HTTPException(status_code=400, detail="Version must be between 1 and 3")
        
    current_active = _get_active_version(challenge_id)
    main_path = _solution_path(challenge_id)
    
    # Save current state to its version backup if it exists
    if main_path.exists():
        _version_path(challenge_id, current_active).write_text(main_path.read_text(encoding="utf-8"), encoding="utf-8")
        
    # Update state to new version
    _set_active_version(challenge_id, body.version)
    
    # Load new version into main path (or template if missing)
    target_path = _version_path(challenge_id, body.version)
    if target_path.exists():
        main_path.write_text(target_path.read_text(encoding="utf-8"), encoding="utf-8")
    else:
        # Load template
        challenge = CHALLENGE_REGISTRY[challenge_id]()
        main_path.write_text(_get_starter(challenge), encoding="utf-8")
        
    return get_solution(challenge_id)


@router.put("/solutions/{challenge_id}/versions/{version}/rename")
def rename_version(challenge_id: str, version: int, body: VersionRenameRequest) -> SolutionVersionsGet:
    if challenge_id not in CHALLENGE_REGISTRY:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    _set_version_name(challenge_id, version, body.name)
    return get_solution(challenge_id)


@router.post("/solutions/{challenge_id}/versions/{version}/reset")
def reset_version(challenge_id: str, version: int) -> SolutionVersionsGet:
    if challenge_id not in CHALLENGE_REGISTRY:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
        
    challenge = CHALLENGE_REGISTRY[challenge_id]()
    starter = _get_starter(challenge)
    
    target_path = _version_path(challenge_id, version)
    target_path.write_text(starter, encoding="utf-8")
    
    active_version = _get_active_version(challenge_id)
    if active_version == version:
        main_path = _solution_path(challenge_id)
        main_path.write_text(starter, encoding="utf-8")
        
    _clear_version_name(challenge_id, version)
        
    return get_solution(challenge_id)
