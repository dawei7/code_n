# Power of Four

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 342 |
| Difficulty | Easy |
| Topics | Math, Bit Manipulation, Recursion |
| Official Link | [LeetCode](https://leetcode.com/problems/power-of-four/) |

## Problem Description
### Goal
Given a signed 32-bit integer `n`, determine whether it can be written exactly as $4^{x}$ for an integer exponent $x \ge 0$. Valid values begin with $1 = 4^{0}$, then `4`, `16`, `64`, and continue by repeated multiplication by four.

Return `True` only for positive exact powers of four. Return `False` for zero, negative values, powers of two whose single set bit lies at an odd binary position, and all other integers. The task asks for a boolean rather than the exponent. Meet the follow-up without loops or recursion by using fixed-width arithmetic properties where required.

### Function Contract
**Inputs**

- `n`: the integer to classify

**Return value**

- `True` if `n` is an exact non-negative integer power of four; otherwise `False`.

### Examples
**Example 1**

- Input: `n = 16`
- Output: `True`

**Example 2**

- Input: `n = 5`
- Output: `False`

**Example 3**

- Input: `n = 1`
- Output: `True`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**First isolate powers of two**

Every power of four is also a power of two, but only every second power of two qualifies:

$4^{x} = 2^{(2x)}$.

First require $n > 0$. A positive power of two has exactly one set bit, which is recognized by $n \mathbin{\&} (n - 1) = 0$: subtracting one changes that lone `1` and all lower zeros, so the bitwise AND clears everything. This test alone would also accept `2`, `8`, and other powers of two with odd exponents.

**Then keep only even bit positions**

Number bit positions from zero at the least-significant bit. Powers of four place their only set bit at positions `0, 2, 4, ..., 30`. Within the signed 32-bit domain, hexadecimal mask `0x55555555` has `1` bits at precisely those even positions. Requiring `n & 0x55555555 != 0` therefore distinguishes powers of four from the remaining powers of two.

**Why the three filters are exact**

The three conditions are jointly sufficient. Positivity excludes zero and negatives; the one-bit test proves $n = 2^{p}$; and the mask proves that `p` is even. Hence $n = 2^{(2x)} = 4^{x}$. They are also necessary because every valid power of four is positive and has exactly one bit in an even position.

**Check the domain boundaries**

The value `1` is accepted: it is $4^{0}$ and its bit occupies position zero. The largest valid signed-32-bit value is $4^{15} = 2^{30} = 1,073,741,824$, whose set bit is also covered by the mask.

#### Complexity detail

The input width is fixed at 32 bits. The method performs a constant number of comparisons and bitwise operations, so it takes $O(1)$ time and $O(1)$ space.

#### Alternatives and edge cases

- **Repeated division by four:** is exact and easy to follow but takes $O(\log_{4} n)$ iterations.
- **Logarithm test:** is compact but risks floating-point rounding near integer exponents.
- **Modulo-three identity:** combines the power-of-two test with $n \bmod 3 = 1$ in constant time, although the bit-position mask expresses the structural reason more directly.
- Zero and negative integers are always false.
- Powers of two such as `2` or $2^{29}$ are counterexamples to the one-bit test alone because their set bit occupies an odd position.

</details>
