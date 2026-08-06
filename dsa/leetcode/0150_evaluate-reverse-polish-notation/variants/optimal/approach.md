## General
**The stack holds complete subexpressions awaiting consumption**

Read tokens from left to right. A numeric token, including a leading-minus integer, is already a complete subexpression, so parse and push it. An operator consumes the two most recent unresolved subexpressions and replaces them with their combined value.

Pop `right` first and `left` second, then evaluate `left operator right`. This order is essential for subtraction and division even though reversing operands would leave addition and multiplication unchanged.

**Division must truncate toward zero using integer arithmetic**

Python floor division is wrong for a negative nonintegral quotient because it rounds toward negative infinity. Compute `abs(left) // abs(right)`, then negate the quotient exactly when the operand signs differ. This implements truncation toward zero without floating-point precision concerns.

After each processed prefix, the stack contains, in order, the values of all complete postfix subexpressions not yet consumed by a later operator. Numbers establish this property, and an operator preserves it by replacing exactly its two operand values with their result. Valid postfix syntax guarantees that the operands exist and that the full expression leaves exactly one value, which is therefore the answer.

## Complexity detail
Each of the $n$ tokens is processed once with a constant number of stack and arithmetic operations, giving $O(n)$ time. An operand-heavy valid prefix can leave $O(n)$ unresolved values on the stack, so auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Build an expression tree:** evaluates correctly but allocates nodes the stack method does not need.
- **Convert to infix and evaluate text:** introduces precedence, safety, and division-semantics concerns.
- **Use `int(left / right)`:** gives the desired rounding for small values but unnecessarily passes through floating point.
- A single numeric token is already a complete expression.
- Negative numeric strings must be parsed as operands; only the four exact operator tokens are operators.
- Valid input guarantees enough operands, no division by zero, and exactly one final stack value.
