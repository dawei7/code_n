# Complement of Base 10 Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1009 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/complement-of-base-10-integer/) |

## Problem Description

### Goal

The complement of an integer is obtained from its binary representation by changing every `0` bit to `1` and every `1` bit to `0`. Only the written representation is complemented; leading zeroes outside its significant bits are not included.

Given a nonnegative integer `n`, return the base-10 value of its complement. For example, `5` is written as `101`, whose complement is `010`, representing `2`. The representation of zero is the single bit `0`, so its complement is `1`.

### Function Contract

**Inputs**

- `n`: an integer satisfying $0\le n<10^9$.

Let $B$ be the number of bits in the standard binary representation of `n`, taking $B=1$ when `n == 0`.

**Return value**

- The integer represented after flipping all $B$ bits of `n`.

### Examples

**Example 1**

- Input: `n = 5`
- Output: `2`
- Explanation: `101` becomes `010`.

**Example 2**

- Input: `n = 7`
- Output: `0`
- Explanation: `111` becomes `000`.

**Example 3**

- Input: `n = 10`
- Output: `5`
- Explanation: `1010` becomes `0101`.
