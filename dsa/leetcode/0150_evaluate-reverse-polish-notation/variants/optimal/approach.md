## General
**The stack contains values of complete but not-yet-consumed subexpressions**

Read tokens left to right. A numeric token, including a leading-minus negative integer, is already a complete subexpression, so parse and push its value. It waits until a later operator consumes it.

**Pop right before left for noncommutative operators**

A binary operator consumes the two most recent unresolved subexpressions. Pop `right` first and `left` second, compute `left operator right`, and push the result. Reversing these operands silently breaks subtraction and division while leaving addition and multiplication tests deceptively correct.

**Implement truncation toward zero without floating point**

Language floor division is wrong for negative nonintegral quotients because it rounds toward negative infinity. Compute `floor(abs(left) / abs(right))` and negate exactly when operand signs differ. This yields truncation toward zero and avoids precision loss from converting large integers through floating point.

**Every operator replaces exactly the subexpressions it combines**

After each token, the stack contains the values of all complete subexpressions in the processed prefix that have not yet been consumed by a later operator, in their original order.

**Trace operand order and negative division**

For tokens `7 -3 /`, pop right `-3`, then left `7`. Absolute quotient is `2`, signs differ, so push `-2`. Computing $-3 / 7$ instead would truncate to zero and be incorrect.

**Each operator collapses one complete postfix subexpression**

After any token prefix, the stack contains the values of the complete subexpressions formed by that prefix which have not yet been consumed. Reading a number creates one such value. Reading an operator consumes the two most recent subexpressions—left operand below right operand—and replaces them with the value of their combination.

Valid postfix syntax guarantees those operands exist and that a complete expression leaves one unconsumed value. The final stack entry is therefore the value of the whole expression.

## Complexity detail
Every token is pushed or causes a constant number of stack operations once, giving $O(n)$ time. In an operand-heavy prefix the stack can hold $O(n)$ integers.

## Alternatives and edge cases
- **Build an expression tree:** works but allocates nodes that evaluation does not require.
- **Convert to infix text and evaluate it:** introduces precedence, safety, and truncation issues.
- **Use `int(left / right)`:** truncates correctly for small values but unnecessarily converts through floating point.
- A single numeric token is a complete expression. Valid input guarantees sufficient operands and exactly one final stack value.
- Tokens may represent negative integers; only exact operator strings should be classified as operators.
