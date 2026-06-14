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


# === math_05: Big Integer Add (string) ===

MATH_05_SOURCE = '''
def solve(a, b):
    """Add two non-negative integers given as digit strings.

    Reverse both strings, add digit by digit with carry, then
    reverse the result. Handles arbitrary length.
    """
    if not a:
        return b
    if not b:
        return a
    a_rev = a[::-1]
    b_rev = b[::-1]
    n = max(len(a_rev), len(b_rev))
    carry = 0
    out = []
    for i in range(n):
        da = int(a_rev[i]) if i < len(a_rev) else 0
        db = int(b_rev[i]) if i < len(b_rev) else 0
        s = da + db + carry
        out.append(str(s % 10))
        carry = s // 10
    if carry:
        out.append(str(carry))
    return "".join(reversed(out))
'''


def _setup_big_add(challenge, n, seed):
    rng = random.Random(seed)
    n_digits = max(1, min(n, 6))
    a = "".join(str(rng.randint(0, 9)) for _ in range(n_digits))
    if a[0] == "0" and len(a) > 1:
        a = "1" + a[1:]
    b = "".join(str(rng.randint(0, 9)) for _ in range(n_digits))
    if b[0] == "0" and len(b) > 1:
        b = "1" + b[1:]
    challenge._a = a
    challenge._b = b
    return {"a": a, "b": b}


def _verify_big_add(challenge, result):
    if not isinstance(result, str):
        return False
    expected = str(int(challenge._a) + int(challenge._b))
    return result.lstrip("0") == expected.lstrip("0") or (result == "0" and expected == "0")


# === math_06: Carmichael Function ===

MATH_06_SOURCE = '''
def solve(n):
    """Carmichael function: the smallest m > 0 such that
    a^m == 1 (mod n) for every a coprime to n.

    Lambda(n) is computed as follows:
    - lambda(1) = 1
    - lambda(2) = 1, lambda(4) = 2
    - for n = 2^k (k >= 3): lambda(n) = 2^(k-2)
    - lambda(p^k) for odd prime p: p^(k-1) * (p-1)
    - lambda(lcm of coprime a, b) = lcm(lambda(a), lambda(b))
    """
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 4:
        return 2
    # Factor n.
    temp = n
    factors = {}
    p = 2
    while p * p <= temp:
        while temp % p == 0:
            factors[p] = factors.get(p, 0) + 1
            temp //= p
        p += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    # Compute lambda for each prime power.
    from math import gcd
    lam = 1
    for p, k in factors.items():
        if p == 2:
            if k == 1:
                pk_lam = 1
            elif k == 2:
                pk_lam = 2
            else:
                pk_lam = 2 ** (k - 2)
        else:
            pk_lam = (p ** (k - 1)) * (p - 1)
        # lcm of two coprime lambdas.
        lam = lam * pk_lam // gcd(lam, pk_lam)
    return lam
'''


def _setup_carmichael(challenge, n, seed):
    rng = random.Random(seed)
    n_val = max(2, min(n, 30))
    # Pick a value with multiple small prime factors for an interesting answer.
    candidates = [12, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30, 35, 36, 40, 45, 48, 50]
    val = rng.choice(candidates)
    challenge._n = val
    return {"n": val}


def _verify_carmichael(challenge, result):
    if not isinstance(result, int):
        return False
    n = challenge._n
    # Find the actual Carmichael function by testing coprime a's.
    from math import gcd
    expected = 1
    for a in range(2, n):
        if gcd(a, n) == 1:
            # Find the multiplicative order of a mod n.
            k = 1
            x = a % n
            while x != 1:
                x = (x * a) % n
                k += 1
            expected = max(expected, k)
    return result == expected


