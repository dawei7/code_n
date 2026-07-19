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
