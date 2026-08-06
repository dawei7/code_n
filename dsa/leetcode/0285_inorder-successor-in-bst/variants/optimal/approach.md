## General

**Greater ancestors are successor candidates**

Whenever `node.val > p.val`, the current node is a successor candidate; remember it and continue left for a smaller
candidate. Otherwise continue right because neither the current node nor its left subtree can succeed `p`.

`successor` is the smallest visited node whose value is greater than `p.val`. The chosen child is the only remaining
subtree that may contain a better candidate.

**Each branch discards values that cannot improve the candidate**

At a value greater than `p.val`, the node qualifies and everything in its right subtree is even larger, so only its
left subtree might contain a better successor. At a value no greater than `p.val`, neither that node nor its left
subtree can qualify, so only the right subtree remains relevant. The remembered minimum is therefore globally optimal
when the path ends.

## Complexity detail

Let $h$ be the tree height. The search visits at most one node per level, so it takes $O(h)$ time. The current node and
successor candidate are the only auxiliary references, giving $O(1)$ space.

## Alternatives and edge cases

- **Full inorder traversal:** takes $O(n)$ time and extra traversal storage.
- **Target has a right subtree:** the same root-based search reaches its right subtree's leftmost node without needing a
  separate case.
- **Successor is an ancestor:** each greater ancestor is retained while the search continues left for a closer value.
- **Maximum node:** no greater candidate is encountered, so the result remains `None`.
- **Skewed tree:** $h$ can equal $n$, while a balanced tree gives $h = O(\log n)$.
