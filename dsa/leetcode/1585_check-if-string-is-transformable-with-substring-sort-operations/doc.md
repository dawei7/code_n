# Check If String Is Transformable With Substring Sort Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1585 |
| Difficulty | Hard |
| Topics | String, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/) |

## Problem Description
### Goal

Given digit strings `s` and `t` of equal length, decide whether `s` can be changed into `t` by repeating the following operation any number of times: choose a non-empty substring of the current string and sort that substring in ascending order in place.

Each operation may move a smaller digit left across larger digits, but ascending sorting cannot move a larger digit left across a smaller digit. Operations may overlap, and choosing no operations is allowed.

Return whether some sequence of these substring sorts produces exactly `t`. A substring is a contiguous part of the string.

### Function Contract
**Inputs**

- `s`: A string of $N$ decimal digits, where $1 \le N \le 10^5$.
- `t`: A string of the same length as `s`, also containing only decimal digits.

**Return value**

Return `true` if ascending sorts of non-empty substrings can transform `s` into `t`; otherwise, return `false`.

### Examples
**Example 1**

- Input: `s = "84532", t = "34852"`
- Output: `true`

**Example 2**

- Input: `s = "34521", t = "23415"`
- Output: `true`

**Example 3**

- Input: `s = "12345", t = "12435"`
- Output: `false`
