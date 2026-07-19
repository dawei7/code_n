# Consecutive Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1446 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/consecutive-characters/) |

## Problem Description
### Goal

The power of a string is the greatest length among its non-empty substrings
whose characters are all identical. Such a substring must occupy consecutive
positions: equal letters separated by a different letter belong to different
runs and cannot be combined.

Given a non-empty string `s` containing only lowercase English letters,
return its power. If several runs share the maximum length, return that common
length; the particular character or substring does not need to be reported.

### Function Contract
**Inputs**

- `s`: a string of length $n$, where $1 \le n \le 500$.
- Every character of `s` is a lowercase English letter.

**Return value**

Return an integer equal to the maximum number of consecutive occurrences of
one character anywhere in `s`.

### Examples
**Example 1**

- Input: `s = "leetcode"`
- Output: `2`
- Explanation: The two consecutive `"e"` characters form a longest
  single-character substring.

**Example 2**

- Input: `s = "abbcccddddeeeeedcba"`
- Output: `5`
- Explanation: The run `"eeeee"` is longer than every other run.

**Example 3**

- Input: `s = "abcdef"`
- Output: `1`
- Explanation: Every character starts a new run, so every valid non-empty
  single-character substring has length one.
