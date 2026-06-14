"""Bit Manipulation algorithms.

12 specs covering the canonical GfG bit-manipulation catalog:

  bit_01  Count Set Bits               (Hamming weight)
  bit_02  Power of Two Check            (single-bit test)
  bit_03  Single Number (XOR)           (XOR trick)
  bit_04  Power Set                     (bit-mask subsets)
  bit_05  Single Number III             (XOR + diff bit)
  bit_06  Bit Flips to Convert          (Hamming distance)
  bit_07  Swap Odd and Even Bits        (mask + shift)
  bit_08  Divide Without /              (bit-by-bit long division)
  bit_09  Multiply Without *            (bit-by-bit shift-add)
  bit_10  Missing Number                (XOR + sum OR)
  bit_11  Bitwise AND of [0, n)         (range bit-trick)
  bit_12  Reverse Bits                  (mask-shift sandwich)

These specs (bit_01..bit_09) were previously mis-filed under
``intro.py``; they have been moved to their own category and
expanded with 3 new specs (bit_10..bit_12) to complete the
GfG bit-manipulation syllabus.
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


SPECS: list[AlgorithmSpec] = []


# === bit_01: Count Set Bits (Hamming Weight) ===

BIT_01_SOURCE = '''
def solve(n):
    """Count the 1-bits in n (Hamming weight)."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
'''


def _setup_bit_01(challenge, n, seed):
    import random
    # n controls the magnitude: value is a random int in [0, 2^n).
    # Cap n at 30 so the loop stays short even for larger test sizes.
    value = (hash((seed, n)) & 0x7FFFFFFF) % (1 << min(n, 30))
    challenge._expected = bin(value).count("1")
    return {"n": value}


def _verify_bit_01(challenge, result):
    return isinstance(result, int) and result == challenge._expected


# === bit_02: Power of Two Check ===

BIT_02_SOURCE = '''
def solve(n):
    """True iff n is a power of two (n >= 1)."""
    return n > 0 and (n & (n - 1)) == 0
'''


def _setup_bit_02(challenge, n, seed):
    import random, math
    # Half the time pick a power of two, half the time pick something else.
    max_val = max(2, 1 << min(n, 20))
    rng = random.Random((seed or 0) * 31 + n)
    is_pow = rng.random() < 0.5
    if is_pow:
        k = rng.randint(0, int(math.log2(max_val)))
        value = 1 << k
    else:
        value = rng.randint(1, max_val)
        while value > 0 and (value & (value - 1)) == 0:
            value = rng.randint(1, max_val)
    challenge._expected = is_pow
    return {"n": value}


def _verify_bit_02(challenge, result):
    return isinstance(result, bool) and result == challenge._expected


# === bit_03: Single Number (XOR) ===

BIT_03_SOURCE = '''
def solve(arr):
    """Return the element that appears exactly once (others appear twice)."""
    result = 0
    for v in arr:
        result ^= v
    return result
'''


def _setup_bit_03(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n_pairs = max(1, min(n, 12))
    unique = rng.randint(0, 1000)
    pairs = []
    for _ in range(n_pairs):
        v = rng.randint(0, 1000)
        pairs.extend([v, v])
    rng.shuffle(pairs)
    insert_at = rng.randint(0, len(pairs))
    arr = pairs[:insert_at] + [unique] + pairs[insert_at:]
    challenge._expected = unique
    return {"arr": arr}


def _verify_bit_03(challenge, result):
    return isinstance(result, int) and result == challenge._expected


# === bit_04: Power Set ===

BIT_04_SOURCE = '''
def solve(arr, n):
    """Return every subset of arr as a list of lists."""
    result = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
        result.append(subset)
    return result
