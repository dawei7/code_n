"""``GET /api/profiles``, ``POST /api/profiles``, and others.

Allows multiple user preparation profiles to switch between Free and Career Modes.
"""
from __future__ import annotations

from fastapi import APIRouter, HTTPException

from engine.progress import PlayerProgress
from server.app import progress_store
from server.app.schemas import (
    CreateProfileRequest,
    ProfileSummary,
    ProfilesResponse,
)

router = APIRouter()


@router.get("/profiles")
def list_profiles() -> ProfilesResponse:
    """List all profiles and report the active profile."""
    data = progress_store.load_profiles_data()
    active_profile = data.get("active_profile", "Default")
    profiles_dict = data.get("profiles", {})
    
    profiles_list = []
    for name, p_data in profiles_dict.items():
        p = PlayerProgress.from_dict(p_data)
        profiles_list.append(
            ProfileSummary(
                name=name,
                career_mode=p.career_mode,
                leetcode_username=p.leetcode_username,
                completed_count=len(p.completed),
                verified_leetcode_count=len(p.unlocked_leetcode),
            )
        )
        
    return ProfilesResponse(
        active_profile=active_profile,
        profiles=profiles_list
    )


@router.post("/profiles")
def create_profile(body: CreateProfileRequest) -> ProfilesResponse:
    """Create a new profile and switch to it immediately."""
    name = body.name.strip()
    if not name:
        raise HTTPException(status_code=400, detail="Profile name cannot be empty")
        
    data = progress_store.load_profiles_data()
    profiles_dict = data.setdefault("profiles", {})
    
    if name in profiles_dict:
        raise HTTPException(status_code=400, detail=f"Profile '{name}' already exists")
        
    # Create fresh progress
    p = PlayerProgress(player_name=name)
    p.career_mode = body.career_mode
    p.leetcode_username = body.leetcode_username
    
    profiles_dict[name] = p.to_dict()
    data["active_profile"] = name
    
    progress_store.save_profiles_data(data)
    return list_profiles()


@router.post("/profiles/{name}/select")
def select_profile(name: str) -> ProfilesResponse:
    """Switch active profile."""
    data = progress_store.load_profiles_data()
    profiles_dict = data.get("profiles", {})
    
    if name not in profiles_dict:
        raise HTTPException(status_code=404, detail=f"Profile '{name}' not found")
        
    data["active_profile"] = name
    progress_store.save_profiles_data(data)
    return list_profiles()


@router.delete("/profiles/{name}")
def delete_profile(name: str) -> ProfilesResponse:
    """Delete a profile. Active profile switches to default if deleted."""
    data = progress_store.load_profiles_data()
    profiles_dict = data.get("profiles", {})
    
    if name not in profiles_dict:
        raise HTTPException(status_code=404, detail=f"Profile '{name}' not found")
        
    if len(profiles_dict) <= 1:
        raise HTTPException(status_code=400, detail="Cannot delete the last remaining profile")
        
    del profiles_dict[name]
    
    # If we deleted the active profile, pick another one
    if data.get("active_profile") == name:
        data["active_profile"] = list(profiles_dict.keys())[0]
        
    progress_store.save_profiles_data(data)
    return list_profiles()
