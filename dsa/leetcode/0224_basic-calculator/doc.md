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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(d)$

<details>
<summary>Approach</summary>

#### General

Because the grammar contains only addition and subtraction, terms can be committed as soon as the next operator or closing parenthesis is reached; there is no multiplication precedence to defer.

Within the current parenthesis level, maintain:

- `result`: the sum of fully committed terms,
- `number`: the multi-digit integer currently being read,
- `sign`: `+1` or `-1` for that pending number.

Digits extend `number = 10 * number + digit`. On `+` or `-`, add `sign * number` to `result`, reset the number, and store the new sign. Spaces do nothing.

**Parentheses as saved affine contexts**

An opening parenthesis starts an inner expression whose final value will act as one signed term in the outer expression. Push the outer `result` and the sign preceding the parenthesis, then reset to a fresh context. At `)`, first commit the inner pending number, then recover the saved values and compute

`outer_result + outer_sign * inner_result`.

For `1-(2-(3+4))`, the first `(` saves outer result `1` and sign `-1`. The nested context similarly saves `2` and `-1`. Closing the inner group produces `7`, then $2 - 7 = -5$; closing the outer group yields $1 - (-5) = 6$.

Unary signs work because a fresh context begins with `result = 0` and `number = 0`. Encountering `-` at the beginning simply commits zero and sets the sign of the following number or group. Valid-input guarantees remove the need for error recovery, but the parser still must commit the final pending number after the scan.

At any scan position, `result + sign * number` represents the value accumulated so far in the current level, and the stack holds exactly the suspended outer affine contexts. Each token update preserves that interpretation; closing a group substitutes its completed value into the saved context, matching the expression grammar.

#### Complexity detail

Each character is examined once, so time is $O(n)$. The stack stores two values per unmatched opening parenthesis, using $O(d)$ space for nesting depth `d`.

#### Alternatives and edge cases

- Recursive descent maps naturally to the grammar and has the same asymptotic bounds, using call frames instead of an explicit context stack.
- Converting to postfix requires an operator stack and a separate evaluation pass, which is unnecessary for this limited precedence.
- Calling a built-in evaluator violates the contract and may introduce security risks on untrusted input.
- Spaces may appear anywhere permitted by the grammar, and numbers may contain multiple digits.
- Unary minus can appear at the start or before a parenthesized subexpression; deeply nested input determines stack usage.

</details>