SPECS.extend([
    AlgorithmSpec(
        id="math_05",
        name="Big Integer Add (Strings)",
        category="math",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Add two non-negative integers given as digit strings.\n"
            "Reverse, add digit-by-digit with carry, reverse the\n"
            "result. Handles arbitrary length without overflow.\n"
            "Source: https://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/"
        ),
        source_url="https://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/",
        params=["a", "b"],
        inputs={
            "a": "first integer (digit string).",
            "b": "second integer (digit string).",
        },
        returns="a + b as a digit string.",
        source=MATH_05_SOURCE,
        setup_fn=_setup_big_add,
        verify_fn=_verify_big_add,
        samples=[
            Sample('a = "123", b = "456"', '"579"'),
            Sample('a = "999", b = "1"', '"1000"'),
        ],
        hint="Reverse, add digit by digit, carry, reverse back.",
        parents=["math_04"],
        children=["math_06"],
    ),
    AlgorithmSpec(
        id="math_06",
        name="Carmichael Function",
        category="math",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "The Carmichael function lambda(n): the smallest m > 0\n"
            "such that a^m == 1 (mod n) for every a coprime to n.\n"
            "Compute via prime factorization: lambda(p^k) is p^(k-1)\n"
            "* (p-1) for odd primes, 2^(k-2) for n = 2^k, k >= 3.\n"
            "For composite n, lambda is the lcm of the per-prime-power\n"
            "lambdas.\n"
            "Source: https://www.geeksforgeeks.org/carmichael-function/"
        ),
        source_url="https://www.geeksforgeeks.org/carmichael-function/",
        params=["n"],
        inputs={
            "n": "positive integer (small, with multiple prime factors in the setup).",
        },
        returns="the Carmichael function value lambda(n).",
        source=MATH_06_SOURCE,
        setup_fn=_setup_carmichael,
        verify_fn=_verify_carmichael,
        samples=[
            Sample("n = 12", "2 (gcd(5,12)=1, 5^2 = 25 = 1 mod 12)"),
            Sample("n = 35", "12 (lambda(5)=4, lambda(7)=6, lcm=12)"),
        ],
        hint="Factor n. Compute lambda per prime power. Combine via lcm.",
        parents=["math_05"],
        children=[],
    ),
])


# === math_07: Extended Euclidean Algorithm ===

MATH_07_SOURCE = '''
def solve(a, b):
    """Extended Euclidean: a*x + b*y = gcd(a, b)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t
'''

