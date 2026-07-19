## General
**Traverse both trees in lockstep.** Put the pair `(original, cloned)` on an explicit stack. Each pair always contains nodes at the same structural position because the two roots correspond and matching left or right children are pushed together.

For every pair, compare the original-side node with `target` by object identity. When they are the same object, return the clone-side node from that pair. Otherwise continue with the matching child pairs. Since `target` is guaranteed to belong to the original tree, one visited pair must match.

The lockstep invariant proves the returned object is at precisely the target's position in the clone. Identity comparison also remains correct when two or more nodes share the same value, whereas a value-only search could return the wrong occurrence.

## Complexity detail
In the worst case the traversal examines all $N$ corresponding node pairs, so time is $O(N)$. The explicit stack contains at most $O(N)$ pairs in the worst case.

## Alternatives and edge cases
- **Record and replay the target path:** Find the root-to-target directions in the original and follow them in the clone. This is also $O(N)$ time, but requires path bookkeeping.
- **Build every node's path independently:** Repeatedly replay root paths in the clone. It is correct but can take $O(N^2)$ time on a chain.
- **Match by value:** This works only when values are unique and is invalid for the general identity-based contract.
- **Target is the root:** The corresponding answer is immediately the `cloned` root.
- **Duplicate values:** Compare original node objects with `is`, not their `val` fields.
- **Deep tree:** The iterative stack avoids recursion-depth failure on a skewed tree.
- **Existing object required:** Return a node already reachable from `cloned`, never a newly allocated copy.
