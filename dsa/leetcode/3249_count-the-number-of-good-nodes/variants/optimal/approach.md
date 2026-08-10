## General

Whether a node is good depends on the sizes of the subtrees rooted at each of its children. Those sizes are naturally computed from leaves upward: once every child reports its subtree size, the parent can compare them and add them to obtain its own size.

The input edges are undirected even though the tree is conceptually rooted at zero. The code first builds an adjacency list `g` in both directions. During DFS, arguments `a` and `fa` mean the current node and its parent. When scanning `g[a]`, the test `b != fa` keeps only rooted children and prevents walking immediately back to the parent. Because the graph is a valid tree, there is no other route to an already visited node.

The recursive function returns the size of the subtree rooted at `a`. Variable `cnt` starts at one to count `a` itself. For each child `b`, `cur = dfs(b, a)` obtains that child's complete subtree size, and `cnt += cur` accumulates it. After all children are processed, returning `cnt` gives exactly one plus the sum of child subtree sizes.

At the same time, the function determines whether all child sizes are equal. `pre` begins at minus one, a sentinel meaning no child size has been seen. The first child's `cur` becomes the reference size in `pre`. Every later child is compared with that reference. If any differs, `ok` becomes zero. It never needs to become one again because one unequal pair permanently proves the node is not good.

`ok` begins at one. This deliberately classifies leaves as good: a leaf has no child subtrees, so the statement “all child subtrees have the same size” is vacuously true. A node with exactly one child is also always good because there are no two child sizes that can disagree. The loop behavior matches both logical cases without special branches.

After processing children, the function adds `ok` to the nonlocal result `ans`. A good node adds one and a non-good node adds zero. The addition occurs in postorder, but the final count does not depend on traversal order.

For a perfect rooted binary tree where every internal node's two child subtrees have equal sizes, each leaf contributes good status automatically, each parent compares equal child sizes, and the root does the same. Every node is counted.

Consider a node with child subtree sizes two, two, and five. The first size sets `pre = 2`, the second matches, and the third changes `ok` to zero. Its own returned subtree size is still `1 + 2 + 2 + 5 = 10`. Goodness and size are separate outputs: even a non-good node must return its correct size so its parent can be evaluated.

**Why comparing everything with the first size is sufficient.** Equality is transitive. If every later child's size equals the first child's size, then every pair of child sizes is equal. If one later size differs from the first, the all-equal requirement already fails. No sorting or frequency table is needed.

**Exact implementation versus the manifest summary.** The summary says subtree sizes are accumulated in iterative postorder. The exact source uses recursive DFS. Its logical order is still postorder because each `dfs(b,a)` finishes before the parent consumes `cur`, but it relies on Python's call stack rather than an explicit order array. This distinction matters operationally for very deep trees.

The proof follows structural induction. Every leaf returns size one and is correctly good. Assuming each child returns its exact subtree size, the parent sums those disjoint child subtrees plus itself, so its returned size is exact. The comparisons test the definition of goodness using those exact sizes. Thus every node's status is counted correctly, and `ans` is the total number of good nodes after `dfs(0,-1)` completes.

## Complexity detail

Let $n$ be the number of nodes. Building `g` stores two adjacency entries for each of $n-1$ edges and takes $O(n)$ time. DFS enters each node once and examines every adjacency entry once, so traversal is $O(n)$. Total time is $O(n)$.

The adjacency list uses $O(n)$ space. In a chain, recursive depth is $O(n)$, so the call stack also uses $O(n)$ space. Total auxiliary space remains $O(n)$.

The constraint allows $n=10^5$, far beyond Python's usual recursion limit of roughly one thousand. Therefore the exact recursive source has a genuine robustness risk: a sufficiently deep valid tree can raise `RecursionError` unless the environment raises the recursion limit. An iterative parent/order traversal would preserve $O(n)$ bounds and avoid that risk; the manifest summary describes such an implementation, but the provided source does not contain it.

## Alternatives and edge cases

- **Iterative postorder:** Build parent and traversal-order arrays from root zero, then process nodes in reverse order to accumulate sizes and compare child sizes. It has the same $O(n)$ time and space and is safer for the maximum-depth chain.
- **Raise the recursion limit:** Calling `sys.setrecursionlimit` can let the recursive code handle deeper trees, but very large Python recursion still consumes substantial native stack and an iterative method is more robust.
- **Store all child sizes:** Collecting them and checking `len(set(sizes)) <= 1` is correct but allocates unnecessary lists and sets. A single reference size suffices.
- **Sort child sizes:** Sorting makes equality visible but adds $O(d\log d)$ work at a node of degree $d$ without benefit.
- **Leaf node:** It has zero children and is good by vacuous truth. `ok` remains one.
- **Exactly one child:** Any one-element collection has all equal sizes, so the node is good regardless of that child's size.
- **Root node:** Passing parent minus one means all of root zero's neighbors are treated as children, matching the specified root.
- **A chain:** Every node has at most one child and is therefore good. It is also the input most likely to trigger the recursive depth problem.
- **A star rooted at zero:** Every child is a leaf of size one, so the root and all leaves are good.
- **Unequal sizes after an early mismatch:** `ok` remains zero, but recursion and summation continue so the parent still receives the correct total subtree size.
- **Valid-tree requirement:** Merely skipping the parent is insufficient for a graph with cycles. The guarantee that `edges` forms a tree is essential to avoid infinite recursive revisits.
- **Dictionary adjacency:** `defaultdict(list)` creates lists as nodes are referenced. With valid labels and a connected tree, every node appears and is visited.
