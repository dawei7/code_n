# Number of Even and Odd Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2595 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-even-and-odd-bits/) |

## Problem Description

### Goal

You are given a positive integer `n`. Consider its binary representation with bit positions numbered from right to left, beginning at index zero.

An index is classified by its ordinary parity: `0`, `2`, `4`, and so on are even, while `1`, `3`, `5`, and so on are odd. Only positions whose binary digit is `1` contribute; zero bits are ignored.

Count the set bits at even indices and the set bits at odd indices. Return those two counts in the order `[even, odd]`.

### Function Contract

**Inputs**

- `n`: A positive integer satisfying $1 \leq n \leq 1000$.

**Return value**

- A two-element list whose first value is the number of set bits at even indices and whose second value is the number at odd indices.

### Examples

**Example 1**

- Input: `n = 50`
- Output: `[1,2]`

The binary representation is `110010`, whose set bits are at indices `1`, `4`, and `5`. Index `4` is even, while indices `1` and `5` are odd.

**Example 2**

- Input: `n = 2`
- Output: `[0,1]`

The binary representation is `10`, so its only set bit is at odd index `1`.
