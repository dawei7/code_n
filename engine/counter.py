"""Complexity class enum and per-class operation budget table.

The complexity-budget check is the load-bearing piece of the
"is the solution efficient enough?" gate. The engine has one
op-counting mechanism — the **AST-based** counter in
:mod:`server.app.ast_ops` — which walks the source and
multiplies by the enclosing-loop iteration count to produce
a single integer per ``(source, n)`` pair. This module
provides the budget table that integer is compared against.

The old runtime counter (``OperationCounter``, ``TrackedList``,
``TrackedGrid``) was removed in v0.8.5. Every operation in
this file is now purely a function of static source text and
``n`` — no global state, no runtime instrumentation, no proxies.
"""

from __future__ import annotations

import math
from enum import Enum
from typing import Optional


class ComplexityClass(Enum):
    O_1 = "O(1)"
    O_LOG_N = "O(log n)"
    O_N = "O(n)"
    O_N_LOG_N = "O(n log n)"
    O_N2 = "O(n²)"
    O_N3 = "O(n³)"
    O_2N = "O(2ⁿ)"
    O_N_FACTORIAL = "O(n!)"
    O_KN = "O(k^n)"
    UNKNOWN = "O(?)"


# Order from cheapest to most expensive. Used by
# :func:`classify_ast_ops` to pick the smallest class that
# still has budget for the user's op count.
_CLASSES_IN_ORDER: tuple[ComplexityClass, ...] = (
    ComplexityClass.O_1,
    ComplexityClass.O_LOG_N,
    ComplexityClass.O_N,
    ComplexityClass.O_N_LOG_N,
    ComplexityClass.O_N2,
    ComplexityClass.O_N3,
    ComplexityClass.O_2N,
    ComplexityClass.O_N_FACTORIAL,
    ComplexityClass.O_KN,
)


def get_complexity_factor(n: int, complexity_class: ComplexityClass) -> float:
    """Compute the base complexity factor for a given class at size n."""
    if complexity_class == ComplexityClass.O_1:
        return 1.0
    elif complexity_class == ComplexityClass.O_LOG_N:
        return math.log2(max(n, 2))
    elif complexity_class == ComplexityClass.O_N:
        return float(n)
    elif complexity_class == ComplexityClass.O_N_LOG_N:
        return n * math.log2(max(n, 2))
    elif complexity_class == ComplexityClass.O_N2:
        return float(n * n)
    elif complexity_class == ComplexityClass.O_N3:
        return float(n * n * n)
    elif complexity_class == ComplexityClass.O_2N:
        return float(2 ** min(n, 25))
    elif complexity_class == ComplexityClass.O_N_FACTORIAL:
        return float(math.factorial(min(n, 10)))
    elif complexity_class == ComplexityClass.O_KN:
        capped = min(n, 8)
        return float(capped**capped)
    return 1.0


def limit_for(n: int, max_class: ComplexityClass) -> int:
    """Return the operation budget for a required complexity class.

    The constant factors are tuned against the AST op counter
    (the sole op metric since v0.8.5). A clean O(n) algorithm
    with two passes and a per-element compare-then-update
    counts ~3 AST ops per element on the hot path (one
    compare + two subscripts for the read, one assign + four
    subscripts for the update), so 5x n comfortably fits any
    2-pass O(n) implementation. O(n log n) mergesorts and
    O(n²) bubble/selection/insertion sorts all fit in their
    respective budgets at small n. The constant ``+ 10`` covers
    the per-call overhead (for-loop bookkeeping, function
    call, etc.) that the AST counter attributes to the
    enclosing scope.
    """
    limits = {
        ComplexityClass.O_1: 10,
        ComplexityClass.O_LOG_N: int(math.log2(max(n, 2)) * 4) + 10,
        ComplexityClass.O_N: n * 5 + 10,
        ComplexityClass.O_N_LOG_N: int(n * math.log2(max(n, 2)) * 8) + 10,
        ComplexityClass.O_N2: n * n * 12 + 10,
        ComplexityClass.O_N3: n * n * n * 12 + 10,
        ComplexityClass.O_2N: 2 ** min(n, 25) + 10,
        ComplexityClass.O_N_FACTORIAL: math.factorial(min(n, 10)) + 10,
        ComplexityClass.O_KN: min(n, 8) ** min(n, 8) + 10,
    }
    return limits.get(max_class, 10**12)


def classify_ast_ops(
    ast_ops: int,
    n: int,
    reference_ast_ops: Optional[int] = None,
    required_complexity: Optional[ComplexityClass] = None,
) -> ComplexityClass:
    """Pick the smallest complexity class whose budget can hold
    ``ast_ops`` at input size ``n``.

    Semantic: "your code is as efficient as the smallest class
    that still has budget for your op count". A bubble sort
    with 680 AST ops at n=8 fits in O(n²) (8*8*8+10 = 522
    budget? no, 680 > 522) so it's classified as O(n³) — that
    matches the engine's intuition. A linear scan with 60
    AST ops at n=8 fits in O(n) (8*6+10 = 58) so it's O(n).

    Returns ``ComplexityClass.UNKNOWN`` if ``n <= 1`` (we
    don't classify at trivial sizes — there's no useful signal).
    """
    if n <= 1:
        return ComplexityClass.UNKNOWN
    if ast_ops <= 0:
        return ComplexityClass.O_1

    if reference_ast_ops is not None and required_complexity is not None and required_complexity != ComplexityClass.UNKNOWN:
        # If user's ast_ops are within the reference tolerance band, they match the reference complexity
        ci_low = int(math.floor(reference_ast_ops * 0.90))
        ci_high = int(math.ceil(reference_ast_ops * 1.05))
        if ci_low <= ast_ops <= ci_high:
            return required_complexity

        # Dynamic threshold based on reference solution coefficient
        factor = get_complexity_factor(n, required_complexity)
        C_ref = (reference_ast_ops - 10) / factor if factor > 0 else 0.0
        C_ref = max(0.1, C_ref)
        
        # If user's ast_ops is extremely low (e.g. <= 10), classify as O(1)
        if ast_ops <= 10:
            return ComplexityClass.O_1
            
        def limit_for_run(n: int, max_class: ComplexityClass, C_ref: float) -> int:
            factor = get_complexity_factor(n, max_class)
            return int(C_ref * factor) + 10

        for cls in _CLASSES_IN_ORDER:
            if cls == ComplexityClass.O_1:
                limit = 10
            else:
                limit = limit_for_run(n, cls, C_ref)
            if ast_ops <= limit:
                return cls
        return ComplexityClass.O_KN

    for cls in _CLASSES_IN_ORDER:
        if ast_ops <= limit_for(n, cls):
            return cls
    return ComplexityClass.O_KN
