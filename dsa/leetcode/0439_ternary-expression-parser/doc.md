# Ternary Expression Parser

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 439 |
| Difficulty | Medium |
| Topics | String, Stack, Recursion |
| Official Link | [LeetCode](https://leetcode.com/problems/ternary-expression-parser/) |

## Problem Description
### Goal
Given a valid ternary expression made from single-character operands, `?`, and `:`, evaluate it under right associativity. Each condition is `T` or `F`; `T ? a : b` selects `a`, while `F ? a : b` selects `b`.

Expressions may nest in either branch, and a selected result may be a digit or Boolean letter. Return the final single-character value. Match each question mark with the correct colon rather than evaluating from left to right, and do not evaluate an unselected branch as though it could change the result. The input contains no parentheses or whitespace.

### Function Contract
**Inputs**

- `expression`: a valid expression composed of single-character operands, `?`, and `:`

**Return value**

- Return the single-character value selected by the nested ternary expression.

### Examples
**Example 1**

- Input: `expression = "T?2:3"`
- Output: `"2"`

**Example 2**

- Input: `expression = "F?1:T?4:5"`
- Output: `"4"`

**Example 3**

- Input: `expression = "T?T?F:5:3"`
- Output: `"F"`
