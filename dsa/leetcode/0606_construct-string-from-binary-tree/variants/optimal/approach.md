## General
**Emit each node in preorder**

Append a node's value before scheduling either child representation. This fixes the root-left-right ordering required by the format.

**Preserve the left-child position**

If a left child exists, surround its representation with parentheses. If no left child exists but a right child does, append `()` so the right subtree cannot be mistaken for a left subtree.

**Omit an absent right child**

A right-child pair is added only when the right node exists. Once the left position is represented, an absent right child carries no additional structural information.

**Use explicit output actions**

Maintain a stack containing node visits and literal parenthesis tokens. Push actions in reverse output order so popping produces the serialization from left to right. Collect tokens in a list and join once, avoiding recursive string copies and call-stack depth.

**Why the representation is unambiguous**

Preorder identifies each parent before its descendants. Parentheses delimit every represented child subtree. The only potentially ambiguous case is a present right child with an absent left child, and the mandatory empty pair explicitly reserves that left position. All other missing pairs are trailing and can be omitted without changing how the string parses.

## Complexity detail
Every one of the `n` nodes is visited once and contributes a constant number of tokens. Joining the tokens processes the output once, for $O(n)$ time. The action stack and token list use $O(n)$ space.

## Alternatives and edge cases
- **Recursive token append:** directly mirrors the grammar and is linear, but a deep tree can exceed the recursion limit.
- **Recursive string concatenation:** is concise but can repeatedly copy growing subtree strings and take $O(n^2)$ time on a skewed tree.
- **Always emit both child pairs:** preserves structure but violates the minimal-parentheses requirement.
- **Leaf node:** emits only its value.
- **Left child only:** emit the left pair and omit the right pair.
- **Right child only:** emit an empty left pair before the right pair.
- **Negative value:** include its minus sign normally.
- **Deep skewed tree:** an explicit stack avoids recursive call depth.
