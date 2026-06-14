"""Spec generator input - 4 new math specs for Session 1.

Covers the GfG mathematical-algorithms topics that
math_01..06 (GCD, Sieve, ModPow, Karatsuba, Big-Add,
Carmichael) don't already cover:

  math_07  Extended Euclidean Algorithm       (ax + by = gcd(a,b))
  math_08  Modular Multiplicative Inverse    (a^-1 mod m)
  math_09  Miller-Rabin Primality Test       (probabilistic)
  math_10  Euler Totient Function            (count of coprimes < n)

After this batch, math.py covers the canonical number-theory
essentials from GfG.

Run with:
    cd c:/dawei7/code_n
    .venv/Scripts/python.exe -m challenges.algorithms._generator \\
        --module math \\
        --input batch_math_session1.py
"""


SPECS_TO_ADD = [
    # ============================================================
    # math_07: Extended Euclidean Algorithm
    # ============================================================
    {
        "id": "math_07",
        "name": "Extended Euclidean Algorithm",
        "category": "math",
        "difficulty": 4,
        "complexity": "O_LOG_N",
        "description": (
            "Given two non-negative integers a and b (not both\n"
            "zero), find integers x and y such that a*x + b*y\n"
            "= gcd(a, b). Run Euclid's algorithm but keep the\n"
            "coefficients at each step: when (a, b) -> (b, a%b),\n"
            "the new x = old_y - (a//b) * old_x, and the new y\n"
            "= old_x. Return (gcd, x, y). O(log min(a, b)) time.\n"
            "Foundation for the modular inverse.\n"
            "Source: https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/"
        ),
        "source_url": "https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/",
        "params": ["a", "b"],
        "inputs": {
            "a": "first non-negative integer.",
            "b": "second non-negative integer.",
        },
        "returns": "a tuple (gcd, x, y) such that a*x + b*y = gcd.",
        "solve": '''
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
''',
        "setup": '''
import random
rng = random.Random(seed)
# At least one of a, b is non-zero.
a = rng.randint(1, max(2, n) * 30)
b = rng.randint(0, max(2, n) * 30)
challenge._a = a
challenge._b = b
return {"a": a, "b": b}
''',
        "verify": '''
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
''',
        "samples": [
            ("a = 35, b = 15", "(5, 1, -2) since 35*1 + 15*(-2) = 5 = gcd(35, 15)"),
            ("a = 30, b = 20", "(10, 1, -1)"),
        ],
        "hint": "Run Euclid's algorithm. At each step where (a, b) -> (b, a%b), also update the coefficients x and y. Return (gcd, x, y).",
        "parents": ["math_06"],
        "children": ["math_08"],
    },

    # ============================================================
    # math_08: Modular Multiplicative Inverse
    # ============================================================
    {
        "id": "math_08",
        "name": "Modular Multiplicative Inverse",
        "category": "math",
        "difficulty": 4,
        "complexity": "O_LOG_N",
        "description": (
            "Given a and m (with gcd(a, m) = 1), find x such\n"
            "that a*x = 1 (mod m). The inverse exists iff a and\n"
            "m are coprime. Use the extended Euclidean algorithm:\n"
            "the coefficient of a in a*x + m*y = gcd(a, m) = 1\n"
            "is the inverse (mod m). If gcd != 1, return 0 as a\n"
            "sentinel for 'no inverse'. O(log min(a, m)) time.\n"
            "Source: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/"
        ),
        "source_url": "https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/",
        "params": ["a", "m"],
        "inputs": {
            "a": "the integer whose inverse we want.",
            "m": "the modulus.",
        },
        "returns": "x in [0, m) such that a*x = 1 (mod m), or 0 if no inverse exists.",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
if not isinstance(result, int):
    return False
a = challenge._a
m = challenge._m
# Verify: a * result = 1 (mod m).
if m == 1:
    return result == 0
return (a * result) % m == 1 % m
''',
        "samples": [
            ("a = 3, m = 11", "4 since 3*4 = 12 = 1 (mod 11)"),
            ("a = 10, m = 17", "12 since 10*12 = 120 = 1 (mod 17) (10^-1 = 12)"),
        ],
        "hint": "Use the extended Euclidean algorithm. The coefficient of a in a*x + m*y = 1 is the inverse. Normalize mod m to get [0, m).",
        "parents": ["math_07"],
        "children": ["math_09"],
    },

    # ============================================================
    # math_09: Miller-Rabin Primality Test
    # ============================================================
    {
        "id": "math_09",
        "name": "Miller-Rabin Primality Test",
        "category": "math",
        "difficulty": 5,
        "complexity": "O_LOG_N",
        "description": (
            "Given a positive integer n, return True iff n is\n"
            "probably prime using the Miller-Rabin probabilistic\n"
            "test. Write n - 1 = 2^r * d with d odd. For each\n"
            "witness a (random in [2, n-1]), compute x = a^d\n"
            "mod n. If x == 1 or x == n - 1, the test passes for\n"
            "this witness. Otherwise, square x up to r - 1\n"
            "times; if any result is n - 1, the test passes.\n"
            "If none of the witnesses reveal n as composite,\n"
            "n is probably prime. With enough random witnesses\n"
            "the false-positive rate is negligible.\n"
            "O(k log^3 n) time for k witnesses.\n"
            "Source: https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/"
        ),
        "source_url": "https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/",
        "params": ["n_val", "k"],
        "inputs": {
            "n_val": "the integer to test for primality.",
            "k": "number of random witnesses.",
        },
        "returns": "True if n_val is probably prime; False if definitely composite.",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("n_val = 17, k = 5", "True"),
            ("n_val = 18, k = 5", "False"),
            ("n_val = 561, k = 10", "True (Carmichael number passes Miller-Rabin)"),
        ],
        "hint": "Write n-1 = 2^r * d (d odd). For each random witness a, compute a^d mod n. If it's 1 or n-1, this witness is inconclusive. Otherwise square it up to r-1 times; if any is n-1, also inconclusive. If no witness reveals a factor, n is probably prime.",
        "parents": ["math_08"],
        "children": ["math_10"],
    },

    # ============================================================
    # math_10: Euler Totient Function
    # ============================================================
    {
        "id": "math_10",
        "name": "Euler Totient Function",
        "category": "math",
        "difficulty": 3,
        "complexity": "O_N_LOG_N",
        "description": (
            "Given a positive integer n, return phi(n): the\n"
            "number of integers in [1, n] coprime to n. Two\n"
            "approaches: (1) factorize n; phi is multiplicative\n"
            "and phi(p^k) = p^k - p^(k-1) = p^(k-1) * (p-1),\n"
            "so phi(n) = n * product over distinct prime p|n\n"
            "of (1 - 1/p). (2) Euler's sieve: for n up to N,\n"
            "compute all phi in O(N log log N). We use the\n"
            "factorization approach (n is small). O(sqrt(n)) time.\n"
            "Source: https://www.geeksforgeeks.org/eulers-totient-function/"
        ),
        "source_url": "https://www.geeksforgeeks.org/eulers-totient-function/",
        "params": ["n_val"],
        "inputs": {"n_val": "positive integer."},
        "returns": "phi(n) = |{1 <= k <= n : gcd(k, n) = 1}|.",
        "solve": '''
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
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(1, min(n, 100))
challenge._n_val = n
return {"n_val": n}
''',
        "verify": '''
n = challenge._n_val
if n == 0:
    return result == 0
# Brute force: count coprimes.
expected = sum(1 for k in range(1, n + 1) if __import__("math").gcd(k, n) == 1)
return result == expected
''',
        "samples": [
            ("n_val = 1", "1 (gcd(1,1) = 1, just the element 1)"),
            ("n_val = 10", "4 (1, 3, 7, 9 are coprime to 10)"),
            ("n_val = 36", "12"),
        ],
        "hint": "phi(n) = n * product over distinct prime p|n of (1 - 1/p). Factor n, and for each distinct prime p, multiply result by (1 - 1/p).",
        "parents": ["math_09"],
        "children": [],
    },
]
