## Description

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, `'+'`, `'-'`, `'*'`, `'/'` operators, and open `'('` and closing parentheses `')'`. The integer division should **truncate toward zero**.

You may assume that the given expression is always valid. All intermediate results will be in the range of $[-2^{31}, 2^{31} - 1]$.

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.
### Function Contract

**Inputs**

- `s`: a valid expression string containing only decimal digits, `+`, `-`, `*`, `/`, `(`, and `)`.

Every literal is non-negative. Parentheses determine grouping, multiplication and division bind more tightly than addition and subtraction, and equal-precedence operators are evaluated from left to right. The validity guarantee means that every operation, including division, is defined.

**Return value**

- The integer value of the complete expression, using truncation toward zero for every division.

### Examples
#### Example 1

- **Input:** `s = "1+1"`
- **Output:** `2`
#### Example 2

- **Input:** `s = "6-4/2"`
- **Output:** `4`
#### Example 3

- **Input:** `s = "2*(5+5*2)/3+(6/2+8)"`
- **Output:** `21`
### Constraints

- $1 \le s \le 10^{4}$

- `s` consists of digits, `'+'`, `'-'`, `'*'`, `'/'`, `'('`, and `')'`.

- `s` is a **valid** expression.