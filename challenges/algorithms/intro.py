"""Introduction algorithms - the first thing every player sees.

This category is intentionally tiny. Its job is to teach the
basic ``solve(args) -> result`` contract without forcing the
player to think about any specific algorithm yet.
"""

from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.branding import GAME_TITLE
from code_n.counter import ComplexityClass
from code_n.grid import Grid, CellType
from code_n.tracked import TrackedList


# --- Setup / verify helpers (module-level so they're picklable,
# testable in isolation, and never accidentally close over
# per-instance state).

def _setup_hello_grid(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._data = [rng.randint(1, 99) for _ in range(n)]
    challenge._expected = max(challenge._data)

    challenge.grid = Grid(n, 3)
    challenge.grid.fill_row(0, challenge._data, CellType.UNSORTED)

    return {"data": TrackedList(challenge._data)}


def _verify_hello_grid(challenge, result: Any) -> bool:
    return result == challenge._expected


# --- Specs ---

INTRO_01_SOURCE = '''\
"""Optimal solution for intro_01: Hello Grid.

Find the maximum value in a list-like input. O(n) solution.
"""


def solve(data):
    """Iterate once, track the running maximum."""
    n = len(data)
    best = data[0]
    for i in range(1, n):
        value = data[i]
        if value > best:
            best = value
    return best
'''

SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="intro_01",
        name="Hello Grid",
        category="intro",
        difficulty=1,
        required_complexity=ComplexityClass.O_N,
        description=(
            f"Welcome to {GAME_TITLE}!\n"
            "Your task: Find the maximum value in the grid's first row.\n"
            "Use normal Python indexing and comparisons - every read and compare counts.\n"
            "Requirement: Solve it in O(n) operations."
        ),
        source_url="",  # Game-original, not a GFG article
        params=["data"],
        inputs={
            "data": "list-like of n integers. Read with data[i].",
        },
        returns="the maximum value in data.",
        source=INTRO_01_SOURCE,
        setup_fn=_setup_hello_grid,
        verify_fn=_verify_hello_grid,
        hint="Simply iterate through the list once, keeping track of the max.",
        samples=[
            Sample("data = [4, 9, 2]", "9"),
            Sample("data = [7]", "7"),
            Sample("data = [1, 5, 5, 3]", "5"),
        ],
        children=["sort_01", "search_01", "graph_01", "dp_01"],
    ),
]


# === bit_01: Count Set Bits (Hamming Weight) ================
#
# The simplest "bit manipulation" intro: walk through the
# bits of n and count the 1s. n is small (≤ 2^n) so the
# operation count is bounded by O(log n) which the
# ComplexityClass.O_N budget easily absorbs.


BIT_01_SOURCE = '''
def solve(n):
    """Count the 1-bits in n's binary representation (Hamming weight)."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
'''


