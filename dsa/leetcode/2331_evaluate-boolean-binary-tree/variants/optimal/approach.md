## General

The value of an internal node depends only on the completed values of its two
children, so evaluate the tree in postorder. A leaf has no children and
returns `bool(node.val)` immediately.

**Apply the encoded operator after both subtrees**

For an internal node, recursively obtain `left_value` and `right_value`.
Value `2` means return their boolean OR; the only other legal internal value,
`3`, means return their boolean AND. Computing both values explicitly also
mirrors the definition without relying on language-level short-circuiting to
skip a subtree.

The leaf case is correct by its direct encoding. Assuming both recursive calls
correctly evaluate their smaller subtrees, applying the operator encoded at
their parent produces exactly that parent's defined value. Induction from the
leaves to the root establishes the returned result.

## Complexity detail

Let $n$ be the node count and $h$ the tree height. Each node is evaluated once,
so the running time is $O(n)$. The recursive call stack contains at most one
root-to-leaf path and uses $O(h)$ space; no other structure grows with the
tree.

## Alternatives and edge cases

- **Iterative postorder:** A stack plus a map of completed subtree values also
  takes $O(n)$ time, uses $O(n)$ space, and avoids recursion.
- **Repeated subtree evaluation:** Re-evaluating descendants whenever an
  ancestor needs them is unnecessary and can degrade to $O(n^2)$ on a
  maximally unbalanced full tree.
- **Single leaf:** The root may contain no operator at all; its `0` or `1`
  value is the complete answer.
- **Full-tree guarantee:** An internal node always has both children, so no
  missing-child semantics are required.
- **Operator values:** Only internal value `2` denotes OR; internal value `3`
  denotes AND, while the same integers never occur at leaves.
