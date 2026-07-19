# Shuffle String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1528 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [LeetCode](https://leetcode.com/problems/shuffle-string/) |

## Problem Description
### Goal

Given a lowercase string `s` and an integer array `indices` of the same length, shuffle the string by moving the character originally at position `i` to position `indices[i]` in the result.

Every value in `indices` is unique and lies within the string's index range, so `indices` is a permutation of all result positions. Return the string obtained after every character has been moved to its specified destination.

### Function Contract
**Inputs**

- `s`: A string of $n$ lowercase English letters, where $1 \leq n \leq 100$.
- `indices`: A length-$n$ integer array containing unique values from 0 through $n-1$.

**Return value**

Return the length-$n$ string whose character at position `indices[i]` equals `s[i]` for every original index `i`.

### Examples
**Example 1**

- Input: `s = "codeleet", indices = [4, 5, 6, 7, 0, 2, 1, 3]`
- Output: `"leetcode"`
- Explanation: Each source character is written to its paired destination position.

**Example 2**

- Input: `s = "abc", indices = [0, 1, 2]`
- Output: `"abc"`
- Explanation: The identity permutation leaves every character in place.

**Example 3**

- Input: `s = "aiohn", indices = [3, 1, 4, 2, 0]`
- Output: `"nihao"`