def _setup_count_set_bits(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    # n controls the magnitude: value is a random int in [0, 2^n).
    # Cap n at 30 so the loop is short even for the larger test sizes.
    import math
    value = (hash((seed, n)) & 0x7FFFFFFF) % (1 << min(n, 30))
    challenge._expected = bin(value).count("1")
    return {"n": value}


def _verify_count_set_bits(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == challenge._expected


# === bit_02: Power of Two Check ==============================


BIT_02_SOURCE = '''
def solve(n):
    """True iff n is a power of two (n >= 1)."""
    return n > 0 and (n & (n - 1)) == 0
'''


def _setup_power_of_two(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    import math
    # Roughly half the time pick a power of two, half the time
    # pick something else. The value is bounded by 2^n.
    max_val = max(2, 1 << min(n, 20))
    rng = random.Random((seed or 0) * 31 + n)
    is_pow = rng.random() < 0.5
    if is_pow:
        # Pick a power of two in [1, max_val].
        k = rng.randint(0, int(math.log2(max_val)))
        value = 1 << k
    else:
        # Pick a non-power-of-two in [1, max_val].
        value = rng.randint(1, max_val)
        while value > 0 and (value & (value - 1)) == 0:
            value = rng.randint(1, max_val)
    challenge._expected = is_pow
    return {"n": value}


def _verify_power_of_two(challenge, result: Any) -> bool:
    if not isinstance(result, bool):
        return False
    return result == challenge._expected


# === bit_03: Single Number (XOR) =============================
#
# All elements appear twice except one. XOR of the array is
# the unique element. Setup picks the unique value, then
# builds the rest as random pairs.


BIT_03_SOURCE = '''
def solve(arr):
    """Return the element that appears exactly once (others appear twice)."""
    result = 0
    for v in arr:
        result ^= v
    return result
'''


def _setup_single_number(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n_pairs = max(1, min(n, 12))  # number of duplicate pairs
    # Build pairs and a unique value.
    unique = rng.randint(0, 1000)
    pairs: list[int] = []
    for _ in range(n_pairs):
        v = rng.randint(0, 1000)
        pairs.extend([v, v])
    # Shuffle, then drop the unique value in.
    rng.shuffle(pairs)
    insert_at = rng.randint(0, len(pairs))
    arr = pairs[:insert_at] + [unique] + pairs[insert_at:]
    challenge._expected = unique
    return {"arr": arr}


def _verify_single_number(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == challenge._expected


# Append the bit-manipulation specs to the intro SPECS list.
SPECS.extend([
    AlgorithmSpec(
        id="bit_01",
        name="Count Set Bits",
        category="intro",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Count the number of 1-bits in the binary representation\n"
            "of the input integer n. Also known as the Hamming weight\n"
            "or population count.\n"
            "Requirement: O(log n) bit-walking — comfortably within O(n).\n"
            "Source: https://www.geeksforgeeks.org/count-set-bits-in-an-integer/"
        ),
        source_url="https://www.geeksforgeeks.org/count-set-bits-in-an-integer/",
        params=["n"],
        inputs={"n": "non-negative integer."},
        returns="the number of 1-bits in n's binary representation.",
        source=BIT_01_SOURCE,
        setup_fn=_setup_count_set_bits,
        verify_fn=_verify_count_set_bits,
        samples=[
            Sample("n = 7", "3 (binary 111)"),
            Sample("n = 8", "1 (binary 1000)"),
            Sample("n = 0", "0"),
        ],
        hint="Walk through the bits: while n: count += n & 1; n >>= 1.",
        parents=["intro_01"],
        children=["bit_02"],
    ),
    AlgorithmSpec(
        id="bit_02",
        name="Power of Two Check",
        category="intro",
        difficulty=1,
        required_complexity=ComplexityClass.O_1,
        description=(
            "Return True iff the input n is a power of two (n >= 1).\n"
            "A single bitwise trick covers the whole problem.\n"
            "Requirement: O(1).\n"
            "Source: https://www.geeksforgeeks.org/program-to-find-whether-a-no-is-power-of-two/"
        ),
        source_url="https://www.geeksforgeeks.org/program-to-find-whether-a-no-is-power-of-two/",
        params=["n"],
        inputs={"n": "non-negative integer."},
        returns="True iff n is a power of two (1, 2, 4, 8, ...).",
        source=BIT_02_SOURCE,
        setup_fn=_setup_power_of_two,
        verify_fn=_verify_power_of_two,
        samples=[
            Sample("n = 1", "True"),
            Sample("n = 16", "True"),
            Sample("n = 6", "False"),
        ],
        hint="n is a power of two iff n > 0 and (n & (n - 1)) == 0. Why? Powers of two have exactly one bit set.",
        parents=["bit_01"],
        children=["bit_03"],
    ),
    AlgorithmSpec(
        id="bit_03",
        name="Single Number (XOR)",
        category="intro",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Every element in the input array appears exactly twice\n"
            "except for one element, which appears once. Return that\n"
            "unique element. The classic XOR trick handles it in O(n).\n"
            "Requirement: O(n) — single pass, no extra storage.\n"
            "Source: https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/"
        ),
        source_url="https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/",
        params=["arr"],
        inputs={"arr": "list of integers; one unique value, others appear twice."},
        returns="the unique element that appears exactly once.",
        source=BIT_03_SOURCE,
        setup_fn=_setup_single_number,
        verify_fn=_verify_single_number,
        samples=[
            Sample("arr = [2, 3, 5, 4, 5, 3, 4]", "2"),
            Sample("arr = [7, 1, 5, 1, 7]", "5"),
            Sample("arr = [42]", "42"),
        ],
        hint="XOR a XOR a = 0 and a XOR 0 = a. XOR everything in the array; the duplicates cancel.",
        parents=["bit_02"],
        children=[],
    ),
])
