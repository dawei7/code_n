## General
**A parent can be decided only after both children**

Postorder DFS returns whether each child subtree is univalue. A node qualifies only when both children qualify and every existing child root equals the node value.

When a call returns true, every node in that call's subtree equals its root value; the running count includes every qualifying subtree already completed.

**Each qualifying subtree is counted at its root**

A missing child imposes no restriction, and a leaf therefore qualifies immediately. For an existing child, both the child's entire subtree must be uniform and its root value must equal the current value. Those conditions are necessary and sufficient for every node below the current root to share its value. Incrementing at precisely those roots counts every univalue subtree once.

## Complexity detail
Every node is visited once for $O(n)$ time. Recursion stores one root-to-leaf path, giving $O(h)$ auxiliary space for tree height $h$.

## Alternatives and edge cases
- **Explicit postorder frames:** preserve $O(n)$ time and $O(h)$ space without using recursive calls, but add state-management machinery unnecessary for this runtime's legal depth.
- **Re-scan each subtree:** can take $O(n^2)$ on skewed or uniform trees.
- **Empty tree:** contributes zero because there is no subtree root to count.
- **Leaf:** always contributes one because both absent children impose no restriction.
