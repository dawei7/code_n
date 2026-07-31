# Factorial Generator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2803 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/factorial-generator/) |

## Problem Description

### Goal

Write a JavaScript generator function that accepts a nonnegative integer `n` and yields the factorial sequence through `n!`. For positive `n`, the sequence contains `1!`, `2!`, and every subsequent factorial up to `n!`, in that order. Each value is produced on the next advancement of the generator.

Factorial multiplication follows $i! = i \cdot (i - 1)!$. The special input `n = 0` must still yield one value, because $0!$ is defined as $1$; for positive inputs, do not emit a separate `0!` entry before `1!`.

### Function Contract

**Inputs**

- `n`: The final factorial index, with $0 \le n \le 18$.

**Return value**

Return a generator object. When fully consumed, it yields `[1!, 2!, ..., n!]` for positive `n`, or the single value `[1]` when `n = 0`.

### Examples

**Example 1**

- Input: `n = 5`
- Output: `[1, 2, 6, 24, 120]`
- Explanation: Consecutive generator advances produce `1!` through `5!`.

**Example 2**

- Input: `n = 2`
- Output: `[1, 2]`
- Explanation: The generator yields `1!`, followed by `2!`.

**Example 3**

- Input: `n = 0`
- Output: `[1]`
- Explanation: The sole yielded value is `0!`.
