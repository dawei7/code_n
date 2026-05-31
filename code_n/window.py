"""Shared Pygame window helpers."""

from __future__ import annotations

import ctypes
import os
from typing import Any


def open_maximized_window(pygame: Any, width: int, height: int, caption: str):
    """Create a resizable Pygame window and ask Windows to maximize it."""
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption(caption)
    _maximize_windows_window(pygame)
    pygame.event.pump()
    return pygame.display.get_surface() or screen


def is_resize_event(pygame: Any, event: Any) -> bool:
    resize_events = {pygame.VIDEORESIZE}
    for name in ("WINDOWRESIZED", "WINDOWSIZECHANGED", "WINDOWMAXIMIZED", "WINDOWRESTORED"):
        event_type = getattr(pygame, name, None)
        if event_type is not None:
            resize_events.add(event_type)
    return event.type in resize_events


def sync_window_size(owner: Any, screen: Any) -> None:
    owner.width, owner.height = screen.get_size()


def _maximize_windows_window(pygame: Any) -> None:
    if os.name != "nt":
        return
    try:
        hwnd = pygame.display.get_wm_info().get("window")
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 3)
    except Exception:
        pass
