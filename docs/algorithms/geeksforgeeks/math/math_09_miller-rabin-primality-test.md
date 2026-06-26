# Miller-Rabin Primality Test

| | |
|---|---|
| **ID** | `math_09` |
| **Category** | math |
| **Complexity (required)** | $O(K \log^3 N)$ Time, $O(1)$ Space |
| **Difficulty** | 9/10 |
| **Interview relevance** | 1/10 |
| **Wikipedia** | [Miller–Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) |

## Problem statement

Given a massively large integer `N` (e.g., 10^{18} or larger). Determine if `N` is a prime number.
Standard $O(\sqrt{N})$ division checking takes 1 billion operations for 10^{18}, which is too slow.
The Sieve of Eratosthenes (`math_02`) requires allocating an array of size 10^{18}, which is physically impossible.
You must solve this in incredibly fast logarithmic time using a probabilistic algorithm.

**Input:** An integer `N` and an integer `K` (number of testing rounds).
**Output:** A boolean. `True` if `N` is *almost certainly* prime, `False` if `N` is *definitely* composite.

## When to use it

- When checking primality of a single, astronomically large number (e.g. 64-bit bounds and beyond).
- The cornerstone of modern RSA cryptography key generation.

## Approach

**1. Fermat's Little Theorem (The First Filter):**
Fermat stated that if N is prime, then A^{N-1} \equiv 1 \pmod N for any random base A.
So, we can just pick a random number A, compute A^{N-1} \pmod N using Modular Exponentiation (`math_03`), and if it doesn't equal 1, N is DEFINITELY composite!
*The Flaw:* Carmichael numbers (like 561) are composite, but they magically satisfy Fermat's test and output 1 anyway! They are "pseudoprimes" that trick the test.

**2. The Non-Trivial Square Root (The Miller-Rabin Fix):**
Miller and Rabin added a second mathematical rule to catch the liars.
In modulo arithmetic, the equation X^2 \equiv 1 \pmod N has two trivial roots if N is prime: X=1 and X=N-1 (which is -1).
If we EVER find a number X where X^2 \equiv 1 \pmod N, but X is NEITHER 1 nor N-1, then N is mathematically guaranteed to be composite!

**3. The Algorithm (Factorizing N-1):**
Since N is odd, N-1 is even. We can factor N-1 into 2^D \cdot R (where R is odd).
We pick a random base A. We compute X = A^R \pmod N.
If X == 1 or X == N-1, this round passes! N might be prime.
If not, we square X repeatedly (D times): X = (X \cdot X) \pmod N.
Every time we square it, we are checking if we hit 1.
- If we hit N-1, it's a valid root! The round passes.
- If we finish all D squarings and never hit N-1, then N is DEFINITELY composite!

**4. Probabilistic Rounds (K):**
One round of testing might get tricked by 1/4 of composite numbers. But if we run the test K times with K different random bases A, the probability of a composite number surviving all K rounds is (\frac{1}{4})^K.
If K=40, the probability of being wrong is 1 in 10^{24} (virtually impossible). Thus we declare it "almost certainly prime".

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for math_09: Miller-Rabin Primality Test.

Given a positive integer n, return True iff n is
"""


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
```

</details>

## Walk-through

Is `N = 13` prime? `k = 1`.
`N - 1 = 12`.
12 = 2^2 \cdot 3. So `d = 2`, `r = 3`.

1. **Round 1:** Pick random `a = 2`.
   - Calculate X = 2^3 \pmod{13} = 8 \pmod{13} = 8.
   - X is not 1 or 12.
   - Enter squaring loop (`d-1 = 1` time).
   - X = (8 \cdot 8) \pmod{13} = 64 \pmod{13} = 12.
   - X == 12 (N-1). Round Passed! `break`.
2. All rounds finished. Return `True`! ✓

*What if `N = 15` (Composite)?*
`N - 1 = 14 = 2^1 \cdot 7`. `d = 1`, `r = 7`.
1. **Round 1:** Pick `a = 2`.
   - X = 2^7 \pmod{15} = 128 \pmod{15} = 8.
   - X is not 1 or 14.
   - Squaring loop runs `d-1 = 0` times. (Doesn't run).
   - `round_passed = False`. Return `False`. (Composite!) ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(\log N)$ | $O(1)$ |
| **Average** | $O(K \log^3 N)$ | $O(1)$ |
| **Worst** | $O(K \log^3 N)$ | $O(1)$ |

We run K iterations.
In each iteration, `power_mod` takes $O(\log N)$ arithmetic operations.
Squaring the numbers takes $O(\log N)$ arithmetic operations.
If the numbers are massively large (requiring BigInteger objects), each multiplication operation itself takes $O(log^2 N)$ time.
Therefore, total time complexity is $O(K log^3 N)$. If integers fit in 64-bit registers, it simplifies to $O(K log N)$.
Space complexity is $O(1)$.

## Variants & optimizations

- **Deterministic Miller-Rabin:** If N < 2^{64}, you don't need random bases! It has been mathematically proven that you only need to test exactly 7 specific bases: `[2, 3, 5, 7, 11, 13, 17]`. If a number < 2^{64} passes those 7 specific tests, it is 100% mathematically proven to be prime. No randomness or probability required!

## Real-world applications

- **RSA Key Generation:** OpenSSL uses this exact algorithm to generate 2048-bit prime numbers. It randomly guesses an odd 2048-bit number, and runs Miller-Rabin on it. If it fails, it adds 2 and tries again until one survives.

## Related algorithms in cOde(n)

- **[math_03 - Modular Exponentiation](math_03_modular-exponentiation.md)** — The engine that powers the X = A^R \pmod N calculation.
- **[math_02 - Sieve of Eratosthenes](math_02_sieve-of-eratosthenes.md)** — The deterministic array-based alternative when you need ALL primes up to a small N.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
