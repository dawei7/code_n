## Description

You are given a string `expression` encoding a nested mathematical expression in a simplified grammar.

A valid expression is one of two forms:

- an integer literal, which may be negative; or
- `op(a,b)`, where `a` and `b` are themselves valid expressions and `op` is one of `"add"`, `"sub"`, `"mul"`, or `"div"`.

The four operations have these meanings:

- `add(a,b) = a + b`
- `sub(a,b) = a - b`
- `mul(a,b) = a * b`
- `div(a,b) = a / b`

Fully evaluate every nested operand according to that grammar, then return the final integer result.
