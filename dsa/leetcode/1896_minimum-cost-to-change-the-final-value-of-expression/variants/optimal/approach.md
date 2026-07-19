## General
**Keep both possible outcomes.** For every parsed subexpression, store a pair $(c_0,c_1)$: the minimum cost to make that subexpression evaluate to $0$ and to $1$. A literal `0` starts as $(0,1)$, while `1` starts as $(1,0)`.

When two pairs meet at an operator, consider the four combinations of left and right Boolean values. For each combination, evaluate both the written operator and its flipped form; changing the operator adds one to the cost. Taking the minimum for each resulting Boolean value produces the pair for the combined expression. This constant-size transition accounts for changing operands, changing the operator, or doing both.

**Parse the specified evaluation order.** Scan the string once. The current pair and pending operator describe the active parenthesis level. Because `&` and `|` have equal precedence, combine a new operand immediately with the current pair. On `(`, save the outer state on a stack and start a fresh frame. On `)`, restore the outer frame and treat the completed inner pair as its next operand.

For the complete expression, exactly one entry in the final pair is zero: it corresponds to the unchanged value. Return the other entry, which is the least cost to obtain the opposite value.

## Complexity detail
Each of the $N$ characters is examined once. A combination checks only two Boolean values for each operand and two possible operators, so it takes constant time. The total time is $O(N)$. Nested parentheses may place $O(N)$ saved frames on the stack, giving $O(N)$ auxiliary space.

## Alternatives and edge cases
- **Recursive parsing:** A recursive descent parser can carry the same two-cost state, but an expression may nest far beyond Python's safe call depth.
- **Re-evaluate after candidate edits:** Trying changes and evaluating the whole expression again repeats work and quickly becomes exponential when the answer needs several edits.
- **Conventional precedence:** Treating `&` as stronger than `|` is incorrect here; unparenthesized operators are evaluated left to right.
- **Operator changes:** The cheapest solution may flip an operator even when neither operand changes, so transitions must include both possible operators.
- **Redundant parentheses:** Extra matched layers around a literal or group do not change its cost pair.
- **Single literal:** With no operator present, flipping the only character always costs exactly one.
