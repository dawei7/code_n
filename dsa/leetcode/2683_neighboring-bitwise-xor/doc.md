# Neighboring Bitwise XOR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2683 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/neighboring-bitwise-xor/) |

## Problem Description

### Goal

A 0-indexed binary array `derived` was formed from a binary array `original` of the same length by XOR-ing neighboring values around a circle. For every index except the last, `derived[i] = original[i] ^ original[i + 1]`. The final entry closes the circle with `derived[n - 1] = original[n - 1] ^ original[0]`.

Given `derived`, determine whether at least one valid binary array `original` could have produced it. A binary array contains only zeros and ones.

### Function Contract

**Inputs**

- `derived`: A binary list of length $n$, where $1 \leq n \leq 10^5$.

**Return value**

Return `True` if some binary `original` satisfies every circular neighboring-XOR equation; otherwise return `False`.

### Examples

#### Example 1

- **Input:** `derived = [1,1,0]`
- **Output:** `true`
- **Explanation:** `original = [0,1,0]` produces the three required XOR values.

#### Example 2

- **Input:** `derived = [1,1]`
- **Output:** `true`
- **Explanation:** `original = [0,1]` produces both entries.

#### Example 3

- **Input:** `derived = [1,0]`
- **Output:** `false`