'''


def _setup_bit_04(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # 2^n subsets blows up fast; cap at 6.
    n = max(1, min(n, 6))
    arr = rng.sample(range(1, 100), n)
    challenge._arr = list(arr)
    return {"arr": list(arr), "n": n}


def _verify_bit_04(challenge, result):
    if not isinstance(result, list):
        return False
    arr = challenge._arr
    expected = []
    for mask in range(1 << len(arr)):
        subset = [arr[i] for i in range(len(arr)) if mask & (1 << i)]
        expected.append(subset)
    return result == expected


# === bit_05: Single Number III ===

BIT_05_SOURCE = '''
def solve(arr):
    """Return the two elements that appear exactly once (sorted)."""
    xor_all = 0
    for v in arr:
        xor_all ^= v
    diff_bit = xor_all & -xor_all
    a, b = 0, 0
    for v in arr:
        if v & diff_bit:
            a ^= v
        else:
            b ^= v
    return sorted([a, b])
'''


def _setup_bit_05(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n_pairs = max(1, min(n, 8))
    u1 = rng.randint(0, 1000)
    u2 = rng.randint(0, 1000)
    while (u1 ^ u2) == 0:
        u2 = rng.randint(0, 1000)
    pairs = []
    for _ in range(n_pairs):
        v = rng.randint(0, 1000)
        pairs.extend([v, v])
    rng.shuffle(pairs)
    arr = list(pairs)
    arr.insert(rng.randint(0, len(arr)), u1)
    arr.insert(rng.randint(0, len(arr)), u2)
    challenge._expected = sorted([u1, u2])
    return {"arr": arr}


def _verify_bit_05(challenge, result):
    if not isinstance(result, list) or len(result) != 2:
        return False
    if result != sorted(result):
        return False
    return result == challenge._expected


# === bit_06: Bit Flips to Convert (Hamming Distance) ===

BIT_06_SOURCE = '''
def solve(a, b):
    """Return the number of bit flips to convert a to b (Hamming distance)."""
    return bin(a ^ b).count("1")
'''


def _setup_bit_06(challenge, n, seed):
    import random
    rng = random.Random(seed)
    max_val = max(2, 1 << min(n, 20))
    a = rng.randint(0, max_val)
    b = rng.randint(0, max_val)
    challenge._a = a
    challenge._b = b
    return {"a": a, "b": b}


def _verify_bit_06(challenge, result):
    if not isinstance(result, int):
        return False
    return result == bin(challenge._a ^ challenge._b).count("1")


# === bit_07: Swap Odd and Even Bits ===

BIT_07_SOURCE = '''
def solve(n):
    """Swap the odd and even bits of n. Bit 0 (LSB) goes to bit 1, etc."""
    even_mask = 0x55555555
    odd_mask = 0xAAAAAAAA
    even_bits = (n & even_mask) >> 1
    odd_bits = (n & odd_mask) << 1
    return even_bits | odd_bits
'''


def _setup_bit_07(challenge, n, seed):
    import random
    rng = random.Random((seed or 0) * 31 + n)
    max_val = max(2, 1 << min(n, 20))
    value = rng.randint(0, max_val)
    challenge._value = value
    return {"n": value}


def _verify_bit_07(challenge, result):
    if not isinstance(result, int):
        return False
    value = challenge._value
    even_mask = 0x55555555
    odd_mask = 0xAAAAAAAA
    expected = ((value & even_mask) >> 1) | ((value & odd_mask) << 1)
    return result == expected


# === bit_08: Divide Without / ===

BIT_08_SOURCE = '''
def solve(dividend, divisor):
    """Return dividend / divisor (integer division) without using /."""
    if divisor == 0:
        return 0
    if dividend == 0:
        return 0
    negative = (dividend < 0) != (divisor < 0)
    a = abs(dividend)
    b = abs(divisor)
    quotient = 0
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


def _setup_bit_08(challenge, n, seed):
    import random
    rng = random.Random((seed or 0) * 31 + n)
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


def _verify_bit_08(challenge, result):
    if not isinstance(result, int):
        return False
    if challenge._divisor == 0:
        return result == 0
    a, b = abs(challenge._dividend), abs(challenge._divisor)
    q = 0
    while a >= b:
        a -= b
        q += 1
    if (challenge._dividend < 0) != (challenge._divisor < 0):
        q = -q
    return result == q


