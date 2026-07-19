# Binary Number with Alternating Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 693 |
| Difficulty | Easy |
| Topics | Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-number-with-alternating-bits/) |

## Problem Description
### Goal
Given a positive integer `n`, inspect its binary representation without leading zeroes. It has alternating bits when every pair of adjacent bit positions contains different values, so each `0` is next to `1` and each `1` is next to `0` wherever a neighbor exists.

Return `True` if all adjacent bits alternate and `False` otherwise. A one-bit representation is valid because it has no adjacent pair that violates the condition; any occurrence of `00` or `11` makes a longer representation invalid.

### Function Contract
**Inputs**

- `n`: a positive integer

**Return value**

- `true` when the ordinary binary representation of `n` alternates between `0` and `1`; otherwise `false`

### Examples
**Example 1**

- Input: `n = 5`
- Output: `true`
- Explanation: `5` is `101` in binary.

**Example 2**

- Input: `n = 7`
- Output: `false`
- Explanation: `7` is `111`, which contains equal adjacent bits.

**Example 3**

- Input: `n = 11`
- Output: `false`
- Explanation: `11` is `1011`; its two least-significant bits are both `1`.
