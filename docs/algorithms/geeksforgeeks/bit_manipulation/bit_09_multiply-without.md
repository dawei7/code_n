# Multiply Two Integers Without Multiplication (Russian Peasant)

| | |
|---|---|
| **ID** | `bit_09` |
| **Category** | bit_manipulation |
| **Complexity (required)** | $O(\log N)$ Time, $O(1)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 5/10 |
| **GeeksForGeeks Equivalent** | [Russian Peasant Multiplication](https://www.geeksforgeeks.org/russian-peasant-multiply-two-numbers-using-bitwise-operators/) |

## Problem statement

Given two integers `a` and `b`, multiply them without using the `*` operator.
You may use addition, subtraction, and bitwise operators.

**Input:** Two integers `a` and `b`.
**Output:** An integer representing `a * b`.

## When to use it

- A classic bit-manipulation brainteaser often referred to as **Russian Peasant Multiplication** or **Ancient Egyptian Multiplication**.
- Demonstrates how mathematical multiplication is physically implemented in hardware ALUs using bit shifts and adders.

## Approach

**1. The Mathematical Foundation:**
Multiplication is just repeated addition. a x b means adding a to itself b times.
If b = 13, then a x 13 = a + a + a \dots (13 times). This is $O(b)$ operations.
But we can decompose b into powers of 2 (Binary representation)!
13 in binary is `1101` (8 + 4 + 1).
Therefore, a x 13 = a x (8 + 4 + 1) = (a x 8) + (a x 4) + (a x 1).

**2. The Bitwise Shift:**
How do we multiply a by 8? We just left-shift it 3 times! `a << 3`.
How do we know WHICH powers of 2 to add? We just look at the binary bits of b!
If the lowest bit of b is `1`, we add our current scaled a to the total result.
Then we physically chop off the lowest bit of b by right-shifting (`b >> 1`), and simultaneously double a by left-shifting (`a << 1`).
We repeat this until b reaches 0.

**3. Edge Cases & Signs:**
Just like Division (`bit_08`), if the numbers have different signs, the result is negative. We strip the signs, do the bitwise logic on positive numbers, and re-apply the sign at the end.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bit_09: Multiply Without *.

Compute a * b using only addition and shifts. For
"""


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
```

</details>

## Walk-through

`a = 5`, `b = 13`. (`13` is `1101`).

1. **Loop 1:** `b = 13`.
   - `b & 1` -> `13 & 1 == 1`. True!
   - `result += 5`. `result = 5`.
   - `a = 5 << 1 = 10`.
   - `b = 13 >> 1 = 6` (`0110`).
2. **Loop 2:** `b = 6`.
   - `b & 1` -> `6 & 1 == 0`. False!
   - `result = 5`.
   - `a = 10 << 1 = 20`.
   - `b = 6 >> 1 = 3` (`0011`).
3. **Loop 3:** `b = 3`.
   - `b & 1` -> `3 & 1 == 1`. True!
   - `result += 20`. `result = 25`.
   - `a = 20 << 1 = 40`.
   - `b = 3 >> 1 = 1` (`0001`).
4. **Loop 4:** `b = 1`.
   - `b & 1` -> `1 & 1 == 1`. True!
   - `result += 40`. `result = 65`.
   - `a = 40 << 1 = 80`.
   - `b = 1 >> 1 = 0`.
5. **Loop 5:** `b = 0`. Terminate.

Result is `65`. ✓ (5 x 13 = 65).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(log B)$ | $O(1)$ |
| **Worst** | $O(log B)$ | $O(1)$ |

*Where B is the value of the multiplier.*
The `while` loop runs exactly as many times as there are bits in `b`. If `b` is a 32-bit integer, the loop runs at most 32 times. This makes the time complexity logarithmically bounded $O(log B)$, effectively $O(1)$ for fixed-width integers.
Space complexity is strictly $O(1)$.

## Variants & optimizations

- **Optimized Choice of Multiplier:** Since a x b = b x a, the algorithm runs significantly faster if the `while` loop is bound to the SMALLER of the two numbers! E.g. 10000 x 2 takes 2 iterations if b=2, but 14 iterations if b=10000. Just add `if a < b: a, b = b, a` at the start!

## Real-world applications

- **Cryptography (Modular Exponentiation):** When performing RSA encryption, you must calculate incredibly massive exponents like x^{1024} \pmod N. You cannot multiply x by itself 1024 times. The "Exponentiation by Squaring" algorithm used to solve this is mathematically IDENTICAL to Russian Peasant Multiplication, just swapping `+` for `*`, and `*` for `^`!

## Related algorithms in cOde(n)

- **[bit_08 - Divide Without Division](bit_08_divide-without.md)** — The inverse operation using identical scaling logic.
- **[math_02 - Fast Exponentiation](../math/math_02_fast-exponentiation.md)** — The exact same algorithm applied to powers instead of multiplication.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
