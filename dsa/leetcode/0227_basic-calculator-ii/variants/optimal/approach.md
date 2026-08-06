## General
**Reduce high-precedence work before committing an additive term**

Scan left to right while building the current number. Keep `total` for additive terms that can no longer change and `term` for the one term that multiplication or division may still extend. Addition and subtraction commit `term` to `total` before starting the next signed term, while multiplication and division update `term` in place.

**Let the previous operator consume the completed number**

Store the previously seen operator. When the scan reaches the next operator or the end of the string, apply that stored operator to the completed number. Starting with `operator = "+"` lets the first number follow the same rule as every later number and ensures multi-digit values are consumed as a unit.

After each operator boundary, `total + term` is the value of the processed prefix after all multiplication and division seen so far have been resolved. Only `term` can still change because a following `*` or `/` has higher precedence than a following `+` or `-`.

**Multiplication changes the most recent term, not the whole sum**

For `3+2*2`, the `+` boundary commits `3` and starts `term = 2`. The final multiplication changes that term to $2 \cdot 2 = 4$, so `total + term` is $3 + 4 = 7$.

Every number is consumed exactly once by the operator before it. Immediate updates for `*` and `/` keep an entire multiplicative chain inside `term`, while `+` and `-` finalize the preceding chain. At end of input, returning `total + term` therefore gives the expression's value under the required precedence rules.

## Complexity detail
Each of the $n$ characters is inspected once, for $O(n)$ time. The parser retains a fixed number of integers and characters, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Recursive-descent parsing:** is extensible to parentheses but unnecessary here.
- **Stack of signed terms:** also evaluates precedence in $O(n)$ time, but stores up to $O(n)$ additive terms instead of folding finalized terms into one sum.
- **Repeatedly searching for high-precedence operators:** can become quadratic.
- **Spaces and multi-digit numbers:** spaces may occur between tokens, and all consecutive digits must be accumulated before applying the pending operator.
- **Negative division:** a negative intermediate term must be divided with truncation toward zero rather than Python's floor-division result.
