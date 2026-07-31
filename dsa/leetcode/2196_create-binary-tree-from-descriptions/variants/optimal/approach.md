## General

**Give each value one persistent node**

Maintain a map from node value to its `TreeNode` object. For every description,
create the parent or child object only if that value has not appeared before.
Then assign the child object to the parent's left or right field according to
`isLeft`. Interning by value ensures that an object first seen as a child is
reused later when its own children are described.

**Identify the unique node without a parent**

Record every value that appears in the child position. A valid tree has
exactly one root, and it is the only created value absent from this child set.
After all links are installed, scan the node map and return that object.

Each description installs exactly its specified directed parent-child edge on
the specified side. Because equal values always retrieve the same object, all
edges that meet at a node connect the same subtree rather than copies. The
valid-tree guarantee makes the only non-child value the root, so the returned
object reaches the entire described tree.

## Complexity detail

Let $m=\lvert\texttt{descriptions}\rvert$. Hash-map and set operations take
expected $O(1)$ time per description, and the final root scan visits at most
$m+1$ nodes, for $O(m)$ total time. The nodes, value map, and child set use
$O(m)$ space.

## Alternatives and edge cases

- **Linear node lookup:** Store created nodes in a list and scan it for both
  endpoints of every description. It is correct but takes $O(m^2)$ time.
- **Recursive construction from parent searches:** Repeatedly scan all
  descriptions to discover each node's children. This can also take
  $O(m^2)$ time and risks deep recursion.
- A single description forms a two-node tree.
- The root may first appear only as a parent in a late description.
- A node may be created as a child before its outgoing edges are processed.
- Description order does not determine traversal order or root identity.
- Large node values are labels, not array indices that must be allocated
  densely.
