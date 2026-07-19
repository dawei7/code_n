# Binary Gap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 868 |
| Difficulty | Easy |
| Topics | Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-gap/) |

## Problem Description
### Goal
Given a positive integer `n`, examine the `1` bits in its binary representation and return the greatest distance between two adjacent `1` bits. Two `1` bits are adjacent in this sense when every bit strictly between them is `0`; consecutive `1` bits with no separating zero also form an adjacent pair.

The distance is the absolute difference between the two bit positions. For example, the `1` bits in binary `1001` are three positions apart. If the representation contains fewer than two `1` bits and therefore has no adjacent pair, return `0`.

### Function Contract
**Inputs**

- `n`: a positive integer where $1 \leq n \leq 10^9$.

Let $L=\lfloor\log_2 n\rfloor+1$ be the number of bits in the binary representation without leading zeros.

**Return value**

Return the maximum difference between the positions of consecutive `1` bits when all set-bit positions are listed in order, or `0` if fewer than two exist.

### Examples
**Example 1**

- Input: `n = 22`
- Output: `2`

Binary `10110` has consecutive set-bit gaps `2` and `1`. The outside pair is not adjacent because another `1` lies between it.

**Example 2**

- Input: `n = 8`
- Output: `0`

Binary `1000` contains only one `1`.

**Example 3**

- Input: `n = 5`
- Output: `2`

Binary `101` has one adjacent pair whose positions differ by `2`.
