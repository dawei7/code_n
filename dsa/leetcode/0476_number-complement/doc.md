# Number Complement

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 476 |
| Difficulty | Easy |
| Topics | Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/number-complement/) |

## Problem Description
### Goal
Given a positive integer `num`, write its binary representation without leading zeroes. Form its complement by changing every significant `0` bit to `1` and every significant `1` bit to `0`, from the highest set-bit position through the least significant bit.

Return the integer represented by that complemented bit sequence. Do not flip an unlimited supply of leading zeroes or apply a fixed signed-width complement, because those bits are outside the original representation. For example, a leading `1` always becomes `0` and may disappear when the result is written numerically. The input is strictly positive.

### Function Contract
**Inputs**

- `num`: a positive integer

**Return value**

- The integer represented by complementing only the significant binary bits of `num`

### Examples
**Example 1**

- Input: `num = 5`
- Output: `2`

**Example 2**

- Input: `num = 1`
- Output: `0`

**Example 3**

- Input: `num = 10`
- Output: `5`

### Required Complexity

- **Time:** $O(\log num)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Restrict inversion to significant bits**

An unrestricted bitwise NOT also flips infinitely many leading zeros in Python or the full machine word in fixed-width languages. Instead determine the number of significant bits `b` and construct a mask with exactly those low `b` bits set: $(1 \ll b) - 1$.

**XOR with an all-ones mask**

XOR flips a bit wherever the mask contains one. The mask covers every bit in the representation and no leading positions, so `num ^ mask` is exactly the requested complement.

**Why the result has no spurious leading bits**

All mask positions above the highest set bit are zero and leave the implicit leading zeros unchanged. Within the mask, every original zero becomes one and every original one becomes zero, including the leading one becoming a harmless leading zero in the result.

#### Complexity detail

For bit width $b = O(\log num)$, determining or constructing the mask requires at most $O(b)$ conceptual bit work; fixed-width machine operations are constant bounded. The algorithm stores only the mask, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Build the mask by shifting:** repeatedly append one bits until the mask exceeds `num`, then XOR; this is also linear in bit width.
- **Inspect and rebuild each output bit:** works but is more verbose and can repeat shifts if masks are reconstructed from scratch.
- **Binary-string translation:** is easy to visualize but allocates strings and parses the result.
- **`num = 1`:** its sole bit flips to zero.
- **Power of two:** the leading one becomes zero and every lower zero becomes one.
- **All significant bits already one:** the complement is zero.
- **Leading zeros:** are not part of the representation and must not be flipped.

</details>
