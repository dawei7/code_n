# 24 Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 679 |
| Difficulty | Hard |
| Topics | Array, Math, Backtracking |
| Official Link | [LeetCode](https://leetcode.com/problems/24-game/) |

## Problem Description
### Goal
You are given exactly four cards whose integer values lie from `1` through `9`. Arrange all four values in a mathematical expression using the binary operators `+`, `-`, `*`, and `/` together with parentheses so that the expression evaluates to `24`.

Return `True` if such an expression exists and `False` otherwise. Use every card exactly once. Division is real division rather than integer division; every operation combines two values, so unary negation is forbidden; and card digits cannot be concatenated into a multi-digit number. Parentheses may impose any valid evaluation order.

### Function Contract
**Inputs**

- `cards`: exactly four integers, each between one and nine

**Return value**

- `true` if some legal expression using every card evaluates to 24; otherwise `false`

### Examples
**Example 1**

- Input: `cards = [4,1,8,7]`
- Output: `true`

**Example 2**

- Input: `cards = [1,2,1,2]`
- Output: `false`

**Example 3**

- Input: `cards = [3,3,8,8]`
- Output: `true`
