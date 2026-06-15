"""Detect "too efficient" solutions: hardcoded answers + suspiciously
low op counts.

The player can sometimes produce the correct output without doing
the algorithmic work:

  * **Hardcoded return**: ``def solve(data, n): return [0, 1, 2, 3]``
  * **Accessing private state**: ``return challenge._data`` (which
    bypasses the algorithm)
  * **Skipped work**: returns the expected output from a memoized
    dict, returns a precomputed constant, etc.

This module flags those cases so the engine can mark the run as
not correct. Two complementary checks:

  1. **AST scan** of the player source for the specific patterns
     above. Targeted so legitimate code isn't tripped (e.g.
     ``return arr[i]`` is fine; ``return arr`` is fine; only
     ``return <literal>`` / ``return challenge._*`` are flagged).
  2. **Op-count ratio vs the reference solution**. If the player's
     run is correct but uses ``< 30%`` of the ops the canonical
     optimal solution uses, the player is probably skipping work
     (or the optimal solution is wasteful — in which case we'd
     still want the run flagged for review).

The check is intentionally conservative: false positives cost
players a frustrating "wait, that didn't pass?" moment, so we'd
rather under-flag than over-flag. The 30% threshold is a starting
point and easy to tune later.
"""
from __future__ import annotations

import ast
from dataclasses import dataclass
from enum import Enum
from typing import Optional


# Threshold for the op-count ratio check. 0.30 = "user did less
# than 30% of the reference's work". Tunable; lower = stricter
# (more false negatives), higher = looser (more false positives).
DEFAULT_RATIO_THRESHOLD = 0.30


class Reason(Enum):
    OK = "ok"
    HARDCODED = "hardcoded_return"     # `return <literal-list/dict/tuple/set>`
    PRIVATE_STATE = "private_state"    # `return challenge._<name>` or similar
    TOO_CHEAP = "too_cheap"            # op-count ratio below threshold


@dataclass
class CheckResult:
    """Outcome of :func:`check`. ``reason`` is ``Reason.OK`` when
    the source is clean. ``message`` is a short human-readable
    string for the UI; empty when ``reason`` is OK.
    """

    reason: Reason
    message: str = ""

    @property
    def flagged(self) -> bool:
        return self.reason is not Reason.OK


def check(
    user_source: str,
    user_ops: int,
    reference_ops: Optional[int] = None,
    ratio_threshold: float = DEFAULT_RATIO_THRESHOLD,
) -> CheckResult:
    """Run the AST scan + op-count ratio check.

    Parameters
    ----------
    user_source:
        The full Python source the player submitted. Parsed with
        :func:`ast.parse`; syntax errors are caught and treated as
        "clean" (the engine's own syntax-error path will already
        have caught the problem before we get here).
    user_ops:
        The number of operations the player's run consumed.
    reference_ops:
        The number of operations the reference solution consumed
        on the same (n, seed). Optional: when ``None``, the ratio
        check is skipped (only the AST scan runs).
    ratio_threshold:
        ``user_ops / reference_ops`` below this is flagged.

    Returns
    -------
    :class:`CheckResult`
    """
    # --- 1. AST scan -------------------------------------------------
    try:
        tree = ast.parse(user_source)
    except SyntaxError:
        # The engine surfaces a syntax error before this point;
        # nothing to do here.
        return CheckResult(Reason.OK)

    ast_result = _scan_ast(tree)
    if ast_result.flagged:
        return ast_result

    # --- 2. Op-count ratio -----------------------------------------
    if reference_ops is not None and reference_ops > 0 and user_ops > 0:
        ratio = user_ops / reference_ops
        if ratio < ratio_threshold:
            return CheckResult(
                Reason.TOO_CHEAP,
                message=(
                    f"Used {user_ops} ops vs the reference's {reference_ops} "
                    f"({ratio:.0%}). The solution may be skipping work or "
                    f"returning a precomputed answer. Re-run with care."
                ),
            )

    return CheckResult(Reason.OK)


# ---------------------------------------------------------------------------
# AST scanning helpers
# ---------------------------------------------------------------------------

# Names that, when accessed on a `challenge` instance, are private
# state set up by `setup_fn` and not part of the player's contract.
# Reading these is the canonical "cheat" (you have the answer in
# `challenge._data` etc).
_PRIVATE_STATE_ATTRS = {"_data", "_working_data", "_expected"}


def _scan_ast(tree: ast.AST) -> CheckResult:
    """Walk every function in the source and look for flagged returns."""

    class _Visitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.flag: Optional[CheckResult] = None

        def visit_Return(self, node: ast.Return) -> None:  # noqa: N802
            if self.flag is not None:
                return  # already flagged; keep walking for completeness
            value = node.value
            if value is None:
                return
            if _is_literal_container(value):
                self.flag = CheckResult(
                    Reason.HARDCODED,
                    message=(
                        "Solution returns a hardcoded literal "
                        f"({ast.unparse(value)!r}). Implement the algorithm."
                    ),
                )
                return
            if _is_private_state_access(value):
                self.flag = CheckResult(
                    Reason.PRIVATE_STATE,
                    message=(
                        "Solution reads the challenge's private state "
                        f"({ast.unparse(value)!r}). Use the function arguments."
                    ),
                )
                return
            # Keep visiting in case the return is nested in a tuple
            # like `return (foo, challenge._data)`.
            self.generic_visit(node)

    v = _Visitor()
    v.visit(tree)
    return v.flag or CheckResult(Reason.OK)


def _is_literal_container(node: ast.AST) -> bool:
    """True iff ``node`` is a list / tuple / set / dict literal.

    Note: we do NOT flag ``return [x for x in arr]`` or
    ``return list(data)`` — those do real work. Only a literal
    of constants is flagged.
    """
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        return all(_is_constant(el) for el in node.elts)
    if isinstance(node, ast.Dict):
        return all(
            _is_constant(k) and _is_constant(v)
            for k, v in zip(node.keys, node.values)
        )
    return False


def _is_constant(node: ast.AST) -> bool:
    """True iff ``node`` is a Python literal constant or a
    tuple of constants (the ``(a, b)`` form is a constant in
    Python's AST sense, represented as :class:`ast.Constant`)."""
    if isinstance(node, ast.Constant):
        return True
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        return _is_constant(node.operand)
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        return all(_is_constant(el) for el in node.elts)
    return False


def _is_private_state_access(node: ast.AST) -> bool:
    """True iff ``node`` is a ``challenge._<attr>`` or
    ``self._<attr>`` access, where ``_<attr>`` is in the
    known-private set."""
    if not isinstance(node, ast.Attribute):
        return False
    if node.attr not in _PRIVATE_STATE_ATTRS:
        return False
    # `challenge._data` → Attribute(value=Name(id='challenge'), attr='_data')
    if isinstance(node.value, ast.Name) and node.value.id in {"challenge", "self", "c"}:
        return True
    return False
