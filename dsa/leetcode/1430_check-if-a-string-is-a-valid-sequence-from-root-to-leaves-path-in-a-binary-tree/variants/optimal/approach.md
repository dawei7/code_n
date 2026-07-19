## General
**Carry the array position with the traversal.** At a node paired with index `i`, fail immediately if the node is absent, `i` is outside the array, or `node.val != arr[i]`. No descendant of that state can repair a mismatched prefix.

**Enforce the leaf endpoint.** If the current value matches and the node is a leaf, accept exactly when `i` is the final array index. This single condition enforces both sides of the contract: the array cannot stop at an internal node, and a leaf cannot be accepted while unconsumed values remain.

**Explore only matching prefixes.** For a matching non-leaf node, recursively test the left and right children with `i + 1`. A successful branch describes a connected root-to-leaf path with every value aligned. Conversely, any valid path follows one of those child branches and survives every equality and endpoint check, so the traversal finds it.

## Complexity detail
Each reachable node is examined at most once before its branch either fails or continues, giving $O(N)$ worst-case time. Recursive calls follow at most one root-to-current path at a time, so the stack uses $O(h)$ space.

## Alternatives and edge cases
- **Materialize all root-to-leaf paths:** Comparing `arr` after copying every path is correct but can take $O(Nh)$ time and space on deep trees.
- **Breadth-first search:** Queue pairs of nodes and array indices; it remains $O(N)$ time but can use $O(N)$ space at a wide level.
- **Array ends at an internal node:** Return `false` even if every consumed value matched.
- **Leaf reached too early:** Return `false` while array values remain.
- **Single-node tree:** Return `true` only for a one-element array equal to the root value.
- **Duplicate values:** Track structure and depth, not merely whether the values occur somewhere in the tree.
