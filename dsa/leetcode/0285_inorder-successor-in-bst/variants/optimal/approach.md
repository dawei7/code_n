## General
**Greater ancestors are successor candidates**

Whenever the current node is greater than `p`, it is a successor candidate; remember it and continue left for a smaller candidate. Otherwise continue right because neither the current node nor its left subtree can succeed `p`.

`successor` is the smallest visited value greater than `p`. The chosen child is the only remaining subtree that may contain a better candidate.

**Each branch discards values that cannot improve the candidate**

At a value greater than `p`, the node qualifies and everything in its right subtree is even larger, so only its left subtree might contain a better successor. At a value no greater than `p`, neither that node nor its left subtree can qualify, so only the right subtree remains relevant. The remembered minimum is therefore globally optimal when the path ends.

## Complexity detail
The search visits at most one node per tree level for $O(h)$ time and stores only two node references.

## Alternatives and edge cases
- **Full inorder traversal:** takes $O(n)$ time and extra traversal storage.
- The maximum node has no successor; a successor may be an ancestor rather than a child.
