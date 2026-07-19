# Basic Calculator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 224 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Stack, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/basic-calculator/) |

## Problem Description
### Goal
Given a valid arithmetic expression string, evaluate decimal integers combined with addition, subtraction, parentheses, and optional spaces. Parentheses may be nested and change evaluation order. A minus sign may be unary before an integer or parenthesized expression, but a plus sign is never used as a unary operator.

Return the expression's integer result. Multi-digit numbers must be parsed as single operands, spaces have no numerical effect, and subtraction remains order-sensitive across nested groups. The grammar contains no multiplication or division. Evaluate the expression directly without calling a built-in expression evaluator such as `eval`, and consume the full valid input rather than returning an intermediate subexpression value.

### Function Contract
**Inputs**

- `s`: a valid expression string

**Return value**

The expression's integer result without using a built-in evaluator.

### Examples
**Example 1**

- Input: `"1 + 1"`
- Output: `2`

**Example 2**

- Input: `"(1+(4+5+2)-3)+(6+8)"`
- Output: `23`

**Example 3**

- Input: `"-2 + 1"`
- Output: `-1`
