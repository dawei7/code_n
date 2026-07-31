# Check Balanced String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3340 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-balanced-string/) |

## Problem Description

### Goal

You are given a string `num` containing only decimal digits. Using zero-based indices, add the numeric values of the digits at even indices and separately add those at odd indices.

The string is balanced exactly when these two sums are equal. Return `true` for a balanced string and `false` otherwise. Leading zeroes remain ordinary digits and do not change the indexing.

### Function Contract

**Inputs**

- `num`: A digit-only string of length $n$, where $2 \le n \le 100$.

**Return value**

- `True` when the sum at indices $0,2,4,\ldots$ equals the sum at indices $1,3,5,\ldots$; otherwise `False`.

### Examples

**Example 1**

- Input: `num = "1234"`
- Output: `false`
- Explanation: Even indices sum to $1+3=4$, while odd indices sum to $2+4=6$.

**Example 2**

- Input: `num = "24123"`
- Output: `true`
- Explanation: Even indices sum to $2+1+3=6$, and odd indices sum to $4+2=6$.
