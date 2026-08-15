# Shortest and Lexicographically Smallest Beautiful String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2904 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/) |

## Problem Description

### Goal

You receive a binary string `s` and a positive integer `k`. A substring is called beautiful when it contains exactly `k` occurrences of `"1"`.

Among all beautiful substrings, first minimize the substring length. If several beautiful substrings share that minimum length, choose the lexicographically smallest one. For equal-length strings, lexicographic order is determined by the first position at which their characters differ.

Return the selected substring. If `s` has no substring containing exactly `k` ones, return the empty string.

### Function Contract

**Inputs**

- `s`: A binary string with length from $1$ through $100$.
- `k`: The exact required number of ones, where $1\le k\le \lvert s\rvert$.

**Return value**

Return the shortest substring of `s` containing exactly `k` ones, breaking equal-length ties by lexicographic order. Return `""` when no such substring exists.

### Examples

#### Example 1

- **Input:** `s = "100011001", k = 3`
- **Output:** `"11001"`
- **Explanation:** Length five is the minimum possible, and `"11001"` is the lexicographically smallest beautiful substring of that length.

#### Example 2

- **Input:** `s = "1011", k = 2`
- **Output:** `"11"`
- **Explanation:** The adjacent ones form a shorter beautiful substring than either length-three alternative.

#### Example 3

- **Input:** `s = "000", k = 1`
- **Output:** `""`
- **Explanation:** The string contains no ones, so no beautiful substring exists.
