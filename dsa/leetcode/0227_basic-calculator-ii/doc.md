# Basic Calculator II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 227 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/basic-calculator-ii/) |

## Problem Description
### Goal
Given a valid arithmetic expression string, evaluate nonnegative decimal integers joined by the binary operators `+`, `-`, `*`, and `/`, with optional spaces. Multiplication and division have higher precedence than addition and subtraction, and operators of the same precedence are applied from left to right.

Return the final integer result without using a built-in expression evaluator. Division truncates toward zero, including when an intermediate value is negative, and division by zero does not occur. Parse multi-digit operands correctly and consume the entire expression. Parentheses are not part of this grammar, so precedence comes solely from the four operators.

### Function Contract
**Inputs**

- `s`: a valid expression string containing decimal integers, spaces, and the four operators

**Return value**

The integer value of the complete expression.

### Examples
**Example 1**

- Input: `s = "3+2*2"`
- Output: `7`

**Example 2**

- Input: `s = " 3/2 "`
- Output: `1`

**Example 3**

- Input: `s = " 3+5 / 2 "`
- Output: `5`
