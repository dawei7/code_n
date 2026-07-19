# Longest Happy String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1405 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/longest-happy-string/) |

## Problem Description

### Goal

Three integers `a`, `b`, and `c` give the available quantities of the letters `"a"`, `"b"`, and `"c"`. Construct a string using no more than each available quantity.

The string is happy when it contains none of `"aaa"`, `"bbb"`, or `"ccc"` as a substring. Return any happy string with the maximum possible length. Not every available character must be used when one letter is too numerous to separate safely, and different maximum-length answers are allowed.

### Function Contract

**Inputs**

- `a`, `b`, and `c`: available nonnegative counts, each at most 100, with at least one character available.

Let $N = a + b + c$.

**Return value**

- Any longest string over `"a"`, `"b"`, and `"c"` that respects the three budgets and has no run of three equal letters.

### Examples

**Example 1**

- Input: `a = 1, b = 1, c = 7`
- Output: one valid answer is `"ccaccbcc"`.

**Example 2**

- Input: `a = 7, b = 1, c = 0`
- Output: one valid answer is `"aabaa"`.

**Example 3**

- Input: `a = 2, b = 2, c = 2`
- Output: any six-character happy arrangement within the budgets.
