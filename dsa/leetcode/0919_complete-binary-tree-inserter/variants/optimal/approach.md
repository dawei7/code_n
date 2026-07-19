## General
**Keep only parents that still have an opening**

In a complete tree, the next inserted node belongs to the first node in breadth-first order that has fewer than two children. Perform one breadth-first traversal during construction and append every such node to a queue. Their order is exactly the order in which they will receive future children.

**Update the queue with each insertion**

The parent is always the queue's front node. Attach the new node as its left child if that position is empty. Otherwise attach it as the right child and remove the now-full parent from the queue. The new node itself has two open child positions, so append it to the back.

This transition preserves the queue meaning: all earlier nodes are full, the front is the earliest incomplete node, and every later queued node is also incomplete in breadth-first order. Filling the earliest available child position therefore keeps the last level left-aligned, so the tree remains complete after every insertion. Returning the selected parent's value and retaining the original root then implements the two query operations directly.

## Complexity detail
The constructor visits each of the $n$ initial nodes once, taking $O(n)$ time. Each insertion performs a constant number of queue and pointer operations, and `get_root()` returns the stored root reference, so $q$ operations take $O(q)$ time after construction. The queue and the final tree together hold $O(m)$ nodes. In the app-local adapter, serializing a root snapshot costs time and output space proportional to that snapshot; this is output handling rather than data-structure maintenance.

## Alternatives and edge cases
- **Search from the root before every insertion:** A fresh breadth-first traversal finds the correct opening but can take $O(m)$ time per insertion and quadratic time over a long sequence.
- **Store every node by heap index:** Keeping the entire level-order array also identifies the parent at index `(i - 1) // 2` in constant time, but the incomplete-parent queue mirrors the native tree interface without a separate full index.
- **Queue every node:** Retaining full nodes is unnecessary; removing a parent immediately after its right child is filled keeps the queue focused on valid insertion positions.
- **One missing child:** The front parent receives its left child before its right child, which is essential to completeness.
- **Full last level:** Once a level becomes full, the next insertion automatically uses the left child position of the first node on the following parent level.
- **Duplicate values:** Shape, not value uniqueness, determines the parent, so repeated values require no special handling.
- **Root identity:** `get_root()` returns the same root object supplied to the constructor, now connected to all inserted nodes.
