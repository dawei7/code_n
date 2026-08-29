## General

**Use a stack for unfinished expression values**

In Reverse Polish Notation, an operator appears after its two operands. Scanning left to right therefore gives a simple rule:

- a number becomes a value available to a later operator;
- an operator consumes the two most recent available values;
- the computed result becomes one new available value.

The list `s` is used as that stack. Parentheses and precedence rules are unnecessary because token order already says exactly when each operation is ready.

**The stack’s meaning after every token**

After processing any prefix of `tokens`, `s` contains the values of all complete subexpressions in that prefix that have not yet been consumed by a later operator. Their order matches their left-to-right order in the expression.

For a number token, `int(token)` converts the complete signed string, such as `"-11"`, and appends it. A minus sign inside a numeric token is not confused with the operator token `"-"` because dictionary membership checks the entire string.

For an operator token, validity of the RPN input guarantees at least two available values. The operation consumes those two values and pushes their combined result, preserving the invariant.

At the end, a valid complete expression leaves exactly one value. The source returns `s[0]`.

**Understand the unusual two-pop expression**

Suppose the top of the stack ends with left operand `x` followed by right operand `y`:

`[..., x, y]`

Python evaluates function arguments from left to right. First, `s.pop(-2)` removes `x`, the second-last item. The stack becomes `[..., y]`. Then `s.pop(-1)` removes `y`.

The operator is therefore called as `operator(x, y)`, which is the required order.

This is especially important for subtraction and division:

$$
x-y\ne y-x
$$

and generally:

$$
x/y\ne y/x.
$$

A more conventional implementation would pop `y` first and then `x`. This source achieves the same operand ordering through indexed pops.

**Dispatch through operator functions**

The `opt` dictionary maps the four token strings to functions:

- `+` to `operator.add`;
- `-` to `operator.sub`;
- `*` to `operator.mul`;
- `/` to `operator.truediv`.

That removes a long conditional chain while retaining distinct arithmetic semantics.

After applying any function, the source wraps the result in `int(...)`. For addition, subtraction, and multiplication, the result is already an integer, so this conversion changes nothing.

For division, `truediv` produces a floating result. Python’s `int` conversion discards the fractional part toward zero. Thus `int(-7 / 3)` becomes `-2`, while floor division would produce `-3`. Truncation toward zero is exactly the Reference rule.

The contract guarantees that all intermediate integer results fit in signed 32 bits. Such integers are exactly representable by Python’s double-precision float, so using `truediv` does not lose integer magnitude before truncation under this domain. An integer-only sign-aware division formula would be more general for larger values.

**Trace a basic expression**

For `["2","1","+","3","*"]`:

- push two: `[2]`;
- push one: `[2,1]`;
- consume two and one with `+`, producing `[3]`;
- push three: `[3,3]`;
- consume them with `*`, producing `[9]`.

For `["4","13","5","/","+"]`, division consumes 13 as the left operand and five as the right, pushes two, and addition then produces six.

Every intermediate result replaces exactly two operands, so the stack shrinks by one at each operator.

## Complexity detail

Let $n$ be the number of tokens.

Each token is processed once. Number conversion, dictionary lookup, arithmetic under the bounded integer domain, append, and end-position pop are constant-time operations. `pop(-2)` removes the second-last stack element, so it shifts only the one element after it and is also constant time. Total time is $O(n)$.

The stack can contain a linear number of operands before operators consume them. Auxiliary space is $O(n)$, matching the manifest.

The operator dictionary has four fixed entries and therefore contributes $O(1)$ space.

## Alternatives and edge cases

- **Explicit conditionals:** Pop right then left and use `if` branches for each operator. It is longer but makes operand order highly visible.
- **Integer-only truncating division:** Compute `abs(x) // abs(y)` and apply the sign. It avoids floating-point conversion and generalizes beyond 32-bit values.
- **Reduce tokens in place:** Replace each operator and its preceding operands inside the input list. Repeated middle deletions make it $O(n^2)$ time.
- **Recursive parser from the end:** Read tokens backward, recursively evaluate the left and right operands in the correct reversed order. It uses $O(n)$ call-stack space.
- **One numeral:** It is pushed and returned with no operation.
- **Negative numeral token:** The full token is not an operator key and `int` parses its sign.
- **Subtraction/division order:** Swapping the operands yields wrong answers; the indexed pops intentionally preserve `x op y`.
- **Division by zero:** The Reference guarantees it never occurs, so no check is needed.
- **Malformed RPN:** Too few operands would raise on `pop`, and surplus operands would violate the final-one-value assumption; the source trusts validity.
- **Runtime dependency:** The source uses `List` without importing it. Standalone Python needs `from typing import List`.
