# Magical String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 481 |
| Difficulty | Medium |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/magical-string/) |

## Problem Description
### Goal
The magical string begins `122112122122...`, contains only `1` and `2`, and is self-describing: when divided into maximal runs of equal symbols, the sequence of run lengths is the magical string itself. Run symbols alternate between `1` and `2`.

Given a positive prefix length `n`, return how many symbols equal `1` among the first `n` positions. Generate only as much of the sequence as needed, using its already produced run-length entries to extend it. For $n = 1$, the answer is `1`; when the requested prefix ends inside a run, count only symbols whose positions fall within that prefix.

### Function Contract
**Inputs**

- `n`: the prefix length to inspect

**Return value**

- The number of ones in the first `n` symbols of the infinite magical string

### Examples
**Example 1**

- Input: `n = 6`
- Output: `3`

**Example 2**

- Input: `n = 1`
- Output: `1`

**Example 3**

- Input: `n = 0`
- Output: `0`
