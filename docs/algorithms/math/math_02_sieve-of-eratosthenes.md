# Sieve of Eratosthenes

| | |
|---|---|
| **ID** | `math_02` |
| **Category** | math |
| **Complexity (required)** | $O(N log(log N)$) Time, $O(N)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Count Primes](https://leetcode.com/problems/count-primes/) |

## Problem statement

Given an integer `N`. Find all prime numbers strictly less than or equal to `N`.
A prime number is a natural number strictly greater than 1 that cannot be formed by multiplying two smaller natural numbers.

**Input:** An integer `N`.
**Output:** A list of all prime numbers \le N.

## When to use it

- When you need to rapidly pre-compute a lookup table of prime numbers to process multiple queries in $O(1)$ time.
- Standard brute-force checking $O(\sqrt{N})$ for every number takes $O(N \sqrt{N})$ time. The Sieve does the same task for the entire array almost in linear time!

## Approach

**1. The Cross-Out Strategy:**
Instead of mathematically checking if a specific number X is prime, we work backward!
We know that `2` is a prime number. Therefore, every single multiple of `2` (`4, 6, 8, 10...`) is mathematically guaranteed NOT to be prime!
We can just go through an array of numbers and cross out all the multiples of 2.
Then we move to the next non-crossed-out number (`3`). It must be prime! We cross out all multiples of `3` (`6, 9, 12...`).
We move to the next non-crossed-out number (`5` because `4` was already crossed out by `2`!). We cross out all its multiples.

**2. The Optimization (\sqrt{N} Limit):**
Do we need to keep crossing out multiples until we reach N?
No! If N = 100, the square root is 10.
If we reach the number `11`, its first multiple that hasn't already been crossed out by a smaller prime would be 11 x 11 = 121. But 121 is greater than 100!
Therefore, we only need to cross out multiples for prime numbers up to \lfloor\sqrt{N}\rfloor. Any number left uncrossed in the entire array after that is guaranteed to be a prime!

**3. The Algorithm:**
1. Create a boolean array `is_prime` of size N+1, initialized to `True`.
2. Set `is_prime[0] = False` and `is_prime[1] = False`.
3. Loop `p` from `2` up to \sqrt{N}.
4. If `is_prime[p]` is `True`:
   - It's a prime! Cross out all its multiples.
   - Start a nested loop `i` at p x p (because all smaller multiples like p x 2 or p x 3 were already crossed out by 2 and 3!).
   - Increment `i` by p until N. Set `is_prime[i] = False`.
5. After the loop, return the indices of the array that are still `True`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
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
```

</details>

## Walk-through

`N = 20`. `limit = floor(sqrt(20)) = 4`.
Initial array: `[F, F, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T]`

1. `p = 2`:
   - `is_prime[2]` is True.
   - Start loop at `2 * 2 = 4`. Step by 2.
   - Cross out `4, 6, 8, 10, 12, 14, 16, 18, 20`.
2. `p = 3`:
   - `is_prime[3]` is True.
   - Start loop at `3 * 3 = 9`. Step by 3.
   - Cross out `9`. (`12` is already crossed). Cross out `15`. (`18` is already crossed).
3. `p = 4`:
   - `is_prime[4]` is False! (Crossed out by 2). Skip!
4. Loop ends (since `p > 4`).

Remaining Trues: `2, 3, 5, 7, 11, 13, 17, 19`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log(\log N)$) | $O(N)$ |
| **Average** | $O(N \log(\log N)$) | $O(N)$ |
| **Worst** | $O(N \log(\log N)$) | $O(N)$ |

The outer loop runs \sqrt{N} times. The inner loop runs \frac{N}{2} times for 2, \frac{N}{3} times for 3, \frac{N}{5} times for 5, etc.
The total number of inner loop executions is exactly N x (\frac{1}{2} + \frac{1}{3} + \frac{1}{5} + \frac{1}{7} + ...).
This is the Harmonic Series of Primes, which mathematically bounds to $O(log(log N)$).
Therefore, the total time complexity is $O(N log(log N)$). This is so incredibly close to $O(N)$ linear time that for N=1,000,000, log(log(10^6)) ~= 2.6.
Space complexity is strictly $O(N)$ for the boolean array.

## Variants & optimizations

- **Segmented Sieve:** If N is massive (e.g., 10^9), an array of 10^9 booleans takes 1 Gigabyte of RAM and causes massive CPU Cache misses. The Segmented Sieve computes the primes up to \sqrt{N} first, and then processes the remaining range in small, cache-friendly chunks of size 10^5, severely reducing memory footprint to $O(\sqrt{N})$.
- **Smallest Prime Factor (SPF) Sieve:** Instead of storing `True/False`, store the integer value of the prime that crossed it out! `spf[15] = 3`. This modified sieve allows you to mathematically Prime Factorize ANY number in the array in $O(\log N)$ time by just following the pointers down to 1!

## Real-world applications

- **Cryptography Generation:** Generating the candidate pool of massive prime numbers to be tested and used as the secret keys P and Q in RSA encryption algorithms.

## Related algorithms in cOde(n)

- **[math_09 - Miller-Rabin Primality Test](math_09_miller-rabin-primality-test.md)** — The alternative algorithm used when you just need to check if one single MASSIVE number is prime (e.g. 10^{100}), where creating an array of size N is physically impossible.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
