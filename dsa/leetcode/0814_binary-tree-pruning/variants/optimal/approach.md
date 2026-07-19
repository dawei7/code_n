## General
**Decide only after pruning descendants**

Traverse in postorder. Recursively replace the left child with its pruned result, then do the same for the right child. At that point, a current node with value `0` represents an all-zero subtree exactly when both child references are `None`; return `None` for it. Otherwise, return the node.

For a leaf, the rule keeps `1` and removes `0`, which is correct. Inductively, each returned child is present exactly when its original subtree contained a `1`. The current subtree therefore contains a `1` exactly when the current value is `1` or at least one pruned child remains, matching the return condition. Applying this at the original root prunes precisely the required subtrees.

**Reuse the existing nodes**

Assign pruned children back to their parent rather than constructing a second tree. The returned structure preserves every surviving node and edge while releasing references to removed branches.

## Complexity detail
Each of the `n` nodes is visited once and performs constant work, giving $O(n)$ time. Recursive calls occupy $O(h)$ stack space for tree height `h`; no additional tree-sized structure is created.

## Alternatives and edge cases
- **Return a contains-one flag:** A helper can return both the pruned node and whether a `1` was found; postorder child references already encode that flag.
- **Iterative postorder:** An explicit stack avoids recursion depth limits but needs visitation state for each node.
- **Repeated subtree scans:** Calling a separate `contains_one` traversal before pruning each node is correct but can take $O(n^2)$ time on a skewed tree.
- **Empty tree:** Return `None` immediately.
- **All-zero tree:** Every leaf prunes, then each ancestor becomes childless and prunes in turn.
- **Zero ancestor of one:** It must remain because its subtree contains a `1`.
- **Root pruning:** The result may be an empty tree even though the input root existed.
