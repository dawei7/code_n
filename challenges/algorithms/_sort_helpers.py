"""Shared helpers for the sorting-algorithm challenges.

Centralises the ``is_sorted_result`` check so every sort
challenge uses identical acceptance semantics: the player may
either mutate the input in place (``return None``) or return a
new sorted sequence. Both are accepted.
"""

from __future__ import annotations

from typing import Any


def is_sorted_result(result: Any, expected_data: list) -> bool:
    """Return True iff ``result`` is a sorted version of
    ``expected_data``.

    Two valid player contracts:

    * **Return the sorted list** — ``result`` is a list (or tuple)
      that compares element-wise to ``sorted(expected_data)``.
    * **Mutate in place** — ``result is None``; the player mutated
      ``expected_data`` (which IS the player's list reference,
      passed straight from the engine's setup). The caller passes
      ``expected_data`` itself, so reading it now shows the
      post-mutation state.

    The ``working_data`` parameter (and the ``TrackedList`` /
    ``unwrap_tracked`` machinery behind it) was removed in
    v0.8.5: the setup function passes the raw list reference
    directly, so ``expected_data`` is both the canonical
    pre-run storage and the player's input — the same object.
    """
    expected = sorted(expected_data)
    if result is None:
        return expected_data == expected
    if isinstance(result, (list, tuple)):
        return list(result) == expected
    return False
