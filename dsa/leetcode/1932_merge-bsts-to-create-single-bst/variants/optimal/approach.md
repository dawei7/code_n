## General
**Identify the only possible final root**

Record every tree by its root value and collect every value appearing as an
input leaf. Any tree whose root value appears as a leaf must eventually be
grafted into another tree. Therefore the final root must be the unique input
root whose value never appears as a leaf. If there is not exactly one such
root, consuming all trees into one result is impossible.

**Graft while validating global BST bounds**

Traverse from the candidate root while carrying the strict lower and upper
bounds imposed by all ancestors. When the traversal reaches a leaf whose value
matches an unused tree root, replace that leaf's children with the matching
root's children and remove that tree from the root map. Continue through the
newly exposed children using the same bounds.

Checking only each small input tree is insufficient: a graft can satisfy its
parent locally while violating a more distant ancestor. Reject any visited
node whose value is not strictly between its inherited bounds. An iterative
stack avoids recursion-depth failure when many small trees form a long chain.

**Require every tree to participate**

After the traversal, the root map must be empty. The traversal then proves
that every grafted node respects all ancestor bounds, while the empty map
proves that every separate tree was consumed. Conversely, any legal sequence
must start from the unique root absent from the leaf set and must graft a tree
exactly where its root value occurs as a leaf, so the traversal follows every
possible successful merge.

## Complexity detail
Building the root map and leaf set examines all $T$ supplied nodes. Each tree
root is removed at most once, and each node in the merged result is visited
once, so the total time is $O(T)$. The root map and leaf set use $O(K)$ space.
The iterative traversal stack contains at most $O(H)$ pending nodes, giving
$O(K+H)$ total auxiliary space.

## Alternatives and edge cases
- **Linear search for every matching root:** Keeping unused roots in a list
  and scanning it whenever a mergeable leaf is reached is correct, but a
  chain of $K$ trees can require $O(K^2)$ time.
- **Merge first, validate afterward:** Performing all apparent value matches
  and then checking the final BST can work, but bounds-aware traversal rejects
  invalid grafts immediately and combines validation with construction.
- A single input tree is returned unchanged because it is already a valid BST
  and requires zero operations.
- A root cycle leaves no candidate final root and must be rejected.
- More than one root absent from the leaf set means the collection has
  disconnected components that cannot all be consumed.
- A repeated leaf value does not permit reusing one input tree twice; any
  remaining duplicate node must still satisfy strict bounds and all roots must
  be consumed exactly once.
- Equality with either inherited bound is invalid because BST ordering is
  strict.
