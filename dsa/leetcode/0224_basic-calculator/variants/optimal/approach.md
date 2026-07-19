## General
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

## Complexity detail
Each character is examined once, so time is $O(n)$. The stack stores two values per unmatched opening parenthesis, using $O(d)$ space for nesting depth `d`.

## Alternatives and edge cases
- Recursive descent maps naturally to the grammar and has the same asymptotic bounds, using call frames instead of an explicit context stack.
- Converting to postfix requires an operator stack and a separate evaluation pass, which is unnecessary for this limited precedence.
- Calling a built-in evaluator violates the contract and may introduce security risks on untrusted input.
- Spaces may appear anywhere permitted by the grammar, and numbers may contain multiple digits.
- Unary minus can appear at the start or before a parenthesized subexpression; deeply nested input determines stack usage.
