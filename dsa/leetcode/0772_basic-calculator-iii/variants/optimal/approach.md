## General

**Evaluate one parenthesized level at a time**

The exact solution converts the input string into a deque of characters and calls recursive `dfs`. One call evaluates until it consumes the deque or encounters the closing parenthesis belonging to that level.

Each call maintains:

- `num`: the integer literal or nested-expression value currently being built.
- `sign`: the operator that must be applied to `num`.
- `stk`: signed terms whose sum is the value of this level.

**Build multi-digit integers**

When a digit is read, `num = num * 10 + digit`. Consecutive digits therefore form one decimal value.

The number is not committed immediately because later digits may belong to it. It is committed when an operator, closing parenthesis, or end of input is reached.

**Evaluate parentheses recursively**

When `(` appears, the method recursively evaluates the following characters. The nested call stops after processing its matching `)` and returns the parenthesized integer.

That value replaces `num`, so the outer level treats the entire parenthesized expression as one operand. This automatically gives parentheses highest precedence.

**Apply the previous operator at a boundary**

On reaching an operator or `)`, the current `num` belongs to the previously stored `sign`:

- `+` appends `num`.
- `-` appends `-num`.
- `*` pops the previous term, multiplies, and pushes the product.
- `/` pops the previous term, divides by `num`, truncates toward zero, and pushes the quotient.

Then `num` resets to zero and `sign` becomes the current character for the next operand.

This “apply the previous operator” detail is crucial. When reading `3*4+5`, the `*` character ends the number three but the prior sign is `+`, so three is first appended. At `+`, prior sign `*` combines three and four.

**How precedence is encoded**

Addition and subtraction append separate signed terms. Multiplication and division immediately combine with the most recent term before any final sum.

Thus high-precedence operations are completed inside the stack, while low-precedence operations wait until `sum(stk)`. No explicit operator-precedence table is needed.

Equal-precedence operations remain left-associative because each boundary immediately applies the previous operator to the accumulated left term.

For example, `8/4*2` first replaces eight with two when the multiplication boundary is reached, then multiplies that stored two by the final operand. The result is four, matching left-to-right evaluation rather than interpreting it as `8/(4*2)`.

**Truncate division toward zero**

Python’s floor-division operator would round negative results downward, which is wrong for this contract. The code computes ordinary division and converts with `int(...)`, which truncates toward zero.

Intermediate values are guaranteed within 32-bit range, where the floating representation used by this expression retains enough integer precision for these divisions.

**Handle a closing parenthesis**

Character `)` is included among operand boundaries, so the nested call first commits its final `num` using the previous operator. It then breaks and returns the stack sum.

The outer call continues immediately after the consumed closing parenthesis.

**Handle the final character**

The condition `or not q` ensures the final operand is committed even when no trailing operator exists. When the last character is a digit, the deque has become empty after popping it, so the current number is applied.

**Trace `6-4/2`**

Six is committed under initial plus, storing `[6]`. Four is committed when slash is reached under sign minus, storing `[6,-4]`. At the end, two is applied under slash: pop negative four, divide by two, and push negative two.

The stack sum is four. This also shows left-side sign is retained through high-precedence division.


Within one level, every number is committed exactly once. Immediate multiplication and division and deferred signed addition encode the required precedence and associativity. Recursive calls replace parenthesized expressions with their correct values.

Induction on parenthesis nesting proves each `dfs` call returns the correct value of its level. The outer call therefore evaluates the complete valid expression exactly.

The deque position is shared implicitly through destructive `popleft` calls. A nested call cannot reread outer characters, and returning leaves the next outer character at the deque front. This provides the same cursor discipline as an explicit shared index.

## Complexity detail

Let `n` be the expression length. Every character is removed from the deque once and processed by one recursive level. Stack operations are constant time, so total time is `O(n)`.

Across active calls, term stacks and recursion can hold `O(n)` values in the worst case. The deque also stores `O(n)` characters, giving `O(n)` auxiliary space.

## Alternatives and edge cases

- **Shunting-yard algorithm:** Convert to postfix using operator stacks, then evaluate. It is iterative but requires more explicit machinery.

- **Recursive-descent parser by grammar levels:** Separate expression, term, and factor functions. This is very clear and avoids the signed-term trick.

- **Use `//` for division:** It is wrong for negative quotients because it floors instead of truncating toward zero.

- **Forget the end-of-input boundary:** The final number would never be applied.

- **Nested parentheses:** Each recursive call consumes exactly one matching closer.

- **Multi-digit literals:** Repeated multiply-by-ten accumulation constructs them correctly.

- **No spaces:** The local contract contains only meaningful expression characters, so no whitespace branch is needed.

- **Valid-expression guarantee:** Division by zero and unmatched parentheses require no error recovery.
