## General

**Reduce completed subexpressions with a stack**

The expression is nested. A closing parenthesis marks the moment when every operand of one operator has been seen, so the solution scans left to right and postpones evaluation until that closing marker.

The stack stores only meaningful tokens: literal results `t` and `f` plus operators `!`, `&`, and `|`. Opening parentheses and commas are structural separators, so the loop deliberately ignores them.

Nested subexpressions do not remain as raw text. When one closes, it is evaluated immediately and its single literal result is pushed. Its parent then sees that result exactly like an original `t` or `f` operand.

**Collect the operands at a closing parenthesis**

When `c == ')'`, the top of the stack contains the completed operator’s operand results. The loop pops consecutive `t` and `f` tokens, counting true results in `t` and false results in `f`.

After those literals are removed, the next stack item is the operator that opened this subexpression. Valid syntax guarantees this arrangement and guarantees at least one operand.

Only counts are needed. AND cares whether any false value exists, OR cares whether any true value exists, and NOT has exactly one operand. Their original ordering does not affect the Boolean result.

**Apply the operator**

For `!`, the code produces true when `f` is nonzero and false otherwise. Since NOT has exactly one operand, this changes false to true and true to false.

For `&`, any false operand makes the result false. If `f` is zero, every operand was true, so the result is true.

For `|`, any true operand makes the result true. If `t` is zero, every operand was false.

The resulting character is pushed onto the stack, replacing the whole parenthesized expression with one value. This is the key invariant: after processing any prefix, the stack represents operators still waiting for closure and literal results of all completed children.

**Finish at one literal**

Every closing parenthesis reduces one operator and its operands to one literal. For a top-level literal input, no reduction is needed and that literal was pushed directly. Because the full expression is valid and represents one Boolean value, scanning the complete string leaves its result at `stk[0]`.

Comparing that character with `'t'` converts the internal representation to the required Python Boolean.

Correctness follows by structural induction. Literal expressions are pushed with their true meanings. If every immediate child has already been reduced correctly, the closing-parenthesis rules apply the specified operator to exactly those child values, producing the correct parent value. Therefore, the final reduced root is correct.

The stack order also prevents operands from crossing expression boundaries. The operator for the innermost unfinished expression sits immediately below all of its already reduced children. An enclosing operator is farther down the stack, so popping only consecutive literals stops at precisely the correct operator. After reduction, the single pushed literal occupies the same logical position that the complete child expression previously held.

This compression preserves meaning while discarding syntax that can no longer affect any future evaluation.

## Complexity detail

Let $n$ be the expression length. Every relevant token is pushed once and popped at most once. Although a closing parenthesis may pop many operands, those tokens never reappear, so the total stack work across the full scan is $O(n)$.

The stack can hold $O(n)$ operators and values in a deeply nested or operand-heavy expression, giving $O(n)$ space. The counters and current character use constant additional storage.

No substring copying, recursive parsing, or repeated rescanning occurs, which keeps the bound linear even at the maximum expression length.

## Alternatives and edge cases

- **Recursive descent:** Parse one expression at a time and return its Boolean value plus the next index. This follows the grammar directly but can reach deep recursion.
- **Replace innermost text repeatedly:** Search for closing parentheses and rewrite strings. Immutable string construction and repeated scans can lead to quadratic time.
- **Store every punctuation token:** A conventional stack parser can push parentheses and commas too, but they carry no information needed by this reduction.
- **Single literal `t`:** It remains the only stack value and returns true.
- **Single literal `f`:** It remains the only stack value and returns false.
- **NOT:** Valid syntax supplies exactly one operand, making the “any false” check equivalent to negation.
- **One-operand AND or OR:** Both return that operand, and the count tests handle them naturally.
- **Many operands:** Only two counters are needed regardless of count because AND and OR short semantic summaries are sufficient.
- **Nested operators:** Each child is reduced before its parent closes, so the parent receives literals rather than unresolved syntax.
- **Commas:** They merely separate operands and are safely ignored.
- **Valid-input guarantee:** The code does not defend against an empty stack, missing operator, or malformed arity; those cases are outside the contract.
- **Python pattern matching:** Every popped operator is one of the three handled cases, so `c` is always assigned a result before being pushed.
