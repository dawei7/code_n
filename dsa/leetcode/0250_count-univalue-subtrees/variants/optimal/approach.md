## General
**A parent can be decided only after both children**

Postorder DFS returns whether each child subtree is univalue. A node qualifies only when both children qualify and every existing child root equals the node value.

When a call returns true, every node in that call's subtree equals its root value; the running count includes every qualifying subtree already completed.

**Each qualifying subtree is counted at its root**

A missing child imposes no restriction, and a leaf therefore qualifies immediately. For an existing child, both the child's entire subtree must be uniform and its root value must equal the current value. Those conditions are necessary and sufficient for every node below the current root to share its value. Incrementing at precisely those roots counts every univalue subtree once.

## Complexity detail
Every node is visited once for $O(n)$ time. Recursion stores one root-to-leaf path, or $O(h)$ space.

## Alternatives and edge cases
- **Re-scan each subtree:** can take $O(n^2)$ on skewed or uniform trees.
- Empty trees contribute zero; null children do not invalidate an otherwise univalue subtree.
