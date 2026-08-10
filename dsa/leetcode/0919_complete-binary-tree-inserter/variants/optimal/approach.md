## General

A complete binary tree has exactly the same shape as a binary heap: if nodes are listed in level order, children and parents have predictable array indices. The solution performs one initial breadth-first traversal to store all current nodes in level order, then uses index arithmetic for every insertion.

**Build the level-order array.** The constructor starts a queue with `root`. It repeatedly removes nodes from the front, appends each to `self.tree`, and enqueues its left child before its right child.

Breadth-first order processes every level before the next and preserves left-to-right order within a level. For a complete tree, the resulting array has no structural gaps. If an array index is $r$, its children, when present, occupy

$$
2r+1
\quad\text{and}\quad
2r+2.
$$

Conversely, the parent of a nonroot index $c$ is

$$
\left\lfloor\frac{c-1}{2}\right\rfloor.
$$

**Locate the next parent in constant time.** Suppose the tree currently contains `len(self.tree) = m` nodes. The newly inserted node will occupy level-order index $m$. Its parent index must be

$$
\left\lfloor\frac{m-1}{2}\right\rfloor.
$$

The code calculates exactly that before appending:

```text
p = self.tree[(len(self.tree) - 1) // 2]
```

It creates and appends the new node, preserving the level-order array.

**Choose left or right child.** In a complete tree, a parent receives its left child before its right child. The chosen parent is the first node with an open child position.

If `p.left is None`, the new node fills it. Otherwise, the parent's left child already exists and completeness guarantees its right child is the next position, so the code assigns `p.right = node`.

The inserted node's parent value is returned as required.

**Why the parent formula always selects an available position.** Array indices arrive consecutively. For odd new index $m=2r+1$, parent $r$ receives its left child. For even new index $m=2r+2$, the same parent receives its right child. After that, the next index belongs to the next parent in level order. This sequence exactly fills each level left to right.
After construction and after every insertion:

- `self.tree` contains every tree node exactly once in level order;
- its pointer structure matches the heap child-index formulas;
- the tree is complete.

The initial BFS establishes this invariant because the supplied root is complete. For insertion, the parent formula identifies the unique array parent of the next consecutive index. Attaching left for an odd child position or right for an even child position fills the earliest open slot. Appending the node preserves the level-order representation. Therefore the invariant and completeness continue to hold.

For initial tree `[1,2]`, the array length is 2. New index 2 has parent index zero, so value 3 becomes root 1's right child. The next array length is 3; new index 3 has parent index one, so value 4 becomes node 2's left child. Returned parent values are 1 and 2.

**Return the root.** The original root always remains at level-order index zero. Insertions add descendants and never replace it, so `get_root` returns `self.tree[0]` in constant time.

The data structure stores actual node objects, not copied values. The level-order array and tree pointers refer to the same nodes, so mutations performed during insertion are immediately visible through the returned root.

## Complexity detail

Let $n$ be the initial number of nodes and $q$ the number of insertions.

- **Constructor time:** $O(n)$ for breadth-first traversal.
- **Each `insert`:** $O(1)$.
- **Each `get_root`:** $O(1)$.
- **Total time:** $O(n+q)$.
- **Space complexity:** $O(n+q)$ for the level-order node array; the BFS queue uses up to the width of the initial tree during construction.

The manifest denotes current stored tree size by $m$ and states $O(m)$ space.

## Alternatives and edge cases

- **Deque of incomplete parents:** BFS can collect only nodes missing a child. Each insertion uses the front parent and removes it after filling the right child. This also gives $O(1)$ insertion with potentially smaller auxiliary storage.
- **BFS on every insertion:** It finds the first open position but costs $O(m)$ per call and repeats traversal.
- **Binary path from node count:** Bits of the new index can guide a root-to-parent path using $O(\log m)$ time and no all-node array.
- **Initial one-node tree:** First insertion fills root's left child, and the second fills its right child.
- **Parent with no children:** Left is filled first.
- **Parent with only a left child:** Right is filled next.
- **Start a new level:** After the preceding level is full, the parent formula selects the leftmost node of that level.
- **Values may repeat:** Structure and indices, not values, determine insertion.
- **Root never changes:** `get_root` always returns array index zero.
- **Nonempty input:** The constructor safely queues `root` because at least one node is guaranteed.
- **Complete-tree guarantee:** The index formulas would not identify the first structural gap in an arbitrary incomplete tree; the invariant depends on valid input.
- **Shared node references:** The array is an index over the same mutable nodes returned as a tree.
