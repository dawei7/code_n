# Find the Index of the First Occurrence in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `string_04` |
| Frontend ID | 28 |
| Difficulty | Easy |
| Topics | Two Pointers, String, String Matching |
| Official Link | [find-the-index-of-the-first-occurrence-in-a-string](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) |

## Problem Description & Examples
### Goal
Find the first index where pattern occurs in text using
the naive O(n*m) sliding-window approach. Returns -1
if the pattern is not present.
Use KMP (string_03) for the linear-time alternative.
Source: https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/

### Function Contract
**Inputs**

- `text`: the string to search in.
- `pattern`: the string to search for.

**Return value**

the first index of pattern in text, or -1 if not found.

### Examples
**Example 1**

- Input: `text = 'hello', pattern = 'll'`
- Output: `2`

**Example 2**

- Input: `text = 'aaaa', pattern = 'aa'`
- Output: `0`

**Example 3**

- Input: `text = 'abcde', pattern = 'xyz'`
- Output: `-1`

---

## Underlying Base Algorithm(s)
strings

---

## Complexity Analysis
- **Time Complexity**: `O(n²)`
- **Space Complexity**: `TODO`
