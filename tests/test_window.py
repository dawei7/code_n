"""Tests for the cross-platform mono font helper.

Pygame is not initialized for the unit tests; we mock the small surface
that the helper needs. The helper is intentionally pure-Python (no
display) so it can be tested without a real window.
"""
from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from code_n.window import find_mono_font_name, mono_font


class FakePygameFont:
    def __init__(self, installed=("consolas",)):
        # The helper looks up pygame.font.get_fonts() and pygame.font.SysFont,
        # so we model the "font" submodule with a single object.
        self.font = MagicMock()
        self.font.get_fonts = MagicMock(return_value=list(installed))
        self.font.SysFont = MagicMock(side_effect=self._sys_font)

    def _sys_font(self, name, size, bold=False):
        return ("FONT", name, size, bold)


class FindMonoFontTests(unittest.TestCase):
    def test_returns_first_available(self):
        # The candidate list prefers consolas (Windows) over dejavusansmono
        # (Linux); whichever appears first in CANDIDATES wins.
        pygame = FakePygameFont(installed=("dejavusansmono", "consolas"))
        self.assertEqual(find_mono_font_name(pygame), "consolas")

    def test_returns_none_when_nothing_matches(self):
        pygame = FakePygameFont(installed=("arial", "helvetica"))
        self.assertIsNone(find_mono_font_name(pygame))

    def test_returns_consolas_on_windows(self):
        pygame = FakePygameFont(installed=("consolas", "arial"))
        self.assertEqual(find_mono_font_name(pygame), "consolas")


class MonoFontTests(unittest.TestCase):
    def test_returns_sysfont_with_size_and_bold(self):
        pygame = FakePygameFont(installed=("consolas",))
        font = mono_font(pygame, 18, bold=True)
        self.assertEqual(font, ("FONT", "consolas", 18, True))

    def test_falls_back_to_monospace_keyword(self):
        pygame = FakePygameFont(installed=())
        font = mono_font(pygame, 12)
        # When nothing is found we hand Pygame the keyword "monospace" so it
        # can do its own fallback chain.
        self.assertEqual(font, ("FONT", "monospace", 12, False))


if __name__ == "__main__":
    unittest.main()
