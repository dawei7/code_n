# Satisfiability of Equality Equations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 990 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/satisfiability-of-equality-equations/) |

## Problem Description

### Goal

You are given an array of equations describing relationships among one-letter variable names. Every equation has exactly four characters and has one of the forms `"x==y"` or `"x!=y"`, where `x` and `y` are lowercase letters and may even be the same letter.

Determine whether integers can be assigned to all variable names so that every equality and inequality holds simultaneously. Return `true` when such an assignment exists and `false` when the constraints contradict one another.

### Function Contract

**Inputs**

- `equations`: a list of $Q$ strings, where $1\le Q\le500$. Each string has length four, its first and last characters are lowercase letters, its second character is either `'='` or `'!'`, and its third character is `'='`.

**Return value**

- `true` if one integer assignment satisfies every equation; otherwise, `false`.

### Examples

**Example 1**

- Input: `equations = ["a==b", "b!=a"]`
- Output: `false`
- Explanation: The equality requires the two variables to match, while the inequality requires them to differ.

**Example 2**

- Input: `equations = ["b==a", "a==b"]`
- Output: `true`
- Explanation: Assigning the same integer to both variables satisfies both equations.

**Example 3**

- Input: `equations = ["a==b", "b==c", "a!=c"]`
- Output: `false`
- Explanation: The first two equalities imply that `a` and `c` are equal.
