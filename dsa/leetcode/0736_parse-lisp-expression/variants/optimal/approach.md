## General
**Parse from one shared character cursor**

Maintain an index into the original string. A recursive call skips spaces and then reads either an atomic token or a parenthesized form. Atomic tokens beginning with a digit or minus sign are integers; other atomic tokens are variable lookups. Each character is consumed in order instead of repeatedly slicing nested substrings.

**Evaluate fixed-arity forms as they are parsed**

After an opening parenthesis, read the operator. For `add` and `mult`, recursively evaluate exactly two operands, combine their values, and consume the closing parenthesis. The cursor returned implicitly by the shared index is already positioned for the caller's next token.

**Represent lexical shadowing with value stacks**

Map each variable name to a stack of active values. Within `let`, bindings are processed from left to right: evaluate a binding expression using the environment established so far, push its value, and record the name for later cleanup. This order allows a later binding expression to use earlier bindings in the same `let`.

**Distinguish the final let expression**

A parenthesis or integer at the next position must begin the final expression. When the next token is a variable name, it is final if the following non-space character is the closing parenthesis; otherwise that name begins another variable-expression binding pair. Evaluate the final expression, then pop every name bound by this `let` in reverse order so outer shadowed values become visible again.

**Why scoping and evaluation are correct**

Each recursive call consumes exactly one grammar expression and returns its value. The top of each variable stack is precisely the nearest active lexical binding because entering a `let` pushes bindings in source order and leaving it removes exactly those pushes. Thus atomic lookups, arithmetic forms, and nested shadowing all use the value prescribed by the expression's scope; evaluating the root yields the required result.

## Complexity detail
Let `n` be the expression length. The cursor advances across each character a constant number of times, and every binding is pushed and popped once, so time is $O(n)$. Tokens, environment stacks, and recursive calls together occupy $O(n)$ space in the worst case.

## Alternatives and edge cases
- **Tokenize before parsing:** inserting separators around parentheses and parsing a token list is also linear and can simplify cursor handling, at the cost of an additional token array.
- **Copy the environment at every nested form:** immutable-style dictionaries are easy to reason about, but deeply nested `let` expressions can copy a growing scope and take $O(n^2)$ time.
- **Repeated substring evaluation:** locating matching parentheses and slicing operands independently can revisit the same characters many times.
- **Sequential rebinding:** `(let x 3 x 2 x)` evaluates to the most recently bound value.
- **Nested shadowing:** an inner binding hides an outer value only until the inner `let` ends.
- **Negative integers:** a leading minus sign identifies an integer token, not a variable.
- **Final variable expression:** a variable immediately followed by the `let` closing parenthesis is the result, not another binding name.
- **Valid-input guarantee:** every referenced variable has an active binding, and parentheses and operator arities are well formed.
