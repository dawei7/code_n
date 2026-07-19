## General
**Carry the two ancestor values during traversal**

Traverse the tree with an explicit stack. Alongside each node, store the value of its parent and grandparent, using null when an ancestor does not exist. When a node is removed from the stack, add its value exactly when the stored grandparent is non-null and even.

For either child, the current node becomes the child's parent and the current parent becomes the child's grandparent. Push that shifted ancestor state with the child. This local update preserves the actual two-generation relationship on every root-to-node path.

Every tree node is reached once through its unique parent. The stored grandparent is therefore exactly the parent of that unique parent, and the test includes precisely the nodes required by the contract. Nodes at depth zero or one carry a null grandparent and correctly contribute nothing.

## Complexity detail
The traversal visits each of the $n$ nodes once and performs constant work per node, taking $O(n)$ time. The explicit stack holds at most $O(n)$ entries in the worst case. On a balanced tree its maximum size is proportional to the tree height or frontier, but $O(n)$ is the general bound.

## Alternatives and edge cases
- **Recursive depth-first search:** Passing parent and grandparent values as parameters is equally linear, but a legal 10000-node chain can exceed the language recursion limit.
- **Breadth-first search:** Queue entries can carry the same two ancestor values and preserve the $O(n)$ bounds.
- **Repeated parent searches:** Locating each node's parent and then grandparent by searching from the root is correct but can take $O(n^2)$ time on a skewed tree.
- **Root and children:** They have no grandparent and never contribute, even when the root itself is even.
- **Odd parent:** A node still contributes when its grandparent is even; its parent's parity is irrelevant.
- **No qualifying node:** The accumulator remains 0.
- **Repeated values:** Nodes are counted by position and ancestry, not deduplicated by value.
