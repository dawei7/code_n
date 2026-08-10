## General

**Two stacks turn infix notation into a tree**

The expression arrives in infix order: a left operand, then an operator, then a right operand. A tree node for an operator cannot be completed until both of its operand subtrees are known. The solution uses:

- `nodes`, a stack of already constructed operand or expression subtrees;
- `operators`, a stack of operators and opening-parenthesis barriers.

This is the shunting-yard idea adapted to construct tree nodes rather than produce postfix text.

Operands are guaranteed to be single digits, so iterating over `s` one character at a time is sufficient. There is no need to tokenize multi-digit numbers or whitespace.

**What `combine` does**

The helper pops one operator, then pops two subtree roots:

`right = nodes.pop()`

`left = nodes.pop()`.

The pop order is crucial. The right operand was encountered later and is on top of the node stack. Reversing these assignments would change subtraction and division.

It constructs `Node(operator, left, right)` and pushes the new subtree root back on `nodes`. The subtree’s inorder traversal is the left expression, followed by the operator, followed by the right expression, so combining preserves token order.

Every call reduces the operator stack by one and the node stack by one net entry: two subtrees become one larger subtree.

**Processing operands and parentheses**

When `token.isdigit()` is true, the source creates a leaf `Node(token)`. The node value remains the digit character, matching the platform’s expression-node interface.

An opening parenthesis is pushed onto `operators`. It is not an arithmetic node; it acts as a barrier preventing outside operators from combining with the parenthesized interior too early.

On a closing parenthesis, the source repeatedly calls `combine()` until the top operator is `"("`. It then pops and discards that opening parenthesis. The entire parenthesized expression has become one subtree on `nodes`, ready to behave as a single operand in the surrounding expression.

The expression is guaranteed valid and parentheses balanced, so a matching opening barrier exists and every combination has enough operand subtrees.

**Respecting precedence**

The precedence dictionary gives addition and subtraction level one and multiplication and division level two.

When the scan encounters a new operator `token`, it first combines stacked arithmetic operators while all of these are true:

- the operator stack is non-empty;
- the top is not an opening parenthesis;
- the top operator’s precedence is greater than or equal to the incoming operator’s precedence.

A higher-precedence stacked operator must be completed before a lower-precedence incoming operator. For example, when `+` arrives after `*` in `2*3+4`, multiplication is combined first, making its subtree the left operand of addition.

If the incoming operator has higher precedence, it is pushed without combining the lower one. In `2+3*4`, `+` remains pending while `*` is pushed, so multiplication becomes the deeper subtree.

**Why equal precedence uses `>=`**

The four binary operators are left-associative. For equal precedence, the earlier operator must combine before the later one.

For `8-3-2`, encountering the second minus sees the first minus at equal precedence. The `>=` condition combines `8-3` first, then pushes the second minus. The final tree represents `(8-3)-2`.

Using only `>` would delay the first minus and construct `8-(3-2)`, changing the value. The same issue applies to division and to mixed equal-precedence pairs such as multiplication followed by division.

Parentheses override this rule because `"("` stops the while loop. Operators inside are resolved only when their closing parenthesis arrives.

**Finishing the expression**

After every character has been scanned, no future token can supply a reason to delay the remaining operators. The final `while operators` loop calls `combine()` until the stack is empty.

All parentheses have already been matched and removed by valid closing tokens, so only arithmetic operators remain. The last element of `nodes` is the root of the complete expression tree and is returned.

**Why the tree is semantically correct**

At all times, each element in `nodes` represents a contiguous portion of the expression already read, and its inorder traversal reproduces that portion without parentheses. `combine` joins adjacent left and right portions around their original operator, preserving operand and operator order.

An operator is combined exactly when parentheses, precedence, and left associativity say it must be evaluated before the incoming context. Therefore, the nesting of operator nodes matches the original expression’s evaluation rules.

At the end, one subtree spans the complete expression. Its inorder traversal reproduces `s` with parentheses omitted, every operand remains in original order, and its structure evaluates according to the required operations.

## Complexity detail

Let $N$ be the length of `s`.

Every character is scanned once. Each arithmetic operator is pushed once and popped exactly once by `combine`. Each parenthesis is pushed or discarded once, and each operand node is pushed once. Although a while loop is nested inside the scan, its total combinations across the entire run are linear. Time complexity is $O(N)$.

The two stacks can together hold $O(N)$ entries, and the constructed tree contains $O(N)$ nodes. Excluding the required returned tree, temporary stack space is still $O(N)$ in the worst case. Overall space complexity is $O(N)$.

## Alternatives and edge cases

- **Recursive descent parser:** Separate functions for expression, term, and factor naturally encode precedence and parentheses in $O(N)$ time. The two-stack source is iterative and centralizes reduction in `combine`.
- **Convert to postfix, then build a tree:** This is also correct but uses an intermediate token sequence. The checked-in method constructs subtrees during infix processing.
- **Split on the lowest-precedence operator:** Recursively searching substrings can be $O(N^2)$ and requires careful parenthesis-depth tracking.
- **Use `>` instead of `>=`:** This mishandles left associativity for equal-precedence operators, especially subtraction and division.
- **Single operand:** One leaf is pushed, no operator is combined, and that leaf is returned.
- **Fully parenthesized expression:** Each closing parenthesis completes its interior subtree; outside precedence never crosses an opening barrier.
- **Nested parentheses:** Multiple barriers remain stacked and are removed in matching last-in-first-out order.
- **Subtraction and division:** Right must be popped before left in `combine`. Swapping them changes semantics.
- **Adjacent equal-precedence operators:** Earlier operators combine first because the comparison includes equality.
- **Higher incoming precedence:** The existing lower operator stays pending so the higher-precedence operation forms a deeper subtree.
- **Single-digit contract:** Character-by-character operand recognition relies on it. Multi-digit or unary expressions would require a tokenizer and additional grammar rules.
- **Valid-expression guarantee:** The source does not defend against empty stacks, mismatched parentheses, or missing operands because the platform excludes malformed input.
- **Parentheses omitted from inorder:** They influence tree shape but are not stored as nodes, so inorder naturally emits only operands and arithmetic operators.
