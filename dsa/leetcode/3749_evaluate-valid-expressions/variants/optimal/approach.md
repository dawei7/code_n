## General

The grammar is prefix-form and fully parenthesized, so a closing parenthesis always means that the most recently opened operation now has both operand values available. This makes explicit stacks a natural replacement for recursive parsing, whose call depth could exceed Python's limit on a $10^5$-character expression.

Scan the string once. When an operation name appears, push it. When a signed or unsigned integer literal appears, parse its complete digit sequence and push the value. Commas and opening parentheses only delimit tokens and need no stored state.

At each closing parenthesis, pop the right operand, then the left operand, and finally the matching operation. Apply that operation and push its single result back as the value of the completed subexpression. Validity guarantees those items exist in that order. At the end, exactly one value remains, whether the input was a literal or an arbitrarily nested expression.

Integer division is appropriate because every division is guaranteed to be exact. In particular, exact divisibility makes floor division equal the mathematical integer quotient even when an operand is negative.

## Complexity detail

Let $n=\texttt{expression.length}$. Each character is scanned a constant number of times, so evaluation takes $O(n)$ time. The operator and value stacks can each grow with the nesting depth, which is at most $O(n)$, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Recursive descent:** It mirrors the grammar cleanly but can raise a recursion-depth error on a legal deeply nested expression unless implemented with an explicit stack.
- **Repeated innermost replacement:** Finding an innermost call, evaluating it, and rebuilding the string is correct but can take $O(n^2)$ time.
- **Language `eval`:** The input names and exact integer-division semantics do not directly match a safe arithmetic expression, and evaluating constructed source is unnecessary and unsafe as a parsing strategy.
- **Single literal:** No operator is pushed; parsing the literal leaves the one final value directly.
- **Negative literals:** A minus sign belongs to the following digit sequence and must not be confused with the `sub` operation.
- **Operand order:** Subtraction and division are not commutative, so the right value must be popped before the left and applied as `left op right`.
- **Deep nesting:** The explicit stacks scale to the source length limit without consuming the Python call stack.
