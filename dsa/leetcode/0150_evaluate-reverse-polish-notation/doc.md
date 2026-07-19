# Evaluate Reverse Polish Notation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 150 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/) |

## Problem Description
### Goal
Given a valid arithmetic expression in Reverse Polish notation, evaluate its tokens from left to right. Integer tokens contribute operands, while each operator `+`, `-`, `*`, or `/` combines the two most recently available values, with the earlier value used as the left operand.

Return the single integer value of the complete expression. Intermediate calculations also use integer arithmetic, and division truncates toward zero rather than rounding down, including for negative results. Tokens may represent negative or multi-digit numbers. The expression is guaranteed to have enough operands for every operator and to finish with exactly one result, with no division by zero.

### Function Contract
**Inputs**

- `tokens`: numbers and binary operators `+`, `-`, `*`, `/` in valid Reverse Polish Notation

**Return value**

The integer value of the complete expression.

### Examples
**Example 1**

- Input: `tokens = ["2","1","+","3","*"]`
- Output: `9`

**Example 2**

- Input: `tokens = ["4","13","5","/","+"]`
- Output: `6`

**Example 3**

- Input: `tokens = ["7","-3","/"]`
- Output: `-2`
