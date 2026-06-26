# Pow(x, n) (Fast Exponentiation)

| | |
|---|---|
| **ID** | `dc_01` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(\log N)$ Time, $O(\log N)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Pow(x, n)](https://leetcode.com/problems/powx-n/) |

## Problem statement

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., x^n).

**Input:** A floating-point number `x` and an integer `n`.
**Output:** A floating-point number representing x^n.

## When to use it

- To calculate exponential values securely without hitting an $O(N)$ Time Limit Exceeded (TLE) error.
- It is the absolute foundational algorithm of **Divide and Conquer**, teaching the core concept of halving a problem space mathematically rather than physically.

## Approach

**1. The Flaw of $O(N)$ Multiplication:**
The naive way to calculate 2^{10} is `2 * 2 * 2 ...` (10 times).
If n = 2147483647 (the maximum 32-bit integer), this loop will run 2 billion times and freeze the application!

**2. Divide and Conquer (Exponentiation by Squaring):**
How do we calculate x^{10} faster?
Notice that x^{10} = x^5 x x^5.
If we know x^5, we just multiply it by itself! We cut the workload strictly in half!
But wait, how do we calculate x^5? 5 is an odd number.
x^5 = x^2 x x^2 x x.
By continuously cutting the exponent in half, we drop the number of required multiplications from N down to log_2(N)!
Calculating 2^{2147483647} now takes exactly **31 operations** instead of 2 billion!

**3. The Recursive Rules:**
- **Base Case:** If n == 0, return `1.0`. (Anything to the power of 0 is 1).
- **Even Exponent:** If n is even, x^n = (x^{n/2}) x (x^{n/2}).
- **Odd Exponent:** If n is odd, x^n = x x (x^{(n-1)/2}) x (x^{(n-1)/2}).

**4. Edge Cases:**
- What if n is negative? (e.g., 2^{-3}).
  A negative exponent just means taking the reciprocal! x^{-n} = 1 / x^n.
  So if n < 0, we just recursively calculate `pow(x, -n)` and return `1.0 / result`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_01: Power(x, n).

Recursive halving: x^n = (x^(n//2))^2, with an extra x when
n is odd. Handle negative n by computing the reciprocal. O(log n).
"""


def solve(x, n):
    if n == 0:
        return 1
    # Use absolute exponent, then take reciprocal at the end if needed.
    abs_n = -n if n < 0 else n
    result = 1.0
    base = float(x)
    while abs_n > 0:
        if abs_n & 1:
            result *= base
        abs_n >>= 1
        if abs_n:
            base *= base
    if n < 0:
        return 1.0 / result
    return result
```

</details>

## Walk-through

`x = 2.0`, `n = 5`.

1. `fast_pow(2.0, 5)`:
   - `exp` is odd (5).
   - `half = fast_pow(2.0, 2)`:
     - `exp` is even (2).
     - `half = fast_pow(2.0, 1)`:
       - `exp` is odd (1).
       - `half = fast_pow(2.0, 0)` -> **Returns 1.0 (Base Case)**
       - Back to `exp=1`: returns `1.0 * 1.0 * 2.0` -> **Returns 2.0**
     - Back to `exp=2`: returns `2.0 * 2.0` -> **Returns 4.0**
   - Back to `exp=5`: returns `4.0 * 4.0 * 2.0` -> **Returns 32.0**

Result is `32.0`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(\log N)$ | $O(\log N)$ |
| **Average** | $O(\log N)$ | $O(\log N)$ |
| **Worst** | $O(\log N)$ | $O(\log N)$ |

*Where N is the exponent.*
At each step, the exponent is divided by 2 (integer division). The recursion bottoms out when N=0. Thus, there are exactly log_2(N) recursive calls.
Time complexity is $O(\log N)$.
Space complexity is $O(\log N)$ due to the depth of the recursive call stack.

## Variants & optimizations

- **Iterative Approach (Bit Manipulation):** You can completely eliminate the recursive call stack (dropping Space to $O(1)$) by using the exact same logic as Russian Peasant Multiplication (`bit_09`)! Just convert `n` to binary. `while n > 0`, if `n & 1 == 1`, multiply your `result` by `x`. Then blindly square `x` (`x = x * x`) and right-shift `n` (`n >>= 1`). This is the industry-standard way math libraries implement `pow()`.
- **Modular Exponentiation:** If the problem asks for `pow(x, n) % M` (because the answer is too massive to fit in memory), simply apply the modulo operator at EVERY multiplication step! `half = (half * half) % M`.

## Real-world applications

- **RSA Cryptography:** Encrypting and decrypting messages requires computing C = M^e \pmod N. Since the encryption key e is often a massive 2048-bit integer, calculating M to the power of a 2048-bit number naively is physically impossible before the heat death of the universe. Fast Exponentiation computes it in milliseconds.

## Related algorithms in cOde(n)

- **[bit_09 - Multiply Without Multiplication](../bit_manipulation/bit_09_multiply-without.md)** — The exact same "halving" logic applied to addition instead of multiplication.
- **[math_02 - Modular Arithmetic](../math/math_02_modular-arithmetic.md)** — How to apply this algorithm when constrained by a modulo.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
