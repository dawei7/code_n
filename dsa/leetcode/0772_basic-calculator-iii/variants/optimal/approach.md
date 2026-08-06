## General
**Encode precedence in parser levels**

Tokenize the integer literals, operators, and parentheses; the source character set contains no spaces. Parse an expression as terms joined by `+` or `-`; parse each term as factors joined by `*` or `/`; parse each factor as a number, a parenthesized expression, or a signed factor. Because a lower-precedence level calls the next higher-precedence level before applying its own operators, multiplication and division bind more tightly automatically.

**Evaluate while consuming tokens**

Each parser function returns the integer value of the tokens it consumed. Repeated operators at the same level are applied immediately from left to right. On `(`, recursively parse a complete expression and then consume its matching `)`.

**Truncate division without floating point**

Divide absolute values with integer floor division, then negate the quotient exactly when the operands have opposite signs. This produces truncation toward zero and avoids floating-point precision loss for large intermediates.

**Make legal nesting safe in Python**

Every parenthesized factor adds three active parser frames: factor, expression, and term. A valid expression can therefore exceed Python's default recursion limit before reaching the source's 10,000-character boundary. Before parsing, derive a conservative recursion limit from the token count, raise the process limit only when necessary, and restore the previous limit in a `finally` block. This preserves the recursive grammar without leaving global runtime state changed after the call.

Number factors are correct by definition, and recursive factors are correct if their enclosed expression is correct. Term evaluation then applies exactly the multiplication and division operations in left-associative order, and expression evaluation applies addition and subtraction after complete terms. Structural induction over parentheses and these precedence levels proves the returned value matches the expression grammar.

## Complexity detail
Tokenization and parsing each inspect every character or token a constant number of times, taking $O(n)$ time. The token list and recursion stack use $O(n)$ space in the worst case of deeply nested parentheses. Adjusting and restoring the recursion limit takes constant time and does not change these bounds.

## Alternatives and edge cases
- **Operator and value stacks:** A shunting-yard evaluator applies operators when precedence requires and also runs in $O(n)$ time with $O(n)$ space. It avoids recursion-limit management, but its state transitions are more verbose than the grammar-shaped parser.
- **Recursive character scanner:** Parsing directly from the source string avoids a separate token list while retaining the same asymptotic bounds.
- **Repeatedly reduce expression substrings:** Rebuilding the remaining expression after each operation can take $O(n^2)$ time.
- **Negative intermediate division:** Use truncation toward zero, not Python's floor division for unlike signs.
- **Left associativity:** $5 / 2 \cdot 2$ evaluates to `4`, not `5`.
- **Nested parentheses:** Each closing parenthesis returns control to exactly its caller.
- **Maximum nesting:** The scoped recursion-limit adjustment covers the deepest balanced expression permitted by the source length and is always restored, including when parsing raises.
- **Unary signs:** A sign before a number or parenthesized factor changes that factor before surrounding operations.
- **Spaces:** They are outside the source's legal character set. The regular-expression tokenizer happens to ignore them, but correctness does not rely on accepting them.
