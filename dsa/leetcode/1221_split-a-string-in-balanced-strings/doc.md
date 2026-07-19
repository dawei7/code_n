# Split a String in Balanced Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1221 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/split-a-string-in-balanced-strings/) |

## Problem Description

### Goal

A string is **balanced** when it contains the same number of `L` and `R` characters. You are given a balanced string `s` containing only those two characters.

Split `s` into nonempty, contiguous balanced strings so that every character belongs to exactly one piece and the pieces retain their original order. Return the maximum number of balanced strings obtainable in such a split.

### Function Contract

**Inputs**

- `s`: A balanced string of length $n$ containing only `L` and `R`, where $2\le n\le1000$.

**Return value**

- The greatest possible number of nonempty balanced pieces in a complete split of `s`.

### Examples

**Example 1**

- Input: `s = "RLRRLLRLRL"`
- Output: `4`

One maximum split is `RL | RRLL | RL | RL`.

**Example 2**

- Input: `s = "RLRRRLLRLL"`
- Output: `2`

It may be split as `RL | RRRLLRLL`.

**Example 3**

- Input: `s = "LLLLRRRR"`
- Output: `1`

No proper prefix is balanced, so the entire string is the only piece.
