## General

**Root the tree and process children before parents**

Choose node $0$ as the root. Build an adjacency list, then traverse outward once to record each node's parent and a root-to-leaf order. Reversing that order yields an iterative postorder, avoiding recursion-depth limits on a path with up to $3 \cdot 10^4$ nodes.

Only subtree sums modulo $k$ matter. Initialize every node's remainder from its own value. During postorder, all child decisions are already complete when a node is processed.

**Cut exactly the zero-remainder subtrees**

If a node's accumulated subtree remainder is zero, that subtree can be separated from its parent as a valid component. Count it and propagate nothing upward: removing a multiple of $k$ does not alter the remainder of the remaining tree.

If the remainder is nonzero, the subtree cannot be a valid component by itself. Its connecting edge must remain, so add its remainder to the parent modulo $k$.

This decision is optimal by induction on the rooted tree. For a leaf, a zero remainder permits one component, while a nonzero remainder must join its parent. After optimally processing every child, the same statement applies to their combined remainder plus the current node. Cutting a zero-remainder subtree gains one component without changing any ancestor's feasibility, so there is never a benefit to keep it attached. A nonzero subtree cannot be cut in any valid split. Therefore every counted cut is safe and every uncounted edge is necessary at that stage.

The total tree sum is divisible by $k$, so the root's final remainder is zero and the root component is counted. The resulting count is the maximum valid number of components.

## Complexity detail

Let $n$ be the number of nodes. Building the adjacency list touches $n - 1$ edges, and the outward traversal plus postorder each visit every node and edge a constant number of times. The total time is $O(n)$. The adjacency list, parent array, order, and remainders use $O(n)$ auxiliary space.

The benchmark uses $n$ as `size` and supplies paths of 32, 128, and 512 nodes with `k = 1`, so every node becomes its own component. The indexed parent traversal scales linearly. A correct traversal that checks a growing list linearly before visiting each neighbor completes all tiers but exhibits quadratic scaling.

## Alternatives and edge cases

- **Recursive depth-first search:** Returning each subtree remainder gives the same recurrence, but a path of length $3 \cdot 10^4$ can exceed Python's recursion limit.
- **Leaf-removal queue:** Repeatedly merging nondivisible leaves and counting divisible leaves is correct, though it requires mutable degrees and careful value propagation.
- **Repeated visited-list scans:** A list can replace constant-time parent tracking but may make traversal quadratic on a long path.
- **Single node:** The guaranteed divisible total makes the lone node one valid component.
- **Zero-valued subtree:** Remainder zero is immediately separable, including a leaf whose value is zero.
- **All nodes individually divisible:** Every edge can be removed, producing $n$ components.
- **Large values:** Reducing after every addition prevents subtree sums from growing unnecessarily while preserving divisibility.
- **Root component:** It has no parent edge to cut, but its zero remainder still contributes one component.
