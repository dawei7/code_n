"""Mathematical algorithms.

Three problems from GFG's mathematical-algorithms catalog:

  01 GCD / Euclid         - greatest common divisor via the Euclidean algorithm
  02 Sieve of Eratosthenes - primes <= n
  03 Modular Exponentiation - (base^exp) % mod via repeated squaring

All three are short, deterministic, and pass the test gauntlet
at n=4, 8, 16. The setup keeps the inputs small enough that
the player can run the algorithm by hand and the brute-force
verify is fast.
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === math_01: GCD (Euclidean algorithm) ===

MATH_01_SOURCE = '''\
"""Optimal solution for math_01: GCD (Euclidean algorithm).

Repeatedly replace (a, b) with (b, a mod b) until b is 0; the
last non-zero a is the gcd. O(log min(a, b)) time.
"""


def solve(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
'''


def _setup_gcd(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    a = rng.randint(1, max(2, n) * 20)
    b = rng.randint(1, max(2, n) * 20)
    challenge._a = a
    challenge._b = b
    return {"a": a, "b": b}


def _verify_gcd(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    # Brute-force gcd.
    a, b = challenge._a, challenge._b
    g = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            g = i
    return result == g


# === math_02: Sieve of Eratosthenes ===

MATH_02_SOURCE = '''\
"""Optimal solution for math_02: Sieve of Eratosthenes.

Mark every multiple of each prime as composite. The remaining
unmarked numbers are the primes. O(n log log n) time.
"""


def solve(n):
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
'''


def _setup_sieve(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # Cap at 60 so the brute-force verify is fast.
    n = max(2, min(n * 4, 60))
    challenge._n = n
    return {"n": n}


def _verify_sieve(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    n = challenge._n
    expected = [i for i in range(n + 1) if i > 1 and all(i % d != 0 for d in range(2, int(i ** 0.5) + 1))]
    return result == expected


# === math_03: Modular Exponentiation ===

MATH_03_SOURCE = '''\
"""Optimal solution for math_03: Modular Exponentiation.

