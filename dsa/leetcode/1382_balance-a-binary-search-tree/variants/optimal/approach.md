## General
**Extract the sorted node order.** An inorder traversal of a binary search tree visits its nodes in strictly increasing value order. Use an explicit stack so a chain of up to $10^4$ nodes cannot overflow the recursion limit, and store the visited node objects in an array.

**Choose medians recursively.** For any contiguous interval of the sorted array, choose its middle node as the subtree root. Build the left subtree from the values before the midpoint and the right subtree from the values after it, replacing the node's old child links with these balanced children.

Every value appears in exactly one interval and is therefore used once. All left-interval values are smaller than their midpoint and all right-interval values are larger, establishing the BST property. Splitting each interval near its middle makes the two subtree sizes differ by at most one, which inductively keeps their heights within one.

## Complexity detail
The iterative inorder traversal and balanced reconstruction each process all $N$ nodes once, giving $O(N)$ time. The node array uses $O(N)$ space; the reconstruction depth is $O(\log N)$.

## Alternatives and edge cases
- **Create new nodes from sorted values:** It has the same bounds and result semantics, but allocates a second set of node objects instead of reusing the input nodes.
- **Repeated list concatenation:** Growing the inorder array by copying it at every visit can take $O(N^2)$ time.
- **Tree rotations:** Day-Stout-Warren balancing can achieve $O(N)$ time with $O(1)$ auxiliary space, but it is more intricate to implement correctly.
- **Already balanced:** Rebuilding is still valid even if the returned shape differs from the input.
- **Single node:** It is already balanced and remains the sole root.
- **Deep chain:** Keep the input traversal iterative; only the reconstruction recurses, and its depth is logarithmic.
- **Multiple valid answers:** Correctness depends on inorder values and height balance, not on matching one serialized shape.
