## General

**A fixed BST level is already ordered**

An inorder traversal of a Binary Search Tree visits all node values in non-decreasing order. If that inorder sequence is restricted to nodes at one depth, their relative order remains non-decreasing. Breadth-first traversal that enqueues each left child before its right child visits a level in this same left-to-right order. Therefore the nodes gathered for any one level are already sorted by value; a separate sort is unnecessary.

**Traverse only as far as the requested level**

Maintain `current`, the nodes at one depth in left-to-right order. It starts with the root at depth `0`. To form the next level, scan `current` from left to right and append each existing left child followed by its right child. This preserves the level's spatial—and hence value—order.

When the current depth equals `level`, let `K = len(current)`. In a zero-based non-decreasing sequence, the ordinary middle index for odd $K$ and the upper of the two middle indices for even $K$ are both `K // 2`. Returning `current[K // 2].val` therefore gives exactly the required median.

If `current` becomes empty first, the requested level contains no nodes, so the answer is `-1`. Every existing level from the root through the target is generated once, and the method stops without visiting any deeper node. Together with the BST-order observation, these cases cover both possible outcomes and establish that the returned value is correct.

## Complexity detail

In the worst case, the traversal visits all $N$ nodes through the requested level, taking $O(N)$ time. The two level lists together hold at most a constant multiple of the maximum tree width $W$, so auxiliary space is $O(W)$.

The benchmark defines size as $N$ for a perfect BST and requests its widest final level. The accepted list-based traversal and an independent deque-based level traversal both scale linearly. The slower control gathers the same target values and performs quadratic insertion sorting before selecting the upper median.

## Alternatives and edge cases

- **Gather and comparison-sort:** DFS or BFS followed by sorting works for any binary tree, but it ignores the BST ordering and takes $O(N + K\log K)$ time with a general comparison sort.
- **Inorder traversal with depth tracking:** Restricting inorder output to the requested depth also obtains sorted values in $O(N)$ time, but an iterative implementation needs more bookkeeping and a recursive one can overflow on a tree of depth $2\cdot10^5$.
- **Selection after materialization:** Quickselect can find index $\lfloor K/2\rfloor$ in expected $O(K)$ time, yet the values already arrive in the needed order.
- **Root level:** For `level = 0`, the root is the only candidate and is returned immediately.
- **Even width:** Index `K // 2` intentionally chooses the larger of the two middle values.
- **Missing level:** If traversal exhausts the tree before reaching `level`, return `-1`.
- **Skewed tree:** Every existing level contains one node, so that node is its own median even when the height approaches $N$.
