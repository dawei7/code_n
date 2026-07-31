## General

A subtree rooted at a node is perfect exactly when both child subtrees are perfect and have equal height. Treat an empty child as a perfect tree of height zero. A leaf then has two equal empty children, so it is perfect with height one and size one.

Process nodes in postorder so both child results are known before their parent. An explicit stack stores `(node, visited)` pairs: the first visit schedules the node after its children, and the second computes its result. This avoids recursion-depth failures on a 2,000-node chain.

Store a nonnegative height for a perfect subtree and `-1` for a non-perfect subtree. If the two child heights are equal and nonnegative, the parent height is one larger. A perfect binary tree of height $h$ contains

$$
2^h-1
$$

nodes, so append that size. Otherwise mark the parent invalid; an invalid child necessarily prevents every ancestor using it from being perfect. After all nodes are processed, sort the collected sizes in descending order and select index $k-1$, returning `-1` when fewer than $k$ perfect subtrees exist.

## Complexity detail

Let $n$ be the number of nodes. Iterative postorder visits each node twice and performs constant work per visit, taking $O(n)$ time. At most $n$ perfect-subtree sizes are sorted, costing $O(n\log n)$ total time. The stack, height map, and size list use $O(n)$ space.

## Alternatives and edge cases

- **Recursive postorder:** The recurrence is concise, but a skewed legal tree can exceed Python's recursion limit.
- **Maintain a size-k heap:** This reduces ranking to $O(n\log k)$ and $O(k)$ size storage, though the height map and traversal stack remain linear and the constraints do not require the added machinery.
- **Check each subtree independently:** Recounting descendants from every root can take $O(n^2)$ time on nested perfect or skewed structures.
- **Leaves:** Every leaf is itself a perfect subtree of size one.
- **One missing child:** The child heights differ between zero and a positive value, so the parent is not perfect.
- **Duplicate sizes:** Perfect subtrees are ranked with multiplicity; two different roots of size three occupy two positions in the sorted list.
- **Insufficient subtrees:** Return `-1` rather than the smallest available size when $k$ exceeds the count.
