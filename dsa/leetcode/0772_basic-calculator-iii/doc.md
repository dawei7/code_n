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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Encode precedence in parser levels**

Tokenize integers and operators while ignoring spaces. Parse an expression as terms joined by `+` or `-`; parse each term as factors joined by `*` or `/`; parse each factor as a number, a parenthesized expression, or a signed factor. Because a lower-precedence level calls the next higher-precedence level before applying its own operators, multiplication and division bind more tightly automatically.

**Evaluate while consuming tokens**

Each parser function returns the integer value of the tokens it consumed. Repeated operators at the same level are applied immediately from left to right. On `(`, recursively parse a complete expression and then consume its matching `)`.

**Truncate division without floating point**

Divide absolute values with integer floor division, then negate the quotient exactly when the operands have opposite signs. This produces truncation toward zero and avoids floating-point precision loss for large intermediates.

Number factors are correct by definition, and recursive factors are correct if their enclosed expression is correct. Term evaluation then applies exactly the multiplication and division operations in left-associative order, and expression evaluation applies addition and subtraction after complete terms. Structural induction over parentheses and these precedence levels proves the returned value matches the expression grammar.

#### Complexity detail

Tokenization and parsing each inspect every character or token a constant number of times, taking $O(n)$ time. The token list and recursion stack use $O(n)$ space in the worst case of deeply nested parentheses.

#### Alternatives and edge cases

- **Operator and value stacks:** A shunting-yard evaluator applies operators when precedence requires and also runs in $O(n)$ time with $O(n)$ space.
- **Recursive character scanner:** Parsing directly from the source string avoids a separate token list while retaining the same asymptotic bounds.
- **Repeatedly reduce expression substrings:** Rebuilding the remaining expression after each operation can take $O(n^2)$ time.
- **Negative intermediate division:** Use truncation toward zero, not Python's floor division for unlike signs.
- **Left associativity:** $5 / 2 \cdot 2$ evaluates to `4`, not `5`.
- **Nested parentheses:** Each closing parenthesis returns control to exactly its caller.
- **Unary signs:** A sign before a number or parenthesized factor changes that factor before surrounding operations.
- **Spaces:** They have no semantic effect.

</details>
