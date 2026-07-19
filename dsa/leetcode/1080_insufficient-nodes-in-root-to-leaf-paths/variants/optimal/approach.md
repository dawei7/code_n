## General
**Carry the remaining requirement downward:** When visiting a node with value `node.val`, its children need to supply a path sum of at least `need - node.val`. Passing this remaining threshold avoids rebuilding the root prefix sum.

**Decide children before parents:** Use an explicit postorder stack. The first stack entry schedules the node for a later decision and then schedules its children. The later entry sees those children after any insufficient subtrees have already been detached.

**Preserve original-leaf semantics:** Record whether the node was a leaf before processing children. An original leaf survives exactly when `node.val >= need`. An original internal node survives exactly when at least one processed child survives. This distinction prevents an internal node whose children were all removed from becoming a newly sufficient leaf.

For an original leaf, the remaining-threshold comparison is equivalent to checking its complete root-to-leaf sum. Inductively, an internal node retains precisely the child subtrees containing a qualifying original leaf and survives if at least one exists. Therefore every retained node lies on a sufficient original path, while every node intersected only by insufficient paths is detached.

## Complexity detail
Each of the $n$ nodes is pushed and resolved once, so the traversal takes $O(n)$ time. The explicit postorder stack can contain $O(n)$ entries, avoiding dependence on Python's recursion limit for a tree of height up to $n$.

## Alternatives and edge cases
- **Recursive postorder:** The same remaining-threshold recurrence is concise and uses $O(h)$ call space, but a height-$n$ tree can exceed the language recursion limit.
- **Recompute a best suffix at every node:** It is correct, but repeated subtree scans can take $O(n^2)$ time on a skewed tree.
- **Check only the current prefix:** A low prefix may later be rescued by positive descendants, so pruning before reaching original leaves is incorrect.
- **All paths insufficient:** The returned root is `null`.
- **Negative values and limit:** Comparisons must use full path sums; neither a negative node nor a negative limit changes the recurrence.
- **One surviving child:** Keep the parent and detach only the insufficient sibling subtree.
- **Internal node losing both children:** Remove it rather than treating it as a new leaf.
