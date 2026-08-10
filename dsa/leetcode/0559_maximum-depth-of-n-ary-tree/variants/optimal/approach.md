## General

Maximum depth is the number of nodes on the longest root-to-leaf path. A recursive tree definition translates directly:

- an empty tree has depth zero;
- a nonempty node has depth one plus the maximum depth among its child subtrees.

The method implements exactly this recurrence.

**Empty tree base case.** If `root is None`, there is no node on any path, so the method returns zero.

This also gives a well-defined result for the source's permitted zero-node input.

**Compute child depths one at a time.** For a real node, variable `mx` begins at zero. The loop visits every node in `root.children` and recursively computes:

`self.maxDepth(child)`.

The update:

`mx = max(mx, child_depth)`

keeps only the deepest child subtree found so far. Shallower child depths cannot affect the final maximum and need not be stored after comparison.

**Count the current node.** After all children are processed, the method returns:

`1 + mx`.

The added one represents `root` itself. If the node is a leaf, its children list is empty, the loop performs no updates, and `mx` remains zero. The leaf therefore returns depth one.

For the first example, leaves two, four, five, and six return one. Node three has children five and six, so it returns two. The root sees maximum child depth two and returns three.

In a chain where every node has exactly one child, each recursive return adds one. A chain of five nodes therefore has depth five.

In a wide tree whose root has many leaf children, every child returns one, `mx` becomes one, and the root returns two regardless of how many children exist. Width does not increase depth.

**Why taking a sum of child depths would be wrong.** A root-to-leaf path chooses exactly one child at every branching node. It cannot visit two sibling subtrees without returning through their parent, which would no longer be a simple downward path. Therefore the correct combination is maximum, not sum.

**Why the recurrence finds the global deepest path.** Every root-to-leaf path in the current subtree begins at `root` and then enters exactly one child subtree. For each possible child, the longest continuation has the recursively returned child depth. Selecting the maximum continuation and adding the root gives the longest path starting at this root.

The same reasoning applies recursively to every child. Structural induction proves the returned value for the full tree.

**Why node values do not matter.** Depth depends only on parent-child links. The implementation never reads `root.val`, so negative, repeated, or missing semantic labels cannot affect path length.

**What the serialization's null markers mean.** They describe child groups in the external input format, but the platform has already built node objects and their `children` lists before this method runs. The algorithm traverses that object structure and does not parse serialization markers.

The method calls itself through `self.maxDepth` rather than a nested helper. Each call has the same base case and recurrence, and no shared mutable state is needed.

Because each call returns an integer depth rather than a node path, a parent can discard a child's internal details immediately after updating `mx`. This is the smallest summary the parent needs.

**Why every node is visited once.** A tree node has one parent except the root. Its parent's child loop invokes the method exactly once for it. There are no graph cycles in a valid n-ary tree, so no visited set is necessary.

## Complexity detail

Let $n$ be the number of nodes and $h$ the maximum depth. Every node is entered once, and every parent-child reference is examined once. The total loop work across all nodes is $O(n)$, matching the manifest.

The recursion stack contains one active frame for each node along the current root-to-descendant path, so auxiliary space is $O(h)$. A broad shallow tree uses little stack space; a one-child chain uses $O(n)$.

Only one scalar maximum is retained per active frame. No array of all depths is constructed.

The source permits depth up to 1000, which is near Python's typical default recursion limit; an iterative traversal can avoid environment-specific recursion-depth risk.

## Alternatives and edge cases

- **Breadth-first search by levels:** Count queue layers until exhaustion. It also takes $O(n)$ time but may use $O(w)$ space for maximum width.
- **Iterative DFS:** Store `(node, depth)` pairs and track the largest depth, avoiding recursion limits.
- **Sum child depths:** This incorrectly combines sibling paths that cannot belong to one downward route.
- **Empty tree:** Return zero.
- **Single node:** Empty child loop leaves `mx = 0` and returns one.
- **One-child chain:** Each level adds one, producing the node count.
- **Many leaf children:** Maximum child depth is one, so total depth is two.
- **Children with different depths:** Only the deepest child determines the answer at that node.
- **Node values:** They are irrelevant and intentionally ignored.
- **No visited set:** Valid tree structure guarantees one route to each node.
- **Depth near 1000:** An explicit stack is safer if the runtime recursion limit is not raised.
