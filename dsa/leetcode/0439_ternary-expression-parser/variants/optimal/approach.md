## General
**Process the right-associative expression from right to left**

The innermost or rightmost ternary must be resolved before a condition to its left can use its result. Scan characters in reverse and push ordinary operands and separators onto a stack.

**Reduce one complete ternary at its condition**

When the current character is `T` or `F` and the stack top is `?`, the stack already contains the complete true value, `:`, and false value in that order. Remove those markers and operands, choose the true or false value from the condition, and push the single chosen result back.

**Why every reduction respects nesting**

Reverse scanning reaches both branches of a right-associative ternary before its condition. Any ternary nested inside either branch has a condition farther right and is therefore already reduced to one operand. Thus each reduction consumes exactly one syntactically complete expression and leaves an equivalent single value for its parent. The final stack value equals the whole expression.

## Complexity detail
Each of the `n` characters is pushed or removed a constant number of times, giving $O(n)$ time. The stack can hold $O(n)$ characters for a deeply nested expression.

## Alternatives and edge cases
- **Recursive cursor parser:** parse both branches while returning the next unread index; this also takes $O(n)$ time and $O(n)$ recursion space.
- **Rescan for the matching colon:** recursively search each substring for its top-level separator; repeated scans and slices can take $O(n^2)$ on deep nesting.
- **Single operand:** return it without stack reduction.
- **Right associativity:** `a?b:c?d:e` groups the false branch as `c?d:e`.
- **Boolean terminal:** `T` or `F` may be a branch value as well as a condition.
- **Deep nesting:** an iterative stack avoids recursion-depth limits.