Repeated squaring. Maintain a result and a base. At each bit of
exp, square the base; if the bit is set, multiply the result
by the base. Take mod after every multiplication to keep
numbers small. O(log exp) time.
"""


def solve(base, exp, mod):
    if mod == 1:
        return 0
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return result
'''


def _setup_mod_exp(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    base = rng.randint(1, max(2, n) * 10)
    exp = rng.randint(1, max(2, n) * 5)
    mod = rng.randint(2, max(3, n) * 20)
    challenge._base = base
    challenge._exp = exp
    challenge._mod = mod
    return {"base": base, "exp": exp, "mod": mod}


def _verify_mod_exp(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    expected = pow(challenge._base, challenge._exp, challenge._mod)
    return result == expected


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="math_01",
        name="GCD (Euclidean)",
        category="math",
        difficulty=2,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Greatest common divisor of two positive integers a and b.\n"
            "Repeatedly replace (a, b) with (b, a mod b) until b is 0.\n"
            "Requirement: O(log min(a, b)).\n"
            "Source: https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/"
        ),
        source_url="https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/",
        params=["a", "b"],
        inputs={
            "a": "first non-negative integer.",
            "b": "second non-negative integer.",
        },
        returns="gcd(a, b).",
        source=MATH_01_SOURCE,
        setup_fn=_setup_gcd,
        verify_fn=_verify_gcd,
        samples=[
            Sample("a = 12, b = 18", "6"),
            Sample("a = 100, b = 75", "25"),
            Sample("a = 17, b = 13", "1"),
        ],
        hint="a, b = b, a % b, repeat until b == 0.",
        parents=["intro_01"],
        children=["math_02"],
    ),
    AlgorithmSpec(
        id="math_02",
        name="Sieve of Eratosthenes",
        category="math",
        difficulty=3,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Find every prime p with p <= n. Mark every multiple of each\n"
            "prime as composite. The numbers that remain unmarked are\n"
            "the primes. Standard textbook sieve.\n"
            "Requirement: O(n log log n) time, O(n) space.\n"
            "Source: https://www.geeksforgeeks.org/sieve-of-eratosthenes/"
        ),
        source_url="https://www.geeksforgeeks.org/sieve-of-eratosthenes/",
        params=["n"],
        inputs={
            "n": "upper bound (capped at 60 in the setup).",
        },
        returns="a list of primes p with p <= n.",
        source=MATH_02_SOURCE,
        setup_fn=_setup_sieve,
        verify_fn=_verify_sieve,
        samples=[
            Sample("n = 10", "[2, 3, 5, 7]"),
            Sample("n = 20", "[2, 3, 5, 7, 11, 13, 17, 19]"),
            Sample("n = 1", "[]"),
        ],
        hint="Sieve up to sqrt(n). For each prime i, mark i*i, i*i+i, ..., up to n.",
        parents=["math_01"],
        children=["math_03"],
    ),
    AlgorithmSpec(
        id="math_03",
        name="Modular Exponentiation",
        category="math",
        difficulty=4,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Compute (base^exp) mod mod without overflowing. Use\n"
            "repeated squaring: for each bit of exp, square the base\n"
            "(and reduce mod) and conditionally multiply the result.\n"
            "Requirement: O(log exp) multiplications.\n"
            "Source: https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/"
        ),
        source_url="https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/",
        params=["base", "exp", "mod"],
        inputs={
            "base": "the base (non-negative).",
            "exp": "the exponent (non-negative).",
            "mod": "the modulus (>= 1).",
        },
        returns="(base ** exp) % mod.",
        source=MATH_03_SOURCE,
        setup_fn=_setup_mod_exp,
        verify_fn=_verify_mod_exp,
        samples=[
            Sample("base = 2, exp = 10, mod = 1000", "24"),
            Sample("base = 3, exp = 5, mod = 100", "43"),
            Sample("base = 5, exp = 0, mod = 7", "1"),
        ],
        hint="Square the base, multiply into result on set bits. Reduce mod after every multiplication.",
        parents=["math_02"],
        children=["math_04"],
    ),
]


# === math_04: Karatsuba Multiplication ===

MATH_04_SOURCE = '''
def solve(x, y):
    """Karatsuba multiplication of two non-negative integers.

    Recursive divide and conquer: split each number into halves,
    compute 3 half-sized products (instead of 4), combine. Faster
    asymptotically than grade-school O(n^2) multiplication.
    """
    if x < 10 or y < 10:
        return x * y
    # Choose the split based on the larger operand.
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    power = 10 ** half
    a, b = divmod(x, power)
    c, d = divmod(y, power)
    ac = solve(a, c)
    bd = solve(b, d)
    ad_bc = solve(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + ad_bc * power + bd
'''


def _setup_karatsuba(challenge, n, seed):
    rng = random.Random(seed)
    # Bounded so the test gauntlet runs in reasonable time.
    max_digits = max(2, min(n, 6))
    a = rng.randint(1, 10 ** max_digits - 1)
    b = rng.randint(1, 10 ** max_digits - 1)
    challenge._a = a
    challenge._b = b
    return {"x": a, "y": b}


def _verify_karatsuba(challenge, result):
    if not isinstance(result, int):
        return False
    return result == challenge._a * challenge._b


SPECS.extend([
    AlgorithmSpec(
        id="math_04",
        name="Karatsuba Multiplication",
        category="math",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Multiply two non-negative integers using Karatsuba's\n"
            "divide-and-conquer algorithm. Split each operand in half,\n"
            "compute 3 half-sized products (ac, bd, and (a+b)(c+d) - ac - bd),\n"
            "and combine. Asymptotically O(n^log_2(3)) ~ O(n^1.585), faster\n"
            "than grade-school O(n^2).\n"
            "Source: https://www.geeksforgeeks.org/karatsuba-algorithm-for-fast-multiplication/"
        ),
        source_url="https://www.geeksforgeeks.org/karatsuba-algorithm-for-fast-multiplication/",
        params=["x", "y"],
        inputs={
            "x": "first non-negative integer.",
            "y": "second non-negative integer.",
        },
        returns="x * y.",
        source=MATH_04_SOURCE,
        setup_fn=_setup_karatsuba,
        verify_fn=_verify_karatsuba,
        samples=[
            Sample("x = 1234, y = 5678", "7006652"),
            Sample("x = 99, y = 99", "9801"),
        ],
        hint="Split each into halves. Compute ac, bd, (a+b)(c+d) - ac - bd. Combine with the right place values.",
        parents=["math_03"],
        children=[],
    ),
])
