# Minimum Additions to Make Valid String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2645 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Stack, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-additions-to-make-valid-string/) |

## Problem Description

### Goal

You are given a nonempty string `word` containing only the letters `a`, `b`, and `c`. You may insert any of these letters at any positions, any number of times, while preserving the original characters' relative order.

A string is valid exactly when it consists of one or more consecutive copies of `"abc"`. Return the minimum number of inserted letters needed to turn `word` into such a valid string. Existing letters cannot be removed, replaced, or reordered.

### Function Contract

**Inputs**

- `word`: A string of length $n$, where $1 \le n \le 50$, containing only `a`, `b`, and `c`.

**Return value**

- Return the minimum number of inserted letters required to make `word` a concatenation of `"abc"`.

### Examples

**Example 1**

- Input: `word = "b"`
- Output: `2`
- Explanation: Insert `a` before the existing `b` and `c` after it.

**Example 2**

- Input: `word = "aaa"`
- Output: `6`
- Explanation: Each existing `a` must begin a different `"abc"` group.

**Example 3**

- Input: `word = "abc"`
- Output: `0`
