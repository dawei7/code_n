# Divide Two Integers Without Division

| | |
|---|---|
| **ID** | `bit_08` |
| **Category** | bit_manipulation |
| **Complexity (required)** | $O(\log N)$ Time, $O(1)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/) |

## Problem statement

Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. Return the quotient after dividing `dividend` by `divisor`.
*Constraint:* Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [-2^{31}, 2^{31} - 1]. If the quotient is strictly greater than 2^{31} - 1, then return 2^{31} - 1.

**Input:** Two integers, `dividend` and `divisor`.
**Output:** An integer representing the quotient.

## When to use it

- The classic "implement basic arithmetic using bits" problem.
- To demonstrate how left-shifting (`<<`) is computationally identical to multiplying by 2, and how repeated subtraction scales logarithmically.

## Approach

**1. The Naive Approach:**
If we want to calculate `10 / 3`, we can just repeatedly subtract `3` from `10` until we drop below `3`.
`10 - 3 = 7` (1 time)
`7 - 3 = 4` (2 times)
`4 - 3 = 1` (3 times). Stop!
Quotient is 3.
This takes $O(N)$ time, where N is the quotient. If we calculate 2^{31} / 1, this will loop two billion times and trigger a Time Limit Exceeded (TLE) error.

**2. The Logarithmic Bit-Shift Optimization:**
Instead of subtracting the divisor 1 at a time, what if we double the divisor rapidly using left-shifts?
We want to subtract the *largest possible multiple of the divisor* from the dividend in a single step!
Example: `dividend = 50`, `divisor = 3`.
- `3 << 0 = 3`
- `3 << 1 = 6`
- `3 << 2 = 12`
- `3 << 3 = 24`
- `3 << 4 = 48`  <-- Largest multiple! We subtract 48 from 50.
Our quotient increases by 2^4 = 16.
Our new `dividend` is 50 - 48 = 2.
Since 2 < 3, we stop. Total quotient is 16. We did this in $O(\log N)$ steps!

**3. Edge Cases & Signs:**
- If the dividend and divisor have different signs, the final quotient must be negative. We can extract the signs, make both numbers strictly positive for the algorithm, and re-apply the sign at the end.
- The 32-bit integer limit constraint is the hardest part. The absolute value of `-2147483648` is `+2147483648`, which OVERFLOWS a signed 32-bit integer! Most standard solutions cheat by using 64-bit longs in Java/C++. The mathematically pure way is to actually convert both numbers to NEGATIVE values, because the negative space has 1 more number of capacity!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bit_08: Divide Without /.

Compute dividend / divisor (integer division) using
"""


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
```

</details>

## Walk-through

`dividend = 29`, `divisor = 3`. Both positive. `quotient = 0`.

1. **Outer Loop 1:** `29 >= 3`.
   - `temp = 3`, `mult = 1`.
   - `29 >= (3<<1=6)`. `temp=6`, `mult=2`.
   - `29 >= (6<<1=12)`. `temp=12`, `mult=4`.
   - `29 >= (12<<1=24)`. `temp=24`, `mult=8`.
   - `29 >= (24<<1=48)` FALSE. Loop ends.
   - `dividend = 29 - 24 = 5`.
   - `quotient = 0 + 8 = 8`.
2. **Outer Loop 2:** `5 >= 3`.
   - `temp = 3`, `mult = 1`.
   - `5 >= (3<<1=6)` FALSE. Loop ends.
   - `dividend = 5 - 3 = 2`.
   - `quotient = 8 + 1 = 9`.
3. **Outer Loop 3:** `2 >= 3` FALSE. Loop ends.

Result `quotient = 9`. ✓ (29 / 3 = 9).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\log N)$ | $O(1)$ |
| **Worst** | $O(\log N)$ | $O(1)$ |

*Where N is the ratio of `dividend` to `divisor`.*
In the absolute worst case (e.g., 2^{31} / 1), the inner loop will shift exactly 31 times, and the outer loop will trigger exactly once. The time complexity is strictly bounded by the number of bits in the integer, making it $O(log(\text{dividend})$), which is effectively an $O(1)$ bound for 32-bit integers.
Space complexity is $O(1)$.

## Variants & optimizations

- **Pure Negative Scaling (No Cheating):** The Python code above uses `abs()`, which conceptually violates strict 32-bit constraints if executed in C/Java (since `abs(-2147483648)` overflows). The pure constraint-compliant solution forces `dividend = -abs(dividend)` and `divisor = -abs(divisor)`, and flips the inner loop logic to `while dividend <= (temp_divisor << 1)`! This guarantees you never overflow the absolute value ceiling.

## Real-world applications

- **Embedded Systems & ALUs:** Extremely low-power microcontrollers (like older PIC or AVR chips) physically lack hardware division circuits (`DIV` instructions) to save silicon space! The compiler translates `/` operations directly into software bit-shifting algorithms exactly like this one.

## Related algorithms in cOde(n)

- **[bit_09 - Multiply Without Multiplication](bit_09_multiply-without.md)** — The exact inverse operation using the same bit-shifting principles.
- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — The logic of jumping by powers of 2 is essentially a continuous binary search across the integer space!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
