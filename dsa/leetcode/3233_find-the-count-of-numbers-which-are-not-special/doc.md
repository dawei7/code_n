# Find the Count of Numbers Which Are Not Special

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3233 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-count-of-numbers-which-are-not-special](https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/).

### Goal
Given a range defined by two integers `l` and `r`, determine how many integers in the inclusive interval `[l, r]` are "not special." A number is defined as "special" if it is the square of a prime number. All other numbers in the range are considered "not special."

### Function Contract
**Inputs**

- `l`: An integer representing the start of the range (1 ≤ l ≤ r).
- `r`: An integer representing the end of the range (1 ≤ r ≤ 10^9).

**Return value**

- An integer representing the count of numbers in `[l, r]` that are not the square of a prime number.

### Examples
**Example 1**

- Input: `l = 5, r = 7`
- Output: `3`
- Explanation: The numbers are 5, 6, 7. None are squares of primes (4 is 2^2, 9 is 3^2). All 3 are not special.

**Example 2**

- Input: `l = 4, r = 16`
- Output: `11`
- Explanation: The special numbers are 4 (2^2) and 9 (3^2). Total numbers in range [4, 16] is 13. 13 - 2 = 11.

**Example 3**

- Input: `l = 1, r = 1`
- Output: `1`
- Explanation: 1 is not a square of a prime.

---

## Solution
### Approach
The problem relies on the Sieve of Eratosthenes to identify prime numbers up to the square root of `r` (which is at most 31,622). By precomputing primes, we can identify all "special" numbers (squares of primes) and count how many fall within the range `[l, r]`. The final answer is the total count of numbers in the range `(r - l + 1)` minus the count of special numbers found.

### Complexity Analysis
- **Time Complexity**: `O(sqrt(r) * log(log(sqrt(r))))` due to the Sieve of Eratosthenes up to `sqrt(r)`.
- **Space Complexity**: `O(sqrt(r))` to store the boolean array for the sieve.

### Reference Implementations
<details>
<summary>python</summary>

```python
import bisect
import math


def _build_prime_squares(limit: int = 1_000_000_000) -> list[int]:
    root = math.isqrt(limit)
    is_prime = [True] * (root + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, math.isqrt(root) + 1):
        if is_prime[p]:
            step_start = p * p
            is_prime[step_start : root + 1 : p] = [False] * (((root - step_start) // p) + 1)
    return [p * p for p in range(2, root + 1) if is_prime[p]]


_PRIME_SQUARES = _build_prime_squares()


def solve(l: int, r: int) -> int:
    left = bisect.bisect_left(_PRIME_SQUARES, l)
    right = bisect.bisect_right(_PRIME_SQUARES, r)
    return (r - l + 1) - (right - left)
```
</details>
