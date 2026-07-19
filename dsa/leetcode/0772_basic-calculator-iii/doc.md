# Basic Calculator III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 772 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Stack, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/basic-calculator-iii/) |

## Problem Description

### Goal

Given a valid arithmetic expression containing non-negative integer literals, spaces, parentheses, and the binary operators `+`, `-`, `*`, and `/`, compute its integer value.

Respect parentheses and ordinary operator precedence, evaluating multiplication and division before addition and subtraction and applying equal-precedence operations from left to right. Division truncates toward zero rather than taking a mathematical floor, and the input guarantees that no division uses a zero divisor. Return the final integer result.

### Function Contract

**Inputs**

- `s`: a valid expression whose divisions never use a zero divisor.

**Return value**

- The integer result after evaluating all parentheses and operations with truncation toward zero for division.

### Examples

**Example 1**

- Input: `s = "1 + 1"`
- Output: `2`

**Example 2**

- Input: `s = "6-4 / 2"`
- Output: `4`
- Explanation: Division is evaluated before subtraction.

**Example 3**

- Input: `s = "2*(5+5*2)/3+(6/2+8)"`
- Output: `21`
- Explanation: Parentheses and multiplication or division are resolved before the outer additions.
