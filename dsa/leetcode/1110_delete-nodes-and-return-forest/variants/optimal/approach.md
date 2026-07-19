## General
**Make deletion membership constant-time:** Convert `to_delete` to a set. Each node then needs one expected constant-time lookup instead of scanning all $D$ requested values.

**Carry whether the current position can start a tree:** Run depth-first search with an `is_root` flag. The original root starts with `is_root = True`; a child receives `True` exactly when its parent is deleted. If the current node is a candidate root and is not deleted, append it to the forest.

**Prune children before returning the current link:** Recursively process both children, passing the current node's deletion status as their `is_root` flag, and assign the returned nodes back through `node.left` and `node.right`. Return `None` when the current node is deleted; otherwise return the node itself. This postorder rewiring prevents a surviving parent from retaining a link to a deleted child.

A node is appended precisely when it survives and either has no original parent or its parent is deleted, which is exactly the definition of a remaining component root. Every other surviving node has a surviving parent and stays connected through the rewritten child link, so it must not be listed separately. Deleted nodes return `None`, while recursive results preserve every link between two surviving adjacent nodes. Thus the returned roots describe all and only the forest components.

## Complexity detail
Building the deletion set costs $O(D)$ time and space. Depth-first search visits each of the $N$ nodes once and performs expected constant-time membership and pointer work, for total $O(N+D)$ time. The set uses $O(D)$ space, recursion uses up to $O(N)$ on a skewed tree, and the forest root list can contain $O(N)$ entries, giving $O(N+D)$ total auxiliary storage.

## Alternatives and edge cases
- **List membership at every node:** It preserves correctness but may scan $D$ values per node, taking $O(ND)$ time.
- **Parent map followed by independent deletions:** Recording parents first can support arbitrary update order, but it needs extra bookkeeping to identify and detach every surviving child.
- **Breadth-first mutation:** A queue can avoid recursion depth, but it must carry the same parent-deleted/root-candidate state and carefully clear parent links.
- **Delete the original root:** Each undeleted child becomes a separate forest root.
- **Delete a leaf:** No new root is created because the deleted node has no children.
- **Delete consecutive ancestors:** A descendant becomes a root only after the nearest surviving connection above it has been removed; deleted intermediate nodes themselves never enter the forest.
- **Delete every node:** Every recursive call returns `None`, so the forest is empty.
- **Delete no nodes:** The original root is the only forest root and all original links remain intact.
- **Output order:** Different traversal orders may list roots differently; the forest structure, not root-list ordering, determines correctness.
