# Get Equal Substrings Within Budget

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1208 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/get-equal-substrings-within-budget/) |

## Problem Description

### Goal

You are given lowercase English strings `s` and `t` of the same length, together with an integer `maxCost`. Changing `s[i]` into the corresponding character `t[i]` costs the absolute difference between their ASCII values, $\lvert\operatorname{ord}(\texttt{s[i]})-\operatorname{ord}(\texttt{t[i]})\rvert$.

Choose one contiguous substring of `s` and change all of its characters to match the substring at the same indices in `t`. Return the maximum possible substring length whose total conversion cost is at most `maxCost`. If no nonempty corresponding substring is affordable, return 0.

### Function Contract

**Inputs**

- `s` and `t`: Lowercase English strings of equal length $n$, where $1\le n\le10^5$.
- `maxCost`: The available conversion budget, where $0\le\texttt{maxCost}\le10^6$.

**Return value**

- The greatest length of a contiguous index interval whose character-conversion costs sum to at most `maxCost`.

### Examples

**Example 1**

- Input: `s = "abcd"`, `t = "bcdf"`, `maxCost = 3`
- Output: `3`

Changing `"abc"` into `"bcd"` costs $1+1+1=3$.

**Example 2**

- Input: `s = "abcd"`, `t = "cdef"`, `maxCost = 3`
- Output: `1`

Each corresponding character costs 2, so two adjacent changes would exceed the budget.

**Example 3**

- Input: `s = "abcd"`, `t = "acde"`, `maxCost = 0`
- Output: `1`

Only positions that already match can belong to a zero-cost answer.
