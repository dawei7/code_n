# Lexicographically Smallest String After Applying Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1625 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Depth-First Search, Breadth-First Search, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/) |

## Problem Description
### Goal
You are given an even-length decimal string `s` and integers `a` and `b`. Starting from `s`, either of two operations may be applied any number of times and in any order.

The addition operation increases every digit at an odd 0-indexed position by `a`, wrapping modulo 10. For example, adding 5 to `"3456"` produces `"3951"`. The rotation operation moves the final `b` characters to the front, which is a right rotation by exactly `b` positions.

Return the lexicographically smallest string reachable under these operations. Strings have equal length, so lexicographic order is decided by the first position at which their digits differ.

### Function Contract
**Inputs**

- `s`: an even-length string of $n$ decimal digits, where $2 \le n \le 100$.
- `a`: the amount added modulo 10 to odd-indexed digits, where $1 \le a \le 9$.
- `b`: the right-rotation distance, where $1 \le b \le n-1$.

**Return value**

Return the lexicographically smallest length-$n$ string reachable from `s` by any finite sequence of the two permitted operations.

### Examples
**Example 1**

- Input: `s = "5525", a = 9, b = 2`
- Output: `"2050"`

**Example 2**

- Input: `s = "74", a = 5, b = 1`
- Output: `"24"`

**Example 3**

- Input: `s = "0011", a = 4, b = 2`
- Output: `"0011"`