# === bit_09: Multiply Without * ===

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


def _setup_bit_09(challenge, n, seed):
    import random
    rng = random.Random((seed or 0) * 31 + n)
    max_val = max(2, n * 5)
    a = rng.randint(-max_val, max_val)
    b = rng.randint(-max_val, max_val)
    challenge._a = a
    challenge._b = b
    return {"a": a, "b": b}


def _verify_bit_09(challenge, result):
    if not isinstance(result, int):
        return False
    return result == challenge._a * challenge._b


# === bit_10: Missing Number ===

BIT_10_SOURCE = '''
def solve(arr, n):
    """Find the missing integer in arr (length n, values in [0, n])."""
    # XOR all values and all indices 0..n; the missing value
    # is the survivor.
    result = n  # include the index n in the XOR
    for i, v in enumerate(arr):
        result ^= i ^ v
    return result
'''


def _setup_bit_10(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # arr has length n, values in [0, n], one missing.
    n = max(1, min(n, 12))
    full = set(range(n + 1))  # values in [0, n]
    missing = rng.randint(0, n)
    full.remove(missing)
    arr = list(full)
    rng.shuffle(arr)
    challenge._expected = missing
    return {"arr": list(arr), "n": n}


def _verify_bit_10(challenge, result):
    return isinstance(result, int) and result == challenge._expected


# === bit_11: Bitwise AND of Range ===

BIT_11_SOURCE = '''
def solve(left, right):
    """Return AND of all integers in [left, right] (the common prefix)."""
    shift = 0
    # While left and right differ, shift them both right by 1
    # (and count the shifts) to find the common prefix.
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift
'''


def _setup_bit_11(challenge, n, seed):
    import random
    rng = random.Random(seed)
    max_val = max(2, 1 << min(n, 20))
    left = rng.randint(0, max_val)
    right = rng.randint(left, max_val)
    challenge._left = left
    challenge._right = right
    return {"left": left, "right": right}


def _verify_bit_11(challenge, result):
    if not isinstance(result, int):
        return False
    expected = challenge._left
    for v in range(challenge._left, challenge._right + 1):
        expected &= v
    return result == expected


# === bit_12: Reverse Bits ===

BIT_12_SOURCE = '''
def solve(n):
    """Reverse the bits of the 32-bit unsigned integer n."""
    result = 0
    for i in range(32):
        # Take bit i of n, place it at bit (31 - i) of result.
        if n & (1 << i):
            result |= 1 << (31 - i)
    return result
'''


def _setup_bit_12(challenge, n, seed):
    import random
    rng = random.Random((seed or 0) * 31 + n)
    value = rng.randint(0, 2 ** min(n, 31) - 1)
    challenge._value = value
    return {"n": value}


def _verify_bit_12(challenge, result):
    if not isinstance(result, int):
        return False
    # 32-bit bit-reverse of challenge._value.
    expected = 0
    v = challenge._value
    for i in range(32):
        if v & (1 << i):
            expected |= 1 << (31 - i)
    return result == expected


SPECS.extend([
    AlgorithmSpec(
        id="bit_01",
        name="Count Set Bits",
        category="bit_manipulation",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Count the number of 1-bits in the binary\n"
            "representation of the input integer n. Also known\n"
            "as the Hamming weight or population count.\n"
            "Walk through the bits: while n, count += n & 1;\n"
            "n >>= 1. O(log n) bit-walks, comfortably within O(n).\n"
            "Source: https://www.geeksforgeeks.org/count-set-bits-in-an-integer/"
        ),
        source_url="https://www.geeksforgeeks.org/count-set-bits-in-an-integer/",
        params=["n"],
        inputs={"n": "non-negative integer."},
        returns="the number of 1-bits in n's binary representation.",
        source=BIT_01_SOURCE,
        setup_fn=_setup_bit_01,
        verify_fn=_verify_bit_01,
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
        category="bit_manipulation",
        difficulty=1,
        required_complexity=ComplexityClass.O_1,
        description=(
            "Return True iff the input n is a power of two.\n"
            "A single bitwise trick covers the whole problem:\n"
            "n is a power of two iff n > 0 and (n & (n - 1)) == 0.\n"
            "Why? Powers of two have exactly one bit set, so\n"
            "n - 1 clears that bit and only that bit, and the\n"
            "AND with n is 0. O(1).\n"
            "Source: https://www.geeksforgeeks.org/program-to-find-whether-a-no-is-power-of-two/"
        ),
        source_url="https://www.geeksforgeeks.org/program-to-find-whether-a-no-is-power-of-two/",
        params=["n"],
        inputs={"n": "non-negative integer."},
        returns="True iff n is a power of two (1, 2, 4, 8, ...).",
        source=BIT_02_SOURCE,
        setup_fn=_setup_bit_02,
        verify_fn=_verify_bit_02,
        samples=[
            Sample("n = 1", "True"),
            Sample("n = 16", "True"),
            Sample("n = 6", "False"),
        ],
        hint="n is a power of two iff n > 0 and (n & (n - 1)) == 0.",
        parents=["bit_01"],
        children=["bit_03"],
    ),
    AlgorithmSpec(
        id="bit_03",
        name="Single Number (XOR)",
        category="bit_manipulation",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Every element in the input array appears exactly\n"
            "twice except for one element, which appears once.\n"
            "Return that unique element. The classic XOR trick\n"
            "handles it in O(n) with O(1) extra space.\n"
            "Source: https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/"
        ),
        source_url="https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/",
        params=["arr"],
        inputs={"arr": "list of integers; one unique value, others appear twice."},
        returns="the unique element that appears exactly once.",
        source=BIT_03_SOURCE,
        setup_fn=_setup_bit_03,
        verify_fn=_verify_bit_03,
        samples=[
            Sample("arr = [2, 3, 5, 4, 5, 3, 4]", "2"),
            Sample("arr = [7, 1, 5, 1, 7]", "5"),
            Sample("arr = [42]", "42"),
        ],
        hint="XOR a XOR a = 0 and a XOR 0 = a. XOR everything; duplicates cancel.",
        parents=["bit_02"],
        children=["bit_04"],
    ),
    AlgorithmSpec(
        id="bit_04",
        name="Power Set",
        category="bit_manipulation",
        difficulty=3,
        required_complexity=ComplexityClass.O_2N,
        description=(
            "Return every subset of the input list as a list\n"
            "of lists. The number of subsets is 2^n; for each\n"
            "mask in [0, 2^n), include arr[i] iff bit i of mask\n"
            "is set. O(2^n * n) time.\n"
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
        setup_fn=_setup_bit_04,
        verify_fn=_verify_bit_04,
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
        category="bit_manipulation",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Every element in the input array appears exactly\n"
            "twice except for TWO elements, which each appear\n"
            "once. Return those two unique values (sorted).\n"
            "XOR everything to find a bit that differs between\n"
            "the two uniques, then split the array by that bit\n"
            "and XOR each half to recover each unique value.\n"
            "O(n) time, O(1) extra space.\n"
            "Source: https://www.geeksforgeeks.org/find-two-non-repeating-elements-given-array/"
        ),
        source_url="https://www.geeksforgeeks.org/find-two-non-repeating-elements-given-array/",
        params=["arr"],
        inputs={"arr": "list of integers; two unique values, others appear twice."},
        returns="a sorted list [a, b] of the two unique elements.",
        source=BIT_05_SOURCE,
        setup_fn=_setup_bit_05,
        verify_fn=_verify_bit_05,
        samples=[
            Sample("arr = [1, 2, 3, 2, 1, 4]", "[3, 4]"),
            Sample("arr = [1, 1, 2, 3]", "[2, 3]"),
        ],
        hint="XOR everything -> diff bit. Split by diff bit and XOR each side.",
        parents=["bit_04"],
        children=["bit_06"],
    ),
    AlgorithmSpec(
        id="bit_06",
        name="Bit Flips to Convert",
        category="bit_manipulation",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Given two non-negative integers a and b, return\n"
            "the number of bit flips to convert a to b. This is\n"
            "equivalent to the Hamming distance between the two\n"
            "integers' binary representations. XOR a and b, then\n"
            "count the set bits. O(log(max(a, b))).\n"
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
        setup_fn=_setup_bit_06,
        verify_fn=_verify_bit_06,
        samples=[
            Sample("a = 10 (1010), b = 20 (10100)", "3"),
            Sample("a = 7 (0111), b = 8 (1000)", "4"),
            Sample("a = 0, b = 0", "0"),
        ],
        hint="a XOR b has a 1 in every position where a and b differ. Count the 1-bits.",
        parents=["bit_05"],
        children=["bit_07"],
    ),
    AlgorithmSpec(
        id="bit_07",
        name="Swap Odd and Even Bits",
        category="bit_manipulation",
        difficulty=3,
        required_complexity=ComplexityClass.O_1,
        description=(
            "Swap the odd and even bits of n. Bit 0 (LSB) goes\n"
            "to bit 1, bit 1 goes to bit 0, and so on. Two mask\n"
            "operations: isolate the even bits with 0x5555..., shift\n"
            "right by 1; isolate the odd bits with 0xAAAA..., shift\n"
            "left by 1; OR the two halves. O(1).\n"
            "Source: https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/"
        ),
        source_url="https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/",
        params=["n"],
        inputs={"n": "non-negative integer."},
        returns="n with odd and even bits swapped.",
        source=BIT_07_SOURCE,
        setup_fn=_setup_bit_07,
        verify_fn=_verify_bit_07,
        samples=[
            Sample("n = 23 (binary 10111)", "43 (binary 101011)"),
            Sample("n = 10 (binary 1010)", "5 (binary 0101)"),
            Sample("n = 0", "0"),
        ],
        hint="0x5555... masks even bits; 0xAAAA... masks odd bits. Shift and OR.",
        parents=["bit_06"],
        children=["bit_08"],
    ),
    AlgorithmSpec(
        id="bit_08",
        name="Divide Without /",
        category="bit_manipulation",
        difficulty=4,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Compute dividend / divisor (integer division) using\n"
            "only addition, subtraction, and shifts. Long-division-\n"
            "style: find the highest power of 2 of the divisor that\n"
            "fits in the dividend, subtract, repeat on the remainder.\n"
            "Handle signs at the end. O(log(dividend / divisor)).\n"
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
        setup_fn=_setup_bit_08,
        verify_fn=_verify_bit_08,
        samples=[
            Sample("dividend = 10, divisor = 3", "3"),
            Sample("dividend = 43, divisor = 8", "5"),
        ],
        hint="Find the highest shift of divisor that fits. Subtract. Repeat.",
        parents=["bit_07"],
        children=["bit_09"],
    ),
    AlgorithmSpec(
        id="bit_09",
        name="Multiply Without *",
        category="bit_manipulation",
        difficulty=3,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Compute a * b using only addition and shifts. For\n"
            "each set bit of b, add (a << k) to the result. O(log b).\n"
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
        setup_fn=_setup_bit_09,
        verify_fn=_verify_bit_09,
        samples=[
            Sample("a = 3, b = 5", "15"),
            Sample("a = -4, b = 6", "-24"),
        ],
        hint="For each set bit k of b, add (a << k) to the result.",
        parents=["bit_08"],
        children=["bit_10"],
    ),
    AlgorithmSpec(
        id="bit_10",
        name="Missing Number",
        category="bit_manipulation",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Given an array arr of n distinct integers in\n"
            "[0, n] (so the array has length n and the values\n"
            "should be exactly 0, 1, ..., n but one value is\n"
            "missing), return the missing value. Two clean\n"
            "solutions: (1) XOR all values with all indices 0..n;\n"
            "the missing value is left over because every other\n"
            "value cancels with its index. (2) Compute the\n"
            "expected sum n*(n+1)/2 and subtract the actual sum.\n"
            "Both run in O(n) time and O(1) extra space.\n"
            "Source: https://www.geeksforgeeks.org/find-the-missing-number/"
        ),
        source_url="https://www.geeksforgeeks.org/find-the-missing-number/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n distinct integers in [0, n] with one value missing.",
            "n": "length of arr (so the missing value is in [0, n]).",
        },
        returns="the missing integer.",
        source=BIT_10_SOURCE,
        setup_fn=_setup_bit_10,
        verify_fn=_verify_bit_10,
        samples=[
            Sample("arr = [3, 0, 1], n = 3", "2"),
            Sample("arr = [0, 1, 2, 3, 5], n = 5", "4"),
            Sample("arr = [0], n = 1", "1"),
        ],
        hint="XOR every index with its value; the missing value is the one left over.",
        parents=["bit_09"],
        children=["bit_11"],
    ),
    AlgorithmSpec(
        id="bit_11",
        name="Bitwise AND of Range",
        category="bit_manipulation",
        difficulty=5,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Given two non-negative integers left and right\n"
            "with left <= right, return the bitwise AND of all\n"
            "integers in the inclusive range [left, right].\n"
            "The result is the common prefix (most significant\n"
            "bits) of left and right, shifted into place. To\n"
            "find it: keep clearing the lowest differing bit of\n"
            "left while left > right; that's the common prefix.\n"
            "Source: https://www.geeksforgeeks.org/bitwise-and-of-numbers-range/"
        ),
        source_url="https://www.geeksforgeeks.org/bitwise-and-of-numbers-range/",
        params=["left", "right"],
        inputs={
            "left": "left bound of the range (inclusive).",
            "right": "right bound of the range (inclusive, >= left).",
        },
        returns="the bitwise AND of all integers in [left, right].",
        source=BIT_11_SOURCE,
        setup_fn=_setup_bit_11,
        verify_fn=_verify_bit_11,
        samples=[
            Sample("left = 5, right = 7", "4 (binary 101 AND 110 AND 111 = 100)"),
            Sample("left = 0, right = 0", "0"),
            Sample("left = 1, right = 1", "1"),
            Sample("left = 12, right = 15", "12 (all 1100..1111 share 1100)"),
        ],
        hint="Keep clearing the lowest differing bit of left while left < right.",
        parents=["bit_10"],
        children=["bit_12"],
    ),
    AlgorithmSpec(
        id="bit_12",
        name="Reverse Bits",
        category="bit_manipulation",
        difficulty=3,
        required_complexity=ComplexityClass.O_1,
        description=(
            "Reverse the bits of a 32-bit unsigned integer n.\n"
            "For each of the 32 bit positions, take bit i of n\n"
            "and place it at bit (31 - i) of the result.\n"
            "O(1) (a fixed number of bitwise ops).\n"
            "Source: https://www.geeksforgeeks.org/reverse-bits-of-an-integer/"
        ),
        source_url="https://www.geeksforgeeks.org/reverse-bits-of-an-integer/",
        params=["n"],
        inputs={"n": "non-negative integer (treated as 32-bit unsigned)."},
        returns="n with its 32 bits reversed (LSB goes to MSB).",
        source=BIT_12_SOURCE,
        setup_fn=_setup_bit_12,
        verify_fn=_verify_bit_12,
        samples=[
            Sample("n = 0b00000010100101000001111010011100 (43261596)", "964176192 (binary 00111001011110000010100101000000)"),
            Sample("n = 0", "0"),
            Sample("n = 1 (binary 1, only the LSB set)", "2^31 = 2147483648"),
        ],
        hint="For each bit position i in 0..31, take bit i of n and place it at bit (31 - i) of result.",
        parents=["bit_11"],
        children=[],
    ),
])
