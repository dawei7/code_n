# Find Valid Pair of Adjacent Digits in String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3438 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/) |

## Problem Description

### Goal

Given a string containing only the digits `1` through `9`, find a valid pair of adjacent characters. The two digits in such a pair must be different, and each of those digits must occur in the entire string exactly as many times as the numeric value it represents.

Inspect adjacent pairs from left to right and return the first one satisfying both conditions. If the string contains no valid pair, return the empty string.

### Function Contract

**Inputs**

- `s`: A digit string of length from $2$ through $100$, using only characters from `1` through `9`.

**Return value**

Return the first valid two-character adjacent substring, or `""` when no such pair exists.

### Examples

#### Example 1

- **Input:** `s = "2523533"`
- **Output:** `"23"`

#### Example 2

- **Input:** `s = "221"`
- **Output:** `"21"`

#### Example 3

- **Input:** `s = "22"`
- **Output:** `""`
