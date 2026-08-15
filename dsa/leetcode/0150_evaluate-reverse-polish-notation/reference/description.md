### 1. Description

You are given an array of strings `tokens` that represents an arithmetic expression in a <a href="http://en.wikipedia.org/wiki/Reverse_Polish_notation" target="_blank">Reverse Polish Notation</a>.

Evaluate the expression. Return *an integer that represents the value of the expression*.

### 2. Function Contract

**Inputs**

- `tokens`: A valid Reverse Polish Notation expression whose tokens are integers or the binary operators `+`, `-`, `*`, and `/`.

**Return value**

Return the integer value of the complete expression.

### 3. Note

that:

- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.

- Each operand may be an integer or another expression.

- The division between two integers always **truncates toward zero**.

- There will not be any division by zero.

- The input represents a valid arithmetic expression in a reverse polish notation.

- The answer and all the intermediate calculations can be represented in a **32-bit** integer.

### 4. Examples

#### Example 1

- **Input:** $tokens = ["2","1","+","3","*"]$
- **Output:** `9`
- **Explanation:** ((2 + 1) * 3) = 9

#### Example 2

- **Input:** $tokens = ["4","13","5","/","+"]$
- **Output:** `6`
- **Explanation:** (4 + (13 / 5)) = 6

#### Example 3

- **Input:** $tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]$
- **Output:** `22`
- **Explanation:** ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

### 5. Constraints

- $1 \le \text{tokens.length} \le 10^{4}$

- $\text{tokens}[i]$ is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.
