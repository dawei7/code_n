# Minimum Add to Make Parentheses Valid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 921 |
| Difficulty | Medium |
| Topics | String, Stack, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) |

## Problem Description
### Goal

A parentheses string is valid exactly when it is empty, is a concatenation `AB` of two valid strings, or has the form `(A)` for a valid string `A`.

You are given a string `s` containing only opening and closing parentheses. In one move, insert either `'('` or `')'` at any position. Return the minimum number of insertions needed to make the resulting string valid.

### Function Contract
**Inputs**

- `s`: a parentheses string of length $n$, where $1 \le n \le 1000$ and every character is either `'('` or `')'`.

**Return value**

The minimum number of parenthesis characters that must be inserted anywhere in `s` to obtain a valid parentheses string.

### Examples
**Example 1**

- Input: `s = "())"`
- Output: `1`

**Example 2**

- Input: `s = "((("`
- Output: `3`

**Example 3**

- Input: `s = "()()"`
- Output: `0`
