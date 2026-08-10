## General

**Only two ancestor values matter at each node**

A direct approach could compare every node with every ancestor on its path. In a skewed tree, one node may have almost `N` ancestors, making all comparisons quadratic.

For a fixed descendant value `v`, however, the largest absolute difference from a set of ancestor values is always achieved by one of the set's extremes: its minimum or its maximum. Values between those extremes cannot be farther from `v` than both endpoints.

If the smallest ancestor value is `mi` and the largest is `mx`, the best difference involving the current node is

$$
\max\left(\lvert v-mi\rvert,\lvert v-mx\rvert\right).
$$

Therefore, a depth-first traversal needs to carry only the minimum and maximum seen along the current root-to-node path. It never needs the entire ancestor list.

**The meaning of `mi` and `mx`**

The helper `dfs(root, mi, mx)` visits one node. At entry, `mi` and `mx` summarize the ancestor values already on the path to that node. For the initial root call, both are initialized to `root.val`. This makes the root's first comparison zero and avoids a separate special case.

The method first updates the global answer with

`max(ans, abs(mi - root.val), abs(mx - root.val))`.

At this moment, the extremes represent the path through the parent, except for the root's harmless self-initialization. Thus the differences compare the current node with actual earlier nodes on its path.

After recording those candidate differences, the code expands the path summary:

- `mi = min(mi, root.val)` makes `mi` the minimum through the current node.
- `mx = max(mx, root.val)` makes `mx` the maximum through the current node.

Those updated values are passed to both child calls because the current node is an ancestor of every node in either child subtree.

**Why update the answer before changing the extremes**

The problem requires two different nodes. If the current value were included first, comparing it with the new extremes could include a zero difference with itself. That would not cause an incorrect maximum, but updating the answer before the extremes makes the intended relationship explicit: current descendant versus earlier ancestor.

For the root, the initial extremes equal the root value because it has no ancestor. The resulting zero cannot incorrectly dominate any valid positive difference, and the tree contains at least two nodes. Once traversal reaches a child, the extremes contain at least the root, so genuine ancestor-descendant comparisons begin.

**Why the same two integers can go into both branches**

Python integers are immutable, and `mi` and `mx` are local variables in each call. Updating them does not mutate shared path state. Passing the resulting values to the left child gives that branch the root-to-left path summary; passing the same values to the right child gives the correct common prefix for the right branch.

Changes made deeper in the left recursion exist only in left-side call frames. When control returns and enters the right subtree, it uses the current node's extremes, not values discovered in the left subtree. This separation is essential because nodes in sibling subtrees are not ancestors of each other and must never be compared as an ancestor-descendant pair.

**What `nonlocal ans` accomplishes**

The variable `ans` is created in `maxAncestorDiff` and shared by every nested `dfs` call. The declaration `nonlocal ans` tells Python that assignments inside `dfs` should update that enclosing variable rather than create a new local one.

Every visited node contributes at most two candidate differences. `ans` retains the largest candidate seen anywhere in the traversal. The helper itself does not need to return a value, so encountering `None` simply returns.

**Walk through the main example**

Start at root value eight with `mi = 8` and `mx = 8`. The candidate difference is zero. The extremes remain eight.

Move to node three. Its differences from both extremes are five, so `ans` becomes five. The path extremes update to three and eight.

Move from three to node one. Comparing one with path minimum three gives two, while comparing it with path maximum eight gives seven. The answer becomes seven. The updated path extremes are one and eight.

When traversal later explores node six under three, it receives extremes three and eight, not the value one from the completed sibling branch. Its best ancestor difference is three. This shows how recursive path state prevents invalid comparisons between one and six.

On the right of the root, node ten begins with extremes eight and eight. Farther down, node thirteen or fourteen is compared only with ancestors on that right-side path. The maximum across all paths remains seven, produced by ancestor eight and descendant one.

**Why extremes are enough even when the current value lies outside them**

