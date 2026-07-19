# Least Operators to Express Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 964 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [least-operators-to-express-number](https://leetcode.com/problems/least-operators-to-express-number/) |

## Problem Description

### Goal

Given positive integers `x` and `target`, build an expression containing only repeated copies of `x` separated by the binary operators `+`, `-`, `*`, and `/`. Division produces rational values, and the expression is evaluated with the usual precedence: multiplication and division before addition and subtraction.

Parentheses may not be inserted, and unary negation is forbidden. Thus `x - x` is allowed, while an expression beginning with `-x` is not. Return the fewest binary operators needed for the complete expression to equal `target` exactly.

### Function Contract

**Inputs**

- `x`: the only permitted numeric operand, where $2 \le x \le 100$.
- `target`: the required positive integer value, where $1 \le \texttt{target} \le 2\times10^8$.
- Let

$$
L = \lfloor \log_x(\texttt{target}) \rfloor + 1
$$

  denote the number of base-$x$ digits in `target`.

**Return value**

Return the minimum number of binary operators in a valid expression whose value is `target`.

### Examples

**Example 1**

- Input: `x = 3, target = 19`
- Output: `5`
- Explanation: `3 * 3 + 3 * 3 + 3 / 3` uses five operators.

**Example 2**

- Input: `x = 5, target = 501`
- Output: `8`
- Explanation: `5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5` uses eight operators.

**Example 3**

- Input: `x = 100, target = 100000000`
- Output: `3`
- Explanation: `100 * 100 * 100 * 100` uses three operators.
