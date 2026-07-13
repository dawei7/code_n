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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Reduce high-precedence work before storing additive terms**

Scan left to right while building the current number. Keep a stack of signed additive terms. Addition and subtraction start new terms, while multiplication and division immediately combine the preceding term with the current number.

**Let the previous operator consume the completed number**

Store the previously seen operator. When the scan reaches the next operator or the end of the string, apply that stored operator to the completed number. This avoids special parsing for the first number and ensures multi-digit values are consumed as a unit.

After each operator boundary, the stack sums to the value of the fully processed expression prefix after all multiplication and division inside that prefix have been resolved. The current number and pending operator describe the only unfinished term.

**Multiplication changes the most recent term, not the whole sum**

For `3+2*2`, push `3`, then push `2`. When the final `2` is complete, replace the preceding `2` with $2 \cdot 2 = 4$. Summing `[3, 4]` gives `7`.

Every number is consumed exactly once by the operator before it. Immediate replacement for `*` and `/` keeps an entire multiplicative chain inside one additive term, while `+` and `-` begin new signed terms. At end of input all terms are complete, so their sum is the expression's value under the required precedence rules.

#### Complexity detail

Each character is inspected once, for $O(n)$ time. In an expression consisting mostly of additions or subtractions, the stack contains $O(n)$ terms.

#### Alternatives and edge cases

- **Recursive-descent parsing:** is extensible to parentheses but unnecessary here.
- **Repeatedly searching for high-precedence operators:** can become quadratic.
- Spaces may occur anywhere between tokens, a number may contain many digits, and division of a negative intermediate term must truncate toward zero rather than toward negative infinity.

</details>
