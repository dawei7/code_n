# Minimum Flips to Make a OR b Equal to c

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1318 |
| Difficulty | Medium |
| Topics | Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/) |

## Problem Description
### Goal
Given three positive integers `a`, `b`, and `c`, change individual bits in the binary representations of `a` and `b` until their bitwise OR equals `c`. A flip changes one selected bit from 0 to 1 or from 1 to 0.

Return the minimum number of flips needed to satisfy `(a | b) == c`. Bits may be changed in either input integer, and each changed position in each integer counts as one flip.

### Function Contract
**Inputs**

- `a`: a positive integer with $1\le a\le10^9$.
- `b`: a positive integer with $1\le b\le10^9$.
- `c`: a positive integer with $1\le c\le10^9$.

Let $M=\max(a,b,c)$.

**Return value**

The minimum number of individual bit flips in `a` and `b` required to make their bitwise OR equal `c`.

### Examples
**Example 1**

- Input: `a = 2, b = 6, c = 5`
- Output: `3`
- Explanation: Three bit changes can produce values 1 and 4, whose OR is 5.

**Example 2**

- Input: `a = 4, b = 2, c = 7`
- Output: `1`
- Explanation: The low bit is absent from both inputs, so one of them must gain it.

**Example 3**

- Input: `a = 1, b = 2, c = 3`
- Output: `0`
- Explanation: The current OR is already 3.

### Required Complexity
- **Time:** $O(\log M)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Treat each bit position independently**

Bitwise OR has no carry between positions. At one position, let `a_bit`, `b_bit`, and `c_bit` be the corresponding bits. Choices made there cannot affect any other position, so an optimal global answer is the sum of the minimum costs for the individual positions.

**Count the forced changes**

If `c_bit` is 0, both input bits must end as 0. The local cost is therefore `a_bit + b_bit`: each present 1 must be cleared.

If `c_bit` is 1, at least one input bit must end as 1. The cost is 0 when either input bit is already 1, and otherwise exactly 1 because either zero can be flipped. These are all possible three-bit configurations, so summing their local optima gives the minimum total.

Process the least-significant bits, shift all three values right, and continue until every remaining value is zero. This includes leading positions that occur in only one of the three original values.

#### Complexity detail

The loop examines one position for each bit of $M$, or $O(\log M)$ positions. It stores only the shifted integers, their current bits, and the running total, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Bit-count identity:** Masks for unwanted 1s and missing 1s can be combined with population counts for a compact solution, but the per-bit cases make the minimum argument more explicit.
- **Binary strings:** Padding three strings to the same length also works in $O(\log M)$ time but allocates $O(\log M)$ additional space.
- **Target bit 0 with two input 1s:** Both 1s must be cleared, so that position contributes 2 rather than 1.
- **Target bit 1 with two input 0s:** Flipping either input is sufficient, so the position contributes exactly 1.
- **Already equal:** If `a | b` is `c`, every bit contributes 0.
- **Different bit lengths:** Continue through bits present in any of the three values; stopping when only one shifted value becomes zero would miss required changes.

</details>