If `v < mi`, the farthest ancestor is `mx`, and `abs(mx - v)` captures it. If `v > mx`, the farthest ancestor is `mi`. If `mi <= v <= mx`, the farthest endpoint is whichever of `v - mi` and `mx - v` is larger.

These cases cover every ordering. An interior ancestor value lies between `mi` and `mx` and cannot have a greater distance from `v` than the farther endpoint. Discarding all non-extreme ancestors is therefore lossless for this objective.

**Why the entire answer is found**

Take any valid pair in which ancestor `a` lies above descendant `b`. When DFS reaches `b`, the path summary contains `a.val`, either as an extreme or between the extremes. If it is an extreme, its difference is checked directly. If it is interior, one of the extremes is at least as far from `b.val`, producing an equal or larger valid ancestor difference on the same path.

Thus, the maximum pair in the tree cannot be missed by retaining only extremes. Conversely, every candidate used to update `ans` compares a node with a minimum or maximum taken from its own ancestor path. No invalid cross-branch pair is introduced. The final `ans` is exactly the maximum requested difference.

**Why a traversal of all nodes is necessary**

A leaf can contain the value that creates the global maximum, and no property of its ancestors reveals that value without visiting it. DFS reaches each node once and performs the minimum constant-sized comparison needed there.

The source guarantees a nonempty tree with at least two nodes, so the exact call `dfs(root, root.val, root.val)` is safe even though the type annotation permits `None` in a more general interface.

## Complexity detail

Let `N` be the number of nodes and `H` be the tree height. Every real node is visited once. Each visit performs a constant number of absolute-value, minimum, maximum, and assignment operations. Calls on missing children also total only `O(N)`. Time complexity is therefore `O(N)`, matching the manifest.

The traversal stores no ancestor array. Its memory is the recursive call stack, with at most one frame for each node on the active root-to-current path. That is `O(H)` space. A balanced binary tree has `H = O(\log N)`, while a one-sided tree has `H = O(N)`. The shared answer and the two numeric extremes per frame do not change the bound.

## Alternatives and edge cases

- **Compare each node with every ancestor:** Carry the whole path and scan it at each node. This is intuitive but becomes `O(N^2)` on a skewed tree.
- **Return subtree minima and maxima upward:** A postorder traversal can summarize descendants, but the required relationship is directional. It must still ensure that differences pair the current node as ancestor with nodes below it. The top-down path-extreme method expresses this directly.
- **Store all root-to-leaf paths:** Enumerating paths duplicates shared prefixes and uses more memory than two running extremes.
- **Iterative depth-first search:** Store triples of node, path minimum, and path maximum in an explicit stack. It has the same `O(N)` time and `O(H)` path-oriented space while avoiding recursion limits.
- **Breadth-first search:** A queue can carry extremes for every pending node. It remains linear but may use `O(W)` memory for tree width `W`.
- **Two-node tree:** The child is compared with the root, so the result is exactly their absolute difference.
- **All values equal:** Every candidate difference is zero, and `ans` correctly remains zero even though the nodes are distinct.
- **Strictly increasing path:** The minimum stays at the root while the maximum grows. The deepest value is compared with the root and produces the largest difference.
- **Strictly decreasing path:** The maximum stays at the root and the minimum decreases, producing the symmetric result.
- **One missing child:** The `None` branch returns immediately, while the existing branch continues with the same valid path extremes.
- **Sibling extremes:** A very small value in the left subtree must not be compared with a very large value in the right subtree because neither is ancestor of the other. Local recursive arguments prevent that mistake.
- **Root initialization:** Using `root.val` for both extremes avoids artificial sentinel values that could create differences with numbers not present in the tree.
- **Large node values:** Values up to `10^5` fit comfortably in the arithmetic used here, and subtraction followed by `abs` handles either ordering.
- **Recursion depth:** With up to 5000 nodes in a skewed tree, a runtime with a limited call stack may require the iterative formulation even though the algorithmic space remains `O(H)`.
