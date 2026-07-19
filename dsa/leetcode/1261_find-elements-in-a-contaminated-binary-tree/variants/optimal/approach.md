## General
Traverse the existing tree once from the root. Assign value `0` to the root, and whenever a node with recovered value `x` has a child, compute the child's value from the stated left or right formula before adding it to the traversal stack.

**Index interpretation of recovered values**

The formulas are exactly the zero-based array indices of a binary heap. Therefore, the path from the root uniquely determines every recovered value, and no two nodes can receive the same value. Induction on depth proves the traversal assigns the required value to every existing node.

**Precompute membership for repeated queries**

Insert each recovered value into a hash set during traversal. A `find(target)` call then needs only a set-membership lookup rather than walking the tree again. The app wrapper constructs one recovered tree and reuses its set for every target in `queries`, preserving the stateful platform behavior.

Because the set contains exactly one value for every existing node and no value for a missing position, membership is true exactly for targets present in the recovered tree.

## Complexity detail
Recovery visits the $N$ nodes once, and $Q$ expected constant-time hash lookups answer the queries, for $O(N+Q)$ total expected time. The traversal stack and recovered-value set use $O(N)$ space.

## Alternatives and edge cases
- **Derive the target path per query:** The binary form of `target + 1` identifies left and right steps, allowing $O(h)$ query time and $O(1)$ preprocessing, but repeated queries cost more.
- **Linear recovered-value list:** It is easy to build, but each membership query may scan all $N$ values and produce $O(NQ)$ total time.
- **Single-node tree:** Only target `0` is present.
- **Sparse tree:** A numeric target is absent when any required child along its heap-index path is missing.
- **Repeated query:** It returns the same Boolean without changing recovered state.
- **Large absent target:** Hash lookup rejects it without traversing nonexistent levels.
