## General

**Operand boundaries and operators form the search tree**

At digit position `i`, try every following substring as the next operand, stopping after the one-character operand zero
when `num[i] == "0"`. The first operand has no operator; later operands branch over addition, subtraction, and
multiplication.

The candidate keeps the current expression as one backtracked `path` list. For each later operand it appends an operator
slot and the token, changes that operator slot from `+` to `-` to `*` across the three recursive calls, and removes both
parts afterward. A complete valid path is joined only when its value equals `target`.

**Carry the final additive term to enforce precedence**

Track the expression's current `value` and the most recent signed operand `last`. Addition and subtraction update both
directly. Multiplication replaces the last operand inside the total with `last * operand`, which enforces multiplication
precedence without reparsing.

At every recursion state, `value` equals the path's arithmetic value and `last` is its final additive term. The path
uses exactly the consumed digit prefix with valid operand formatting.

For multiplication, if the current expression value is `value = prefix + last`, replacing the final term gives
`prefix + last * operand`, computed as `value - last + last * operand`. This handles chains such as `2+3*4*5` without
reparsing or storing an operator stack.

**Every valid expression follows one recursion path**

An expression uniquely determines where each operand ends and which operator follows it, so exhaustive branching
reaches it exactly once. The carried state evaluates every branch with normal precedence, and only branches that
consume all digits and equal the target are emitted. Stopping a multi-digit operand after an initial zero removes
exactly the syntactically invalid choices.

## Complexity detail

Each gap can continue the current operand or introduce one of three operators, producing $O(4^n)$ search states under
the conventional bounded-integer branching model. The recursion stack and shared path contain $O(n)$ total digits and
operators, so auxiliary space is $O(n)$. Joining returned expressions contributes their unavoidable output characters,
which are excluded from the auxiliary bound.

## Alternatives and edge cases

- **Generate strings then call `eval`:** repeatedly reparses expressions and complicates safe validation.
- **Rebuild a new expression string at every branch:** is simpler but retains copied prefixes across Python recursion
  frames instead of meeting the stated linear path-space bound directly.
- **Leading zero:** zero is a valid one-digit operand, but a token such as `05` is invalid and must prune that entire
  longer-token loop.
- **Multiplication by zero:** the algorithm must still replace the previous signed term rather than merely multiply the
  complete accumulated value.
- **Negative target:** subtraction stores a negative `last`, so later multiplication preserves precedence without a
  separate sign case.
