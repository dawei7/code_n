"""Shared Pygame window helpers."""

from __future__ import annotations

import ctypes
import os
from typing import Any, Optional


# Cross-platform monospace font fallback list. Pygame silently substitutes
# when a font name is missing, so we want to try several candidates before
# falling back to Pygame's default.
_MONO_FONT_CANDIDATES = (
    "consolas",         # Windows
    "menlo",            # macOS
    "monaco",           # macOS (older)
    "dejavusansmono",   # Linux
    "liberationmono",   # Linux
    "ubuntumono",       # Linux
    "couriernew",       # Windows / fallback
    "courier",          # POSIX fallback
)


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


def find_mono_font_name(pygame: Any) -> Optional[str]:
    """Return the first installed monospace font from a cross-platform list,
    or None if Pygame's default should be used.

    Pygame's SysFont accepts a comma-separated name list and tries each in
    order, so we hand the full list back to it when nothing matches by
    name. That gives the best chance of finding something monospace on
    whatever the player is running.
    """
    available = {name.lower() for name in pygame.font.get_fonts()}
    # Pygame.font.get_fonts() returns basenames without spaces; also try
    # the SysFont-name form in case the user has a fuller font registry.
    for candidate in _MONO_FONT_CANDIDATES:
        if candidate in available:
            return candidate
    return None


def mono_font(pygame: Any, size: int, bold: bool = False):
    """Return a Pygame font that is monospace on the current platform.

    Pass the result to the rest of the UI as a normal `pygame.font.Font`.
    """
    name = find_mono_font_name(pygame) or "monospace"
    return pygame.font.SysFont(name, size, bold=bold)


def _maximize_windows_window(pygame: Any) -> None:
    if os.name != "nt":
        return
    try:
        hwnd = pygame.display.get_wm_info().get("window")
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 3)
    except Exception:
        pass
