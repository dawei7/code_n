# Euler's Totient Function

| | |
|---|---|
| **ID** | `math_10` |
| **Category** | math |
| **Complexity (required)** | $O(\sqrt{N})$ Time, $O(1)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 3/10 |
| **Wikipedia** | [Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function) |

## Problem statement

Given a positive integer `N`. Calculate Euler's Totient Function, denoted as \phi(N) or \text{phi}(N).
The Totient function counts the number of integers from 1 to N that are coprime to N.
(Two numbers are coprime if their Greatest Common Divisor is 1).

**Input:** An integer `N`.
**Output:** An integer representing \phi(N).

## When to use it

- Calculating the number of possible Modular Multiplicative Inverses for a given modulo.
- The fundamental theorem backing RSA public-key encryption.

## Approach

**1. The Brute Force:**
You could just loop from i=1 to N, run the GCD algorithm `math_01(i, N)`, and increment a counter if the result is 1. This takes $O(N \log N)$ time, which is far too slow for N=10^{12}.

**2. The Mathematical Formula:**
Euler discovered a direct formula using Prime Factorization.
If p_1, p_2, \dots, p_k are the unique prime factors of N, then:
$\phi(N) = N \cdot \left(1 - \frac{1}{p_1}\right) \cdot \left(1 - \frac{1}{p_2}\right) \cdots \left(1 - \frac{1}{p_k}\right)

Why does this work?
Start with N total numbers.
If `2` is a prime factor, exactly \frac{1}{2} of all numbers up to N are divisible by 2. We throw them away! We are left with N \cdot (1 - \frac{1}{2}).
If `3` is a prime factor, exactly \frac{1}{3} of the *remaining* numbers are divisible by 3. Throw them away! Multiply the remainder by (1 - \frac{1}{3}).
We simply strip away the multiples of every prime factor.

**3. The Algorithm:**
We don't need a separate array of prime numbers! We just do standard Prime Factorization.
1. Initialize `result = N`.
2. Loop `p` starting from 2 up to \sqrt{N}.
3. If N \pmod p == 0, then p is a prime factor!
   - Apply Euler's formula to our result: `result = result - (result // p)`. (This is mathematically identical to result \cdot (1 - \frac{1}{p}) but prevents floating point precision errors).
   - Divide N by p as many times as possible to completely strip this prime factor out of the number (just like standard factorization).
4. After the loop, if the remaining N is > 1, it means the final remaining piece is a prime number itself! We apply the formula one last time for this final prime factor.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for math_10: Euler Totient Function.

Given a positive integer n, return phi(n): the
"""


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
```

</details>

## Walk-through

`N = 12`. `result = 12`.

1. `p = 2`:
   - 2 \times 2 \le 12.
   - `12 % 2 == 0`. We found a prime factor!
   - `result -= 12 // 2` \implies `result = 12 - 6 = 6`.
   - Strip `2` from `N`: `12 // 2 = 6`, `6 // 2 = 3`. Now `n = 3`.
2. `p = 3`:
   - 3 \times 3 \not\le 3. Loop terminates!
3. Final check: `n = 3`. `3 > 1` is True!
   - We must process the final prime factor `3`.
   - `result -= 6 // 3` \implies `result = 6 - 2 = 4`.

Result: `4`. ✓
*(Verification: The numbers from 1 to 12 coprime to 12 are `1, 5, 7, 11`. Exactly 4 numbers!)*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(\log N)$ | $O(1)$ |
| **Average** | $O(\sqrt{N})$ | $O(1)$ |
| **Worst** | $O(\sqrt{N})$ | $O(1)$ |

The `while` loop runs up to \sqrt{N}. If N is a prime number, it takes exactly \sqrt{N} iterations. If N is highly composite (e.g. 2^{30}), the inner `while` loop instantly reduces N to 1 in $O(\log N)$ time. Therefore, the worst-case time complexity is bounded by $O(\sqrt{N})$.
Space complexity is strictly $O(1)$ constant time as we only track three integer variables (`n`, `result`, `p`).

## Variants & optimizations

- **Computing 1 to N (Sieve Method):** If a problem requires you to calculate the Totient for *every* number from 1 to 10^5, calling $O(\sqrt{N})$ in a loop takes $O(N \sqrt{N})$ time. You can optimize this to $O(N \log(\log N)$) using an array exactly like the Sieve of Eratosthenes (`math_02`). You initialize `phi[i] = i`, and when you find a prime, you iterate through its multiples M and do `phi[M] -= phi[M] // p`.
- **Carmichael Function (`math_06`):** The advanced variation of the Totient function that finds the smallest possible exponent rather than the guaranteed Euler exponent.

## Real-world applications

- **RSA Cryptography:** To generate an RSA keypair, you pick two massive primes P and Q. You compute N = P \times Q. You then explicitly need to compute Euler's Totient of N: \phi(N) = (P-1)(Q-1). This \phi(N)$ value is used to generate the public and private encryption keys!

## Related algorithms in cOde(n)

- **[math_06 - Carmichael Function](math_06_carmichael-function.md)** — The mathematically superior but much more complex alternative to the Totient function.
- **[math_02 - Sieve of Eratosthenes](math_02_sieve-of-eratosthenes.md)** — The optimal strategy for calculating Totients in bulk.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
