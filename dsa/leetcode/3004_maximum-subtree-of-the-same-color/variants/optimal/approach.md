## General

**A parent subtree is monochromatic only through its children**

A leaf subtree contains one node and is always a same-color subtree. For an internal node `a`, its entire subtree is monochromatic exactly when every child subtree is monochromatic and every child root has the same color as `a`.

That condition naturally flows upward in a postorder depth-first traversal. The recursive function `dfs(a, fa)` returns a Boolean saying whether the whole subtree rooted at `a` is monochromatic.

**Root the undirected tree during traversal**

The input edges are undirected. The code builds adjacency list `g` in both directions. Parameter `fa` stores the parent, and neighbor `b == fa` is skipped so traversal does not immediately return across the same edge.

Starting with `dfs(0, -1)` gives the required root at node zero.

**Accumulate exact subtree sizes**

Array `size` begins with one for every node, counting the node itself. After recursively processing child `b`, the code executes `size[a] += size[b]`.

This happens whether or not the child subtree is monochromatic, because `size[a]` should represent the total number of nodes in the structural subtree. A non-monochromatic subtree may not be an answer candidate at `a`, but its size is still part of the parent’s subtree.

By postorder induction, each child size is complete before it is added, so `size[a]` becomes exact.

**Combine validity without losing earlier failures**

`ok` starts true. For every child, the update is:

`ok = ok and colors[a] == colors[b] and t`,

where `t` is the child’s returned validity.

The existing `ok` preserves failure from an earlier child. `colors[a] == colors[b]` ensures the child’s uniform color, when valid, matches the parent. `t` ensures no different color is hidden deeper in that child subtree.

After all children, if `ok` remains true, `size[a]` is a valid candidate and updates global `ans`.

**Why comparing only child-root colors is enough**

If `t` is true, every node in child `b`’s subtree has color `colors[b]`. If that equals `colors[a]`, then every node in that entire child branch matches `a`. Repeating this for every child proves the whole subtree is uniform.

If `t` is false, a deeper mismatch exists even if the two root colors match, so the parent correctly becomes invalid.


For a leaf, the loop has no children, `ok` remains true, and `size=1`. The function returns the correct validity and considers the leaf.

Assume each child call returns correct validity and size. The parent sums all child sizes plus itself, obtaining its exact subtree size. The Boolean conjunction is true exactly under the necessary-and-sufficient condition above. Therefore, the parent return and candidate update are correct.

Every node is visited as a possible subtree root, so global `ans` becomes the largest valid size.

**A confirmed recursion-depth defect**

The algorithmic postorder is linear, but the exact source uses recursive Python DFS without changing the recursion limit. The source allows $N=50{,}000$. Running the protected implementation on a legal 50,000-node path raises `RecursionError: maximum recursion depth exceeded`.

An iterative parent/order traversal followed by reverse-order processing would avoid this failure while preserving the same recurrence. The current approach description documents the correct logic and the executable robustness limitation.

**Why `ans` starts at zero**

Every nonempty tree has at least one leaf, whose subtree is valid with size one, so DFS always raises `ans` to at least one before returning. Zero is therefore a safe initial sentinel.

**Color magnitude is irrelevant**

The algorithm never allocates an array indexed by color and never compares colors by ordering. It uses equality only. Consequently, the stated color values up to $10^5$ do not affect memory or running time. Two branches with the same numeric label combine normally; different labels invalidate their common ancestor regardless of how far apart the numbers are.

## Complexity detail

With $N$ nodes, the adjacency list contains $2(N-1)$ neighbor entries. DFS visits every node and edge a constant number of times, so algorithmic time is $O(N)$.

The adjacency list, `size` array, and worst-case recursion stack use $O(N)$ space. On a path, stack depth is $N$ and exceeds ordinary Python limits long before the legal maximum; this is an execution defect despite the asymptotic bound.

## Alternatives and edge cases

- **Iterative postorder:** Build parent/order arrays, then process nodes in reverse order. It retains $O(N)$ time and avoids `RecursionError`.
- **Count colors separately in every subtree:** Recomputing maps at each node can become quadratic and stores unnecessary detail.
- **Compare only parent and child colors:** Without the child-validity Boolean, deeper mismatches would be missed.
- **Leaf nodes:** They are always valid size-one candidates.
- **All colors equal:** Every call returns true and the root size $N$ wins.
- **Only isolated valid leaves:** The answer remains one.
- **High-degree root:** The loop combines every child independently; recursion depth is shallow in a star.
- **Deep path:** The exact recursive source fails at legal scale.
- **Subtree sizes for invalid nodes:** They are still accumulated correctly because ancestors need structural size even though validity is false.
