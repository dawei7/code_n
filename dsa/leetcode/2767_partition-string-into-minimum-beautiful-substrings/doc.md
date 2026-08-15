# Partition String Into Minimum Beautiful Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2767 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Dynamic Programming, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Partition String Into Minimum Beautiful Substrings](https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/) |

## Problem Description

### Goal

You are given a binary string `s`. Partition all of its characters, without reordering or omission, into one or more contiguous substrings. A substring is beautiful only if it has no leading zero and its binary value is a power of $5$.

Powers include $5^0 = 1$, whose binary representation is `"1"`. Return the minimum number of beautiful substrings needed for a complete partition of `s`. If no such partition exists, return `-1`.

### Function Contract

**Inputs**

- `s`: A string of length $n$, where $1 \leq n \leq 15$ and every character is either `'0'` or `'1'`.

**Return value**

Return the minimum number of beautiful contiguous pieces in a complete partition, or `-1` when no complete partition is possible.

### Examples

#### Example 1

- **Input:** `s = "1011"`
- **Output:** `2`
- **Explanation:** Split the string as `"101" | "1"`, representing $5^1$ and $5^0$.

#### Example 2

- **Input:** `s = "111"`
- **Output:** `3`
- **Explanation:** Each `"1"` is beautiful, and no longer piece is a power of $5$.

#### Example 3

- **Input:** `s = "0"`
- **Output:** `-1`
- **Explanation:** A beautiful substring cannot begin with zero.