def _setup_math_07(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # At least one of a, b is non-zero.
    a = rng.randint(1, max(2, n) * 30)
    b = rng.randint(0, max(2, n) * 30)
    challenge._a = a
    challenge._b = b
    return {"a": a, "b": b}

def _verify_math_07(challenge, result):
    if not isinstance(result, tuple) or len(result) != 3:
        return False
    g, x, y = result
    a, b = challenge._a, challenge._b
    # Brute-force: try every divisor of gcd(a, b) as the gcd, and
    # check that the bezout identity holds.
    expected_g = 1
    for d in range(1, min(a, b) + 1 if min(a, b) > 0 else max(a, b) + 1):
        if a % d == 0 and b % d == 0:
            expected_g = d
    if a == 0:
        expected_g = b
    if b == 0:
        expected_g = a
    if g != expected_g:
        return False
    if a * x + b * y != g:
        return False
    return True



# === math_08: Modular Multiplicative Inverse ===

MATH_08_SOURCE = '''
def solve(a, m):
    """Return a^-1 mod m using extended Euclidean."""
    if m == 1:
        return 0
    # Reduce a mod m first.
    a = a % m
    if a == 0:
        return 0  # no inverse
    # Extended gcd of (a, m).
    old_r, r = a, m
    old_s, s = 1, 0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    # old_r = gcd(a, m); old_s is the coefficient of a.
    if old_r != 1:
        return 0  # no inverse
    # Normalize to [0, m).
    return old_s % m
'''

def _setup_math_08(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # Pick m and a coprime to m.
    m = rng.randint(2, max(3, n) * 20)
    a = rng.randint(1, m - 1)
    while True:
        g = a
        b = m
        while b:
            g, b = b, g % b
        if g == 1:
            break
        a = rng.randint(1, m - 1)
    challenge._a = a
    challenge._m = m
    return {"a": a, "m": m}

def _verify_math_08(challenge, result):
    if not isinstance(result, int):
        return False
    a = challenge._a
    m = challenge._m
    # Verify: a * result = 1 (mod m).
    if m == 1:
        return result == 0
    return (a * result) % m == 1 % m



# === math_09: Miller-Rabin Primality Test ===

MATH_09_SOURCE = '''
def solve(n_val, k):
    """Miller-Rabin primality test with k random witnesses."""
    if n_val < 2:
        return False
    if n_val < 4:
        return True
    if n_val % 2 == 0:
        return False
    # Write n - 1 = 2^r * d with d odd.
    r, d = 0, n_val - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    # Test with k random witnesses.
    import random
    rng = random.Random(12345)  # deterministic for testing
    for _ in range(k):
        a = rng.randrange(2, n_val - 1)
        x = pow(a, d, n_val)
        if x == 1 or x == n_val - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n_val
            if x == n_val - 1:
                break
        else:
            return False
    return True
'''

def _setup_math_09(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # Pick a number to test: 50/50 a prime or composite.
    n = max(2, min(n, 200))
    if rng.random() < 0.5:
        # Pick a small prime.
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
        n_val = rng.choice(primes)
    else:
        # Pick a composite.
        while True:
            n_val = rng.randint(4, n)
            # Quick composite check.
            is_comp = False
            for d in range(2, int(n_val ** 0.5) + 1):
                if n_val % d == 0:
                    is_comp = True
                    break
            if is_comp:
                break
    k = 10  # 10 witnesses; safe for n < ~3 * 10^18
    challenge._n_val = n_val
    return {"n_val": n_val, "k": k}

def _verify_math_09(challenge, result):
    # Reference: deterministic trial division (n is small enough).
    n = challenge._n_val
    if n < 2:
        return result is False
    if n < 4:
        return result is True
    if n % 2 == 0:
        return result is False
    expected = True
    for d in range(3, int(n ** 0.5) + 1, 2):
        if n % d == 0:
            expected = False
            break
    return result == expected



# === math_10: Euler Totient Function ===

MATH_10_SOURCE = '''
def solve(n_val):
    """Euler's totient function phi(n) via prime factorization."""
    if n_val <= 0:
        return 0
    if n_val == 1:
        return 1
    result = n_val
    p = 2
    temp = n_val
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        # temp is a prime factor > sqrt(original n).
        result -= result // temp
    return result
'''

def _setup_math_10(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 100))
    challenge._n_val = n
    return {"n_val": n}

def _verify_math_10(challenge, result):
    n = challenge._n_val
    if n == 0:
        return result == 0
    # Brute force: count coprimes.
    expected = sum(1 for k in range(1, n + 1) if __import__("math").gcd(k, n) == 1)
    return result == expected


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="math_07",
        name="Extended Euclidean Algorithm",
        category="math",
        difficulty=4,
        required_complexity=ComplexityClass.O_LOG_N,
        description=("""
            Given two non-negative integers a and b (not both
            zero), find integers x and y such that a*x + b*y
            = gcd(a, b). Run Euclid's algorithm but keep the
            coefficients at each step: when (a, b) -> (b, a%b),
            the new x = old_y - (a//b) * old_x, and the new y
            = old_x. Return (gcd, x, y). O(log min(a, b)) time.
            Foundation for the modular inverse.
            Source: https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
            """),
        source_url="https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/",
        params=["a", "b"],
        inputs={
            "a": "first non-negative integer.",
            "b": "second non-negative integer.",
        },
        returns="a tuple (gcd, x, y) such that a*x + b*y = gcd.",
        source=MATH_07_SOURCE,
        setup_fn=_setup_math_07,
        verify_fn=_verify_math_07,
        samples=[
            Sample("a = 35, b = 15", "(5, 1, -2) since 35*1 + 15*(-2) = 5 = gcd(35, 15)"),
            Sample("a = 30, b = 20", "(10, 1, -1)"),
        ],
        hint="Run Euclid's algorithm. At each step where (a, b) -> (b, a%b), also update the coefficients x and y. Return (gcd, x, y).",
        parents=["math_06"],
        children=["math_08"],
    ),
    AlgorithmSpec(
        id="math_08",
        name="Modular Multiplicative Inverse",
        category="math",
        difficulty=4,
        required_complexity=ComplexityClass.O_LOG_N,
        description=("""
            Given a and m (with gcd(a, m) = 1), find x such
            that a*x = 1 (mod m). The inverse exists iff a and
            m are coprime. Use the extended Euclidean algorithm:
            the coefficient of a in a*x + m*y = gcd(a, m) = 1
            is the inverse (mod m). If gcd != 1, return 0 as a
            sentinel for 'no inverse'. O(log min(a, m)) time.
            Source: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
            """),
        source_url="https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/",
        params=["a", "m"],
        inputs={
            "a": "the integer whose inverse we want.",
            "m": "the modulus.",
        },
        returns="x in [0, m) such that a*x = 1 (mod m), or 0 if no inverse exists.",
        source=MATH_08_SOURCE,
        setup_fn=_setup_math_08,
        verify_fn=_verify_math_08,
        samples=[
            Sample("a = 3, m = 11", "4 since 3*4 = 12 = 1 (mod 11)"),
            Sample("a = 10, m = 17", "12 since 10*12 = 120 = 1 (mod 17) (10^-1 = 12)"),
        ],
        hint="Use the extended Euclidean algorithm. The coefficient of a in a*x + m*y = 1 is the inverse. Normalize mod m to get [0, m).",
        parents=["math_07"],
        children=["math_09"],
    ),
    AlgorithmSpec(
        id="math_09",
        name="Miller-Rabin Primality Test",
        category="math",
        difficulty=5,
        required_complexity=ComplexityClass.O_LOG_N,
        description=("""
            Given a positive integer n, return True iff n is
            probably prime using the Miller-Rabin probabilistic
            test. Write n - 1 = 2^r * d with d odd. For each
            witness a (random in [2, n-1]), compute x = a^d
            mod n. If x == 1 or x == n - 1, the test passes for
            this witness. Otherwise, square x up to r - 1
            times; if any result is n - 1, the test passes.
            If none of the witnesses reveal n as composite,
            n is probably prime. With enough random witnesses
            the false-positive rate is negligible.
            O(k log^3 n) time for k witnesses.
            Source: https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
            """),
        source_url="https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/",
        params=["n_val", "k"],
        inputs={
            "n_val": "the integer to test for primality.",
            "k": "number of random witnesses.",
        },
        returns="True if n_val is probably prime; False if definitely composite.",
        source=MATH_09_SOURCE,
        setup_fn=_setup_math_09,
        verify_fn=_verify_math_09,
        samples=[
            Sample("n_val = 17, k = 5", "True"),
            Sample("n_val = 18, k = 5", "False"),
            Sample("n_val = 561, k = 10", "True (Carmichael number passes Miller-Rabin)"),
        ],
        hint="Write n-1 = 2^r * d (d odd). For each random witness a, compute a^d mod n. If it's 1 or n-1, this witness is inconclusive. Otherwise square it up to r-1 times; if any is n-1, also inconclusive. If no witness reveals a factor, n is probably prime.",
        parents=["math_08"],
        children=["math_10"],
    ),
    AlgorithmSpec(
        id="math_10",
        name="Euler Totient Function",
        category="math",
        difficulty=3,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=("""
            Given a positive integer n, return phi(n): the
            number of integers in [1, n] coprime to n. Two
            approaches: (1) factorize n; phi is multiplicative
            and phi(p^k) = p^k - p^(k-1) = p^(k-1) * (p-1),
            so phi(n) = n * product over distinct prime p|n
            of (1 - 1/p). (2) Euler's sieve: for n up to N,
            compute all phi in O(N log log N). We use the
            factorization approach (n is small). O(sqrt(n)) time.
            Source: https://www.geeksforgeeks.org/eulers-totient-function/
            """),
        source_url="https://www.geeksforgeeks.org/eulers-totient-function/",
        params=["n_val"],
        inputs={
            "n_val": "positive integer.",
        },
        returns="phi(n) = |{1 <= k <= n : gcd(k, n) = 1}|.",
        source=MATH_10_SOURCE,
        setup_fn=_setup_math_10,
        verify_fn=_verify_math_10,
        samples=[
            Sample("n_val = 1", "1 (gcd(1,1) = 1, just the element 1)"),
            Sample("n_val = 10", "4 (1, 3, 7, 9 are coprime to 10)"),
            Sample("n_val = 36", "12"),
        ],
        hint="phi(n) = n * product over distinct prime p|n of (1 - 1/p). Factor n, and for each distinct prime p, multiply result by (1 - 1/p).",
        parents=["math_09"],
        children=[],
    ),
])
