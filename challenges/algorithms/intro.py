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
        children=["bit_04"],
    ),
])


# === bit_04: Power Set =======================================
#
# All subsets of an input list. Canonical bit-trick: each
# element i of the input is included in subset ``mask`` iff
# bit i of mask is set. The setup uses a small list (n <= 6)
# so the 2^n outer result is manageable.


BIT_04_SOURCE = '''
def solve(arr, n):
    """Return every subset of arr as a list of lists. Subsets are
    returned in the same bit-iteration order so the verify can
    do a plain equality check on the flattened representation.
    """
    result = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
        result.append(subset)
    return result
'''


def _setup_power_set(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # 2^n subsets blows up fast; cap at 6 so the test stays small.
    n = max(1, min(n, 6))
    arr = rng.sample(range(1, 100), n)
    challenge._arr = list(arr)
    return {"arr": list(arr), "n": n}


def _verify_power_set(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    arr = challenge._arr
    expected = []
    for mask in range(1 << len(arr)):
        subset = [arr[i] for i in range(len(arr)) if mask & (1 << i)]
        expected.append(subset)
    return result == expected


# === bit_05: Single Number III ==============================
#
# Two unique elements; everyone else appears twice. Classic
# trick: XOR everything, find a set bit (it differs between
# the two unique values), then split the array by that bit
# and XOR each half.


BIT_05_SOURCE = '''
def solve(arr):
    """Return the two elements that appear exactly once (sorted)."""
    xor_all = 0
    for v in arr:
        xor_all ^= v
    # Pick a set bit; bit 0 is fine if it's set, otherwise
    # pick the lowest set bit.
    diff_bit = xor_all & -xor_all
    a, b = 0, 0
    for v in arr:
        if v & diff_bit:
            a ^= v
        else:
            b ^= v
    return sorted([a, b])
'''


def _setup_single_number_iii(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n_pairs = max(1, min(n, 8))
    # Pick two unique values that differ in at least one bit.
    u1 = rng.randint(0, 1000)
    u2 = rng.randint(0, 1000)
    while (u1 ^ u2) == 0:
        u2 = rng.randint(0, 1000)
    pairs = []
    for _ in range(n_pairs):
        v = rng.randint(0, 1000)
        pairs.extend([v, v])
    rng.shuffle(pairs)
    # Drop the two unique values in at random positions.
    arr = list(pairs)
    arr.insert(rng.randint(0, len(arr)), u1)
    arr.insert(rng.randint(0, len(arr)), u2)
    challenge._expected = sorted([u1, u2])
    return {"arr": arr}


def _verify_single_number_iii(challenge, result: Any) -> bool:
    if not isinstance(result, list) or len(result) != 2:
        return False
    if result != sorted(result):
        return False
    return result == challenge._expected


# === bit_06: Bit Flips to Convert =============================
#
# Hamming distance between two integers: the number of bits
# that differ. XOR the two numbers, then count set bits.


BIT_06_SOURCE = '''
def solve(a, b):
    """Return the number of bit flips to convert a to b (Hamming distance)."""
    return bin(a ^ b).count("1")
'''


def _setup_bit_flips(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    max_val = max(2, 1 << min(n, 20))
    a = rng.randint(0, max_val)
    b = rng.randint(0, max_val)
    challenge._a = a
    challenge._b = b
    return {"a": a, "b": b}


def _verify_bit_flips(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == bin(challenge._a ^ challenge._b).count("1")


# Append the bit_04..06 specs.
SPECS.extend([
    AlgorithmSpec(
        id="bit_04",
        name="Power Set",
        category="intro",
        difficulty=3,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Return every subset of the input list as a list of lists.\n"
            "The number of subsets is 2^n; iteration is in the same bit\n"
            "order as the verifier, so the result is comparable directly.\n"
            "Requirement: O(2^n * n) time.\n"
            "Source: https://www.geeksforgeeks.org/power-set/"
        ),
        source_url="https://www.geeksforgeeks.org/power-set/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n distinct integers (capped at 6 in the setup).",
            "n": "length of arr.",
        },
        returns="a list of 2^n subsets (each a list), in bit-iteration order.",
        source=BIT_04_SOURCE,
        setup_fn=_setup_power_set,
        verify_fn=_verify_power_set,
        samples=[
            Sample("arr = [1, 2, 3], n = 3", "[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]"),
            Sample("arr = [1], n = 1", "[[], [1]]"),
        ],
        hint="For each mask in [0, 2^n), include arr[i] iff bit i of mask is set.",
        parents=["bit_03"],
        children=["bit_05"],
    ),
    AlgorithmSpec(
        id="bit_05",
        name="Single Number III",
        category="intro",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Every element in the input array appears exactly twice\n"
            "except for TWO elements, which each appear once. Return\n"
            "those two unique values (sorted). XOR everything to find\n"
            "a bit that differs between the two uniques, then split the\n"
            "array by that bit and XOR each half.\n"
            "Requirement: O(n) time, O(1) extra space.\n"
            "Source: https://www.geeksforgeeks.org/find-two-non-repeating-elements-given-array/"
        ),
        source_url="https://www.geeksforgeeks.org/find-two-non-repeating-elements-given-array/",
        params=["arr"],
        inputs={
            "arr": "list of integers; two unique values, others appear twice.",
        },
        returns="a sorted list [a, b] of the two unique elements.",
        source=BIT_05_SOURCE,
        setup_fn=_setup_single_number_iii,
        verify_fn=_verify_single_number_iii,
        samples=[
            Sample("arr = [1, 2, 3, 2, 1, 4]", "[3, 4]"),
            Sample("arr = [5, 1, 5]", "[1] -> wait, the setup always has pairs + 2 uniques, so this is invalid input."),
            Sample("arr = [1, 1, 2, 3]", "[2, 3]"),
        ],
        hint="XOR everything -> diff bit. Split by diff bit and XOR each side to recover each unique value.",
        parents=["bit_04"],
        children=["bit_06"],
    ),
    AlgorithmSpec(
        id="bit_06",
        name="Bit Flips to Convert",
        category="intro",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Given two non-negative integers a and b, return the number\n"
            "of bit flips to convert a to b. Equivalent to the Hamming\n"
            "distance between the two integers' binary representations.\n"
            "XOR a and b, then count the set bits.\n"
            "Requirement: O(log(max(a, b))).\n"
            "Source: https://www.geeksforgeeks.org/count-number-of-bits-to-be-flipped-to-convert-a-to-b/"
        ),
        source_url="https://www.geeksforgeeks.org/count-number-of-bits-to-be-flipped-to-convert-a-to-b/",
        params=["a", "b"],
        inputs={
            "a": "first integer.",
            "b": "second integer.",
        },
        returns="the Hamming distance between a and b.",
        source=BIT_06_SOURCE,
        setup_fn=_setup_bit_flips,
        verify_fn=_verify_bit_flips,
        samples=[
            Sample("a = 10 (1010), b = 20 (10100)", "3"),
            Sample("a = 7 (0111), b = 8 (1000)", "4"),
            Sample("a = 0, b = 0", "0"),
        ],
        hint="a XOR b has a 1 in every position where a and b differ. Count the 1-bits.",
        parents=["bit_05"],
        children=["bit_07"],
    ),
])


# === bit_07: Swap Odd and Even Bits ===
#
# Mask out the even bits, shift them right by 1, then mask out
# the odd bits and shift them left by 1. OR the two halves.


BIT_07_SOURCE = '''
def solve(n):
    """Swap the odd and even bits of n. Bit 0 (LSB) goes to bit 1, etc."""
    even_mask = 0x55555555  # 0101 0101 ...
    odd_mask = 0xAAAAAAAA   # 1010 1010 ...
    even_bits = (n & even_mask) >> 1
    odd_bits = (n & odd_mask) << 1
    return even_bits | odd_bits
'''


def _setup_swap_bits(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random((seed or 0) * 31 + n)
    max_val = max(2, 1 << min(n, 20))
    value = rng.randint(0, max_val)
    challenge._value = value
    return {"n": value}


def _verify_swap_bits(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    value = challenge._value
    even_mask = 0x55555555
    odd_mask = 0xAAAAAAAA
    expected = ((value & even_mask) >> 1) | ((value & odd_mask) << 1)
    return result == expected


# Append the bit_07 spec.
SPECS.extend([
    AlgorithmSpec(
        id="bit_07",
        name="Swap Odd and Even Bits",
        category="intro",
        difficulty=3,
        required_complexity=ComplexityClass.O_1,
        description=(
            "Swap the odd and even bits of n. Bit 0 (LSB) goes to bit 1;\n"
            "bit 1 goes to bit 0; and so on. Two mask operations:\n"
            "isolate the even bits (0x5555...), shift right by 1;\n"
            "isolate the odd bits (0xAAAA...), shift left by 1;\n"
            "OR them together.\n"
            "Requirement: O(1) (a fixed number of bitwise ops).\n"
            "Source: https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/"
        ),
        source_url="https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/",
        params=["n"],
        inputs={"n": "non-negative integer."},
        returns="n with odd and even bits swapped.",
        source=BIT_07_SOURCE,
        setup_fn=_setup_swap_bits,
        verify_fn=_verify_swap_bits,
        samples=[
            Sample("n = 23 (binary 10111)", "43 (binary 101011)"),
            Sample("n = 10 (binary 1010)", "5 (binary 0101)"),
            Sample("n = 0", "0"),
        ],
        hint="0x5555... masks even bits; 0xAAAA... masks odd bits. Shift and OR.",
        parents=["bit_06"],
        children=["bit_08"],
    ),
])


# === bit_08: Divide Without / ===
#
# Repeated subtraction: dividend = divisor * quotient + remainder.
# Build the quotient bit-by-bit from the most significant bit
# of the divisor. Use absolute values; handle the sign at the end.


BIT_08_SOURCE = '''
def solve(dividend, divisor):
    """Return dividend / divisor (integer division) without using /."""
    if divisor == 0:
        return 0  # undefined; the setup avoids this
    if dividend == 0:
        return 0
    # Work with absolute values.
    negative = (dividend < 0) != (divisor < 0)
    a = abs(dividend)
    b = abs(divisor)
    quotient = 0
    # Find the highest power of 2 of b that fits in a.
    power = 32
    while (b << power) > a:
        power -= 1
    while power >= 0:
        if (b << power) <= a:
            a -= b << power
            quotient |= 1 << power
        power -= 1
    if negative:
        quotient = -quotient
    return quotient
'''


def _setup_div_no_slash(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random((seed or 0) * 31 + n)
    # Pick a dividend and a divisor that give a sensible quotient.
    divisor = rng.randint(1, max(2, n))
    quotient = rng.randint(0, max(2, n) * 2)
    dividend = divisor * quotient + rng.randint(0, divisor - 1)
    if rng.random() < 0.5 and dividend != 0:
        dividend = -dividend
    if rng.random() < 0.5:
        divisor = -divisor
    challenge._dividend = dividend
    challenge._divisor = divisor
    return {"dividend": dividend, "divisor": divisor}


def _verify_div_no_slash(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    if challenge._divisor == 0:
        return result == 0
    # Brute force: repeated subtraction.
    a, b = abs(challenge._dividend), abs(challenge._divisor)
    q = 0
    while a >= b:
        a -= b
        q += 1
    if (challenge._dividend < 0) != (challenge._divisor < 0):
        q = -q
    return result == q


# === bit_09: Multiply Without * ===
#
# Bit-by-bit multiplication: for each set bit of b, add (a << k)
# to the result. O(log b) additions.


BIT_09_SOURCE = '''
def solve(a, b):
    """Return a * b without using *."""
    negative = (a < 0) != (b < 0)
    x = abs(a)
    y = abs(b)
    result = 0
    while y > 0:
        if y & 1:
            result += x
        x <<= 1
        y >>= 1
    if negative:
        result = -result
    return result
'''


def _setup_mul_no_star(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random((seed or 0) * 31 + n)
    max_val = max(2, n * 5)
    a = rng.randint(-max_val, max_val)
    b = rng.randint(-max_val, max_val)
    challenge._a = a
    challenge._b = b
    return {"a": a, "b": b}


def _verify_mul_no_star(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == challenge._a * challenge._b


# Append bit_08 and bit_09.
SPECS.extend([
    AlgorithmSpec(
        id="bit_08",
        name="Divide Without /",
        category="intro",
        difficulty=4,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Compute dividend / divisor (integer division) using only\n"
            "addition, subtraction, and shifts. Long-division-style:\n"
            "find the highest power of 2 of the divisor that fits in\n"
            "the dividend, subtract, repeat. Handle signs at the end.\n"
            "Requirement: O(log(dividend / divisor)).\n"
            "Source: https://www.geeksforgeeks.org/divide-two-numbers-without-using-multiplication-division-mod-operator/"
        ),
        source_url="https://www.geeksforgeeks.org/divide-two-numbers-without-using-multiplication-division-mod-operator/",
        params=["dividend", "divisor"],
        inputs={
            "dividend": "the dividend (non-zero; can be negative).",
            "divisor": "the divisor (non-zero; can be negative).",
        },
        returns="dividend // divisor.",
        source=BIT_08_SOURCE,
        setup_fn=_setup_div_no_slash,
        verify_fn=_verify_div_no_slash,
        samples=[
            Sample("dividend = 10, divisor = 3", "3"),
            Sample("dividend = 43, divisor = 8", "5"),
        ],
        hint="Find the highest shift of divisor that fits. Subtract. Repeat on the remainder.",
        parents=["bit_07"],
        children=["bit_09"],
    ),
    AlgorithmSpec(
        id="bit_09",
        name="Multiply Without *",
        category="intro",
        difficulty=3,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Compute a * b using only addition and shifts. For each\n"
            "set bit of b, add (a << k) to the result. O(log b).\n"
            "Source: https://www.geeksforgeeks.org/multiply-two-numbers-without-using/"
        ),
        source_url="https://www.geeksforgeeks.org/multiply-two-numbers-without-using/",
        params=["a", "b"],
        inputs={
            "a": "first factor (can be negative).",
            "b": "second factor (can be negative).",
        },
        returns="a * b.",
        source=BIT_09_SOURCE,
        setup_fn=_setup_mul_no_star,
        verify_fn=_verify_mul_no_star,
        samples=[
            Sample("a = 3, b = 5", "15"),
            Sample("a = -4, b = 6", "-24"),
        ],
        hint="For each set bit k of b, add (a << k) to the result.",
        parents=["bit_08"],
        children=[],
    ),
])
