# Score of Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 856 |
| Difficulty | Medium |
| Topics | String, Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/score-of-parentheses/) |

## Problem Description
### Goal
A balanced parentheses string receives a recursive score. The primitive string `"()"` has score $1$. Concatenating balanced strings adds their scores, so `AB` scores as the score of $A$ plus the score of $B$. Wrapping a balanced string doubles its score, so `(A)` scores twice the score of $A$.

Given a guaranteed balanced string `s` containing only `(` and `)`, evaluate and return its score under those rules.

### Function Contract
**Inputs**

- `s`: a balanced parentheses string of length $n$, where $2 \leq n \leq 50$.

**Return value**

Return the integer score obtained from the primitive, concatenation, and wrapping rules.

### Examples
**Example 1**

- Input: `s = "()"`
- Output: `1`

**Example 2**

- Input: `s = "(())"`
- Output: `2`

**Example 3**

- Input: `s = "()()"`
- Output: `2`
