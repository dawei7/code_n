## General

**The structure is a tree plus a cycle among leaves**

Internal nodes use their `left` and `right` fields as ordinary child pointers. The leaves are special: their fields link to neighboring leaves in circular order. A normal tree traversal that follows every non-null pointer would leave the original tree at a leaf, enter the leaf cycle, and recurse forever.

The exact solution performs depth-first traversal but recognizes those reciprocal leaf links before following them. It carries depth `d` from the original root and records the largest depth seen in `ans`. Since root depth is zero, this depth is the number of tree edges from the root, exactly the problem's height definition.

**Recognize a cyclic left link by looking back**

For a normal left child `c = root.left`, `c.right` is either one of `c`'s own tree children or null. It is not a parent pointer back to `root`.

For a special leaf link, if current leaf `b_i` points left to the preceding leaf `b_{i-1}`, that preceding leaf's right link points back to `b_i`. The two pointers are reciprocal:

`root.left.right == root`.

Therefore the code follows a non-null left pointer only when

`root.left.right != root`.

When equality holds, the pointer is recognized as part of the leaf cycle and skipped.

**Recognize a cyclic right link symmetrically**

If current leaf `b_i` points right to the next leaf `b_{i+1}`, the next leaf's left link points back to `b_i`:

`root.right.left == root`.

The exact right-edge condition is therefore

`root.right and root.right.left != root`.

A genuine right child passes this check because its left field is its own tree child pointer, not a reciprocal parent link.

Together, the two tests distinguish original downward tree edges from the added horizontal/circular leaf links using only local pointer relationships.

**Why a leaf that is an ordinary child is still reached**

Suppose an internal node's genuine left child is itself a leaf. The traversal tests the child's `right` pointer against the internal parent. Special leaf pointers connect that leaf to another leaf, not back to its internal parent. Consequently `root.left.right != root` remains true and the DFS correctly descends into the leaf.

Once that leaf becomes the current `root` of the recursive call, its own left and right pointers are reciprocal with neighboring leaves, so both are skipped. The node is counted at its proper tree depth without traversing the cycle.

**Update height before examining children**

Every call executes `ans = max(ans, d)` immediately. This counts the current node regardless of whether it has ordinary children. Leaves are exactly where maximum depths may occur, so updating before skipping their special links is necessary.

The initial call uses `dfs(root, 0)` and `ans = 0`. In a tree whose deepest node is two edges below the root, recursive calls reach depths zero, one, and two, leaving `ans = 2`.

The reference guarantees at least two nodes and a non-null root, so the exact function does not include a null-root base case at entry.

**A conceptual traversal**

Imagine root 1 has children 2 and 3, and node 3 has leaf children 4 and 5. Leaves 2, 4, and 5 are circularly linked.

From root 1, pointers to 2 and 3 are genuine because neither target points reciprocally back as a special neighbor. DFS visits leaf 2 at depth one, updates the answer, and skips its two leaf-cycle links. It returns rather than walking to 4 or 5 through the cycle. DFS then visits internal node 3 and reaches leaves 4 and 5 at depth two. The maximum becomes two.

Each original tree node is reached through exactly one parent-child edge, and no leaf-neighbor edge is followed.

**Why the reciprocal test is sufficient under the special-tree contract**

The method relies on the promised structure. In an arbitrary pointer graph, a genuine child could deliberately have an opposite pointer back to its parent, or unrelated nodes could form reciprocal links. Here, fields have only two specified roles: downward child pointers on the original tree and the precisely reciprocal predecessor/successor links on leaves.

Under those guarantees, equality with the current node characterizes the leaf-cycle edge being tested. The solution does not need a visited set and does not confuse ordinary edges.

**Why the returned height is correct**

For every genuine tree edge, the reciprocal-leaf condition is false, so DFS follows it and increases depth by one. Thus every original tree node is visited at its true root-to-node edge distance. For every added leaf link, the neighboring leaf points back through the opposite field, so the condition is true and the edge is skipped. No traversal path enters the cycle.

The maximum of the true depths of all original nodes is exactly the length of the longest root-to-node path. Since `ans` records that maximum, the returned value is the tree height.

## Complexity detail

Let `n` be the number of original tree nodes and `h` its height. Every original node is visited once, and each of its two pointer fields is checked once. The reciprocal comparisons and maximum update are constant time, so total time is `O(n)`.

The solution allocates no collection. Its only growing storage is the recursion stack along one root-to-node path, which uses `O(h)` auxiliary space and can be `O(n)` for a highly skewed tree. Scalar `ans` is constant space.

Skipping cyclic links is essential to both termination and the linear bound. If those links were followed, traversal would revisit leaves indefinitely. A visited-set approach could terminate but would use `O(n)` additional storage rather than the exact solution's `O(h)` call stack.

## Alternatives and edge cases

- **Visited set:** Traverse all pointers but ignore nodes already seen. This is robust for more general graphs and still `O(n)` time, but it requires `O(n)` space and does not exploit the reciprocal-link structure.
- **Breadth-first traversal:** A queue plus the same link tests can compute maximum depth iteratively, using up to `O(n)` width storage.
- **Remove the leaf links first:** Mutating the provided structure is unnecessary and risks corrupting caller data. Local tests safely ignore them.
- **Follow every non-null pointer:** This enters the circular leaf list and never terminates.
- **One leaf:** The examples describe its special pointers as absent. If represented as self-reciprocal links, the same equality tests would also skip them.
- **Leaf reached as a tree child:** Its neighbor pointer does not point back to its internal parent, so the incoming genuine edge is not mistaken for a cycle link.
- **Root depth:** Height counts edges, so the root begins at zero rather than one.
- **Skewed tree:** Correct height can approach `n - 1`, and recursion uses `O(n)` frames.
- **Balanced tree:** Recursion storage is only `O(log n)` even though all `n` nodes are visited.
- **Null child:** The short-circuit `root.left` or `root.right` guard prevents dereferencing null.
- **Non-special arbitrary graph:** The reciprocal test is not a general cycle detector; correctness relies on the promised special-tree construction.
- **Input mutation:** The traversal only reads pointers and leaves all original child and leaf links unchanged.
