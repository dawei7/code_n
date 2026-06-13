"""Stack algorithms.

Three classic problems from GFG's stack-data-structures catalog:

  01 Balanced Parentheses     - validate ()[]{} nesting
  02 Next Greater Element    - for each index, the next larger value to the right
  03 Stock Span Problem      - for each day, the number of consecutive
    days before it with a lower (or equal) price

All three use a Python list as the underlying stack. Setup
is deterministic and keeps n small (4-16) so brute-force
verify is fast.
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === stack_01: Balanced Parentheses ===

STACK_01_SOURCE = '''\
"""Optimal solution for stack_01: Balanced Parentheses.

Walk the string; push each opening bracket, and on a closing
bracket pop the top and check that it pairs correctly. Return
True iff the stack is empty at the end. O(n).
"""


def solve(s, n):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack
'''


def _setup_balanced_parens(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    # Build a random valid-or-invalid string.
    valid_count = rng.randint(1, max(1, n // 2))
    # Generate `valid_count` matching pairs.
    openers = "([{"
    closers = ")]}"
    pairs = []
    for _ in range(valid_count):
        idx = rng.randint(0, 2)
        pairs.append((openers[idx], closers[idx]))
    rng.shuffle(pairs)
    # Nest them so the result is well-formed.
    s = ""
    opens = []
    for o, c in pairs:
        s += o
        opens.append(c)
    rng.shuffle(opens)
    s += "".join(opens)
    # Optionally add a stray closer to break the validity.
    if rng.random() < 0.5 and len(s) > 1:
        s += rng.choice(closers)
    challenge._s = s
    return {"s": s, "n": len(s)}


def _verify_balanced_parens(challenge, result: Any) -> bool:
    if not isinstance(result, bool):
        return False
    s = challenge._s
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return result is False
            stack.pop()
    return result is (not stack)


# === stack_02: Next Greater Element ===

STACK_02_SOURCE = '''\
"""Optimal solution for stack_02: Next Greater Element.

Monotonic stack: walk left to right, maintaining a stack of
indices whose next-greater hasn't been found yet. When arr[i]
is greater than the top, pop and record i as the answer for
the popped index. O(n).
"""


def solve(arr, n):
    result = [-1] * n
    stack = []  # indices
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    return result
'''


def _setup_next_greater(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    arr = [rng.randint(0, 99) for _ in range(n)]
    challenge._arr = list(arr)
    return {"arr": list(arr), "n": n}


def _verify_next_greater(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    arr = challenge._arr
    # Brute-force: for each i, find the first j > i with arr[j] > arr[i].
    expected = []
    for i in range(len(arr)):
        nxt = -1
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                nxt = arr[j]
                break
        expected.append(nxt)
    return result == expected


# === stack_03: Stock Span Problem ===

STACK_03_SOURCE = '''\
"""Optimal solution for stack_03: Stock Span Problem.

For each day i, the span is the number of consecutive days
just before i with a price <= arr[i] (plus today). Monotonic
stack: walk left to right, popping while the top's price is
<= today's. The span is i - (top index after popping), or
i + 1 if the stack is empty. O(n).
"""


def solve(arr, n):
    spans = [0] * n
    stack = []  # indices
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            spans[i] = i - stack[-1]
        else:
            spans[i] = i + 1
        stack.append(i)
    return spans
'''


def _setup_stock_span(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    arr = [rng.randint(1, 99) for _ in range(n)]
    challenge._arr = list(arr)
    return {"arr": list(arr), "n": n}


def _verify_stock_span(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    arr = challenge._arr
    # Brute-force: for each i, count j <= i with arr[j] <= arr[i] consecutively.
    expected = []
    for i in range(len(arr)):
        span = 1
        j = i - 1
        while j >= 0 and arr[j] <= arr[i]:
            span += 1
            j -= 1
        expected.append(span)
    return result == expected


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="stack_01",
        name="Balanced Parentheses",
        category="stack",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return True iff the input string of ()[]{} characters is\n"
            "well-balanced. Push each opener; on a closer, pop and check\n"
            "the pair. The string is balanced iff the stack ends empty.\n"
            "Source: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/"
        ),
        source_url="https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/",
        params=["s", "n"],
        inputs={
            "s": "string of n characters in ()[]{}.",
            "n": "length of s.",
        },
        returns="True iff s is well-balanced.",
        source=STACK_01_SOURCE,
        setup_fn=_setup_balanced_parens,
        verify_fn=_verify_balanced_parens,
        samples=[
            Sample('s = "{([])}", n = 6', "True"),
            Sample('s = "([)]", n = 4', "False"),
            Sample('s = "((()))", n = 6', "True"),
        ],
        hint="On an opener, push. On a closer, pop and check the pair.",
        parents=["recursion_04"],
        children=["stack_02"],
    ),
    AlgorithmSpec(
        id="stack_02",
        name="Next Greater Element",
        category="stack",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "For each index i, return the next value to the right that's\n"
            "strictly greater than arr[i], or -1 if none. Monotonic stack\n"
            "of indices: pop while arr[i] > arr[top], record arr[i] as the\n"
            "answer for the popped index.\n"
            "Requirement: O(n) time.\n"
            "Source: https://www.geeksforgeeks.org/next-greater-element/"
        ),
        source_url="https://www.geeksforgeeks.org/next-greater-element/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n random integers.",
            "n": "length of arr.",
        },
        returns="a list of n values (each the next greater to the right, or -1).",
        source=STACK_02_SOURCE,
        setup_fn=_setup_next_greater,
        verify_fn=_verify_next_greater,
        samples=[
            Sample("arr = [4, 5, 2, 25], n = 4", "[5, 25, 25, -1]"),
            Sample("arr = [13, 7, 6, 12], n = 4", "[-1, 12, 12, -1]"),
        ],
        hint="Monotonic stack of indices. Pop when arr[i] > arr[top] and record the answer.",
        parents=["stack_01"],
        children=["stack_03"],
    ),
    AlgorithmSpec(
        id="stack_03",
        name="Stock Span Problem",
        category="stack",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "For each day i, the span is the number of consecutive days\n"
            "ending at i with a price <= arr[i] (including today).\n"
            "Monotonic stack of strictly-greater indices: pop while\n"
            "arr[top] <= arr[i]; the span is i - top_index, or i + 1\n"
            "if the stack is empty.\n"
            "Source: https://www.geeksforgeeks.org/the-stock-span-problem/"
        ),
        source_url="https://www.geeksforgeeks.org/the-stock-span-problem/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n daily prices.",
            "n": "length of arr.",
        },
        returns="a list of n spans (one per day).",
        source=STACK_03_SOURCE,
        setup_fn=_setup_stock_span,
        verify_fn=_verify_stock_span,
        samples=[
            Sample("arr = [100, 80, 60, 70, 60, 75, 85], n = 7", "[1, 1, 1, 2, 1, 4, 6]"),
            Sample("arr = [10, 4, 5, 90, 120, 80], n = 6", "[1, 1, 2, 4, 5, 1]"),
        ],
        hint="Stack of indices where arr[index] is strictly greater than today's. Pop <= and read the gap.",
        parents=["stack_02"],
        children=[],
    ),
]
