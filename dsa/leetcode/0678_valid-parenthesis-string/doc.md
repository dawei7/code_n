# Valid Parenthesis String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 678 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming, Stack, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-parenthesis-string/) |

## Problem Description
### Goal
Given a string `s` containing only `(`, `)`, and `*`, determine whether it can represent a valid parenthesis string. Every left parenthesis must have a later matching right parenthesis, and every right parenthesis must have an earlier matching left parenthesis.

Each `*` may independently be treated as one left parenthesis, one right parenthesis, or the empty string. Return `True` if at least one assignment makes the entire string valid and `False` otherwise. Matching must preserve character order, and all chosen parentheses must be paired by the end.

### Function Contract
**Inputs**

- `s`: a string containing only `(`, `)`, and `*`

**Return value**

- `true` if some interpretation of all wildcards produces valid balanced parentheses; otherwise `false`

### Examples
**Example 1**

- Input: `s = "()"`
- Output: `true`

**Example 2**

- Input: `s = "(*)"`
- Output: `true`

**Example 3**

- Input: `s = "(*))"`
- Output: `true`
