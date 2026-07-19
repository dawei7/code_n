# Check if Binary String Has at Most One Segment of Ones

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/) |
| Frontend ID | 1784 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given a nonempty binary string `s` with no leading zero. A segment of ones is a maximal contiguous run of one or more `'1'` characters; zeros separate one such run from another.

Determine whether the string contains at most one contiguous segment of ones. Return `true` when all ones belong to the initial uninterrupted run, including when that run occupies the entire string. Return `false` if another `'1'` occurs after the string has already entered a run of zeros.

### Function Contract

**Input**

- `s`: a binary string of length $n$, where $1 \le n \le 100$, every character is `'0'` or `'1'`, and `s[0]` is `'1'`.

**Return value**

- Return `true` if `s` contains at most one contiguous segment of ones; otherwise, return `false`.

### Examples

**Example 1**

- Input: `s = "1001"`
- Output: `false`

The two endpoint ones form two distinct segments.

**Example 2**

- Input: `s = "110"`
- Output: `true`

The two ones are adjacent and form one segment.

**Example 3**

- Input: `s = "1"`
- Output: `true`

The minimum-length string has one segment.
