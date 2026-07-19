# Maximum Nesting Depth of the Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1614 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/) |

## Problem Description
### Goal
A valid parentheses string may contain digits, arithmetic operators, and matched pairs of parentheses. Its nesting depth at a position is the number of opening parentheses whose matching closing parentheses have not yet appeared.

Given such a valid string `s`, return its maximum nesting depth: the greatest number of parenthesis pairs simultaneously surrounding any position. A string with no parentheses has depth zero, while adjacent parenthesized groups do not add to one another unless one group is inside another.

### Function Contract
**Inputs**

- `s`: a valid parentheses string of length $n$, where $1 \le n \le 100$.
- Every character is a digit, one of `+`, `-`, `*`, or `/`, or a parenthesis.
- The parentheses in `s` are balanced and properly nested.

**Return value**

Return the largest number of open parenthesis pairs present at the same point while scanning `s`.

### Examples
**Example 1**

- Input: `s = "(1+(2*3)+((8)/4))+1"`
- Output: `3`

**Example 2**

- Input: `s = "(1)+((2))+(((3)))"`
- Output: `3`

**Example 3**

- Input: `s = "()(())((()()))"`
- Output: `3`
