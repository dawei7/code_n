## General

**Right associativity suggests scanning from right to left**

An expression `condition ? trueValue : falseValue` cannot be resolved until both branch expressions have been resolved. Nested ternaries associate from right to left, so scanning the input backward encounters branch results before the condition that selects between them.

The solution uses `expression[::-1]` to traverse characters in reverse and a stack `stk` to store already resolved operands/subexpressions. Colons carry no information once scan direction and stack positions are understood, so they are skipped.

**Ordinary value characters become stack operands**

Digits, `T`, and `F` may all be terminal results. When `cond` is false, any character other than `':'` or `'?'` is appended to the stack.

Scanning `T?2:3` backward, the algorithm first pushes `3`, then pushes `2`. The false branch was encountered first, and the true branch is now on top of it. This ordering is exactly what reduction needs.

**A question mark announces a pending reduction**

When the reverse scan reaches `'?'`, both branch expressions to its right have already been reduced to stack values. The code sets `cond = True` rather than reducing immediately because the condition character lies one position farther left and has not yet been processed.

The next non-separator character is guaranteed by valid syntax to be the condition `T` or `F`. Because `cond` is true, it is interpreted as an operator condition rather than pushed as an ordinary terminal.

**Select the correct stack operand**

Before condition processing, the stack top is the resolved true branch, and the item immediately below it is the resolved false branch.

For condition `T`, the code pops the true result into `x`, pops and discards the false result, then pushes `x` back. The two branch operands are replaced by their selected result.

For condition `F`, `stk.pop()` discards only the top true result. The false result was directly beneath it and remains on top of the stack, so no pop-and-push is necessary.

After either case, `cond` returns to false. The reduced expression now behaves as a single operand for any enclosing ternary farther left.

**Nested example**

Consider `F?1:T?4:5`. Reverse scanning first reaches the inner branches `5` and `4`, then its question mark and condition `T`. Those values reduce to `4`. The stack now represents the outer false branch as one operand.

Continuing left pushes outer true branch `1`; encountering the outer question mark sets `cond`, and condition `F` discards `1`, leaving `4`. The final result is correct for `F ? 1 : (T ? 4 : 5)`.

This demonstrates why right-to-left processing automatically respects right associativity without explicitly finding matching colons or building a parse tree.

**The stack invariant**

After processing any suffix while `cond` is false, the stack contains fully evaluated values of the unresolved branch expressions in that suffix, ordered so the next condition's true result is on top of its false result.

Value characters add an operand. Colons are syntactic separators and change nothing. A question mark followed by its left condition replaces exactly two complete branch operands with the selected one, preserving the invariant for the larger enclosing suffix.

Because the input is valid, every pending condition finds two operands, and every question mark is paired with a condition. After the full scan, the entire expression has reduced to one value, returned as `stk[0]`.

**Why single-character terminal values matter**

The parser treats each digit or Boolean character as one operand. This is correct because the contract restricts numbers to one digit and final values to a single character. Supporting multi-digit values would require tokenization rather than raw character iteration.

## Complexity detail

Let $n$ be the expression length. The reversed slice `expression[::-1]` takes $O(n)$ time and allocates an $O(n)$ string. The loop processes each character once, and every stack item is pushed/popped a constant number of times, so total time is $O(n)$.

The stack can hold $O(n)$ operands in a deeply nested expression, and the reversed string copy also uses $O(n)$ space. Auxiliary-space complexity is $O(n)$.

## Alternatives and edge cases

- **Forward recursive descent:** Parse one condition and recursively parse its true/false expressions while tracking matching separators. It can be linear with a shared index but may use $O(n)$ recursion depth.
- **Repeatedly replace the rightmost atomic expression:** Easy to visualize, but immutable string rebuilding can make it $O(n^2)$.
- **Build an explicit expression tree:** Correct but allocates nodes unnecessary when only the final selected terminal is required.
- **Constant-space focused scan:** Follow only the selected branch from left to right while counting nested `?`/`:` pairs to skip an unselected branch. It can achieve $O(n)$ time and $O(1)$ extra space but is more subtle.
- **Ignore right associativity:** Evaluating leftmost ternaries first changes expressions such as `F?1:T?4:5` and is incorrect.
- **Condition `T`:** Preserve the stack's top true result and discard the false result below it.
- **Condition `F`:** Discard the top true result, naturally exposing the false result.
- **Boolean terminal result:** A `T` or `F` not acting as the character before a pending `?` is pushed like a digit.
- **Colons:** They are skipped because branch ordering is already encoded by reverse traversal and the stack.
- **Valid-expression guarantee:** It ensures no stack underflow, unmatched delimiter, or unfinished `cond` state must be handled.
