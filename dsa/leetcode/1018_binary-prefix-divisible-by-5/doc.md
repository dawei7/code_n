# Binary Prefix Divisible By 5

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1018 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/binary-prefix-divisible-by-5/) |

## Problem Description

### Goal

You are given a 0-indexed binary array `nums`. For every index `i`, let $x_i$ be the integer whose binary representation is the prefix `nums[0..i]`, read from most-significant bit to least-significant bit.

Return a boolean array `answer` of the same length, where `answer[i]` is `true` exactly when $x_i$ is divisible by `5`. Leading zeroes in a prefix do not change its numeric value; for example, the prefixes of `[0, 1, 1]` represent `0`, `1`, and `3`.

### Function Contract

**Inputs**

- `nums`: a binary array of length $N$, where $1\le N\le10^5$ and every element is `0` or `1`.

**Return value**

- An $N$-element boolean array reporting divisibility by `5` for each binary prefix.

### Examples

**Example 1**

- Input: `nums = [0, 1, 1]`
- Output: `[True, False, False]`
- Explanation: The prefixes represent `0`, `1`, and `3`; only zero is divisible by `5`.

**Example 2**

- Input: `nums = [1, 1, 1]`
- Output: `[False, False, False]`
- Explanation: The prefixes represent `1`, `3`, and `7`.

**Example 3**

- Input: `nums = [1, 0, 1, 0]`
- Output: `[False, False, True, True]`
- Explanation: The final two prefixes represent `5` and `10`.
