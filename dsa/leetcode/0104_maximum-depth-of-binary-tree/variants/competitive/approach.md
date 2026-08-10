## General

The competitive implementation uses the canonical recursive depth formula. A real tree's longest path begins at its root, then continues through whichever child subtree is deeper. An empty reference ends a path and contributes zero nodes.

The public method is also the recursive helper: each call receives the root of a subtree and returns that subtree's maximum depth.

**Base case**

If `root is None`, the method returns zero. This handles an entirely empty input and every missing child below a leaf.

No separate leaf test is required. A leaf's two child calls both return zero, so the general expression returns one.

**Recursive expression**

For a real node, the method evaluates:

`max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1`

The two calls measure the longest paths beginning below the current node. `max` selects the longer continuation, and `+ 1` includes the current node.

Python evaluates function arguments left to right, so the left depth is computed before the right depth. The order has no semantic effect because neither call mutates shared state.

**Why a path cannot use both child depths**

A downward root-to-leaf path cannot branch. After visiting a node, it takes either the left edge or the right edge. Adding the two child depths would count nodes from two separate paths and compute something closer to a tree-size or diameter expression.

For example, if both children are leaves, adding their depths plus one would produce three, but every root-to-leaf path contains only the root and one leaf, so the correct depth is two. Taking the maximum gives that result.

**Detailed skewed-tree trace**

For `1 -> right 2 -> right 3`, the empty children of node three return zero, so node three returns one. Node two receives left zero and right one, returning two. Node one receives zero and two, returning three.

This bottom-up unwinding demonstrates why no global counter is needed. Each call returns a complete answer for its subtree, and the parent adds itself.

**Detailed branching trace**

Suppose a root has a left subtree of depth four and a right subtree of depth two. Every path through the left side contains the root plus at most four more nodes; every path through the right contains the root plus at most two. The root returns five. The shorter side must still be evaluated because its depth is not known in advance from tree values or local shape.

**Correctness reasoning**

The empty-tree answer is correct by definition. Assume both recursive child answers are correct.

Every path from the current root includes that root and then follows one child. The longest path through the left has length one plus the left depth; the analogous right path has one plus the right depth. Selecting the larger is exactly the longest path from the node.

Induction over subtree size proves that the method returns the correct value at the original root.

The algorithm ignores `val` because maximum depth depends only on links. It makes no structural or value mutation.

The return-based design also keeps calls independent. A child communicates one integer to its parent; it does not need to know the parent's depth or update a global maximum. This makes the helper reusable for any subtree and removes the need to restore shared state while unwinding.

## Complexity detail

Each of the $n$ real nodes is processed once. Calls on absent children add only constant work proportional to the number of child pointers, so time is $O(n)$.

The deepest simultaneous chain of recursive calls equals tree height $h$. Auxiliary stack space is $O(h)$, matching the manifest and source comment. This becomes $O(\log n)$ for a balanced tree and $O(n)$ for a completely skewed tree.

There is no list, map, or output structure beyond the returned integer. Each frame holds a constant number of references and intermediate results.

The two child computations occur sequentially. After the left result returns, only its integer remains while the right recursion runs. Memory is proportional to the deepest active branch, not to the number of nodes across a level and not to both subtree sizes added together.

Python's recursion limit can be lower than the allowed 10,000-node skewed height. An iterative implementation is safer when worst-case shape is possible.

## Alternatives and edge cases

- **Explicit depth-first stack:** Push each child with `depth + 1` and track the maximum. It preserves $O(n)$ time and avoids language call-stack limits.
- **Breadth-first traversal:** Each completed frontier increases a depth counter. It is intuitive but uses $O(w)$ space on wide trees.
- **Recursive accumulator:** Pass the current depth downward and update a nonlocal maximum. It has the same asymptotic costs but introduces shared state.
- **Empty tree:** Returns zero.
- **Leaf:** Returns one without a special branch.
- **One-sided tree:** Depth equals the number of nodes in the chain.
- **Two equally deep sides:** `max` returns either equal value; only the numerical depth matters.
- **Do not count edges accidentally:** The `+ 1` at every real node implements node count.
- **Large skewed input:** Prefer iteration to prevent `RecursionError`.
- **Supporting node class:** The top-level `TreeNode` definition provides fields but contributes no algorithmic work.
- **No memo table:** Each node is reachable through one parent in a tree, so recursion never solves the same node twice.
- **Path versus tree size:** A balanced tree can contain many nodes but have small depth; answer magnitude and total traversal work are different quantities.
