## General

**Turn the path question into two depth questions**

The distance between two tree nodes is the number of edges on their unique connecting path. In a tree, that path rises from the first node to the lowest common ancestor, then descends from that ancestor to the second node. The lowest common ancestor, usually abbreviated LCA, is the deepest node whose subtree contains both target values. A target is allowed to be its own ancestor, which matters when one target lies above the other or when `p == q`.

If `g` is the LCA, the desired path is split cleanly into two non-overlapping legs:

$$
\operatorname{distance}(p,q)
=
\operatorname{depth}_{g}(p)
+
\operatorname{depth}_{g}(q).
$$

Here each depth counts edges starting at `g`, so `g` itself has depth zero. The exact solution first finds `g` and then calls `dfs` once for each target. This decomposition avoids building parent pointers or storing complete root-to-node paths.

**How the recursive LCA search communicates information**

The helper `lca(root, p, q)` examines a subtree and returns one of two kinds of result:

- `None` means that neither requested value was found in that subtree.
- A node reference means that the subtree contains a target, or that the node is already the LCA discovered below.

The first base case returns `root` when the subtree is empty or when `root.val` equals either target. Stopping at a target is correct because a node may be an ancestor of the other target. In that situation, the target node itself must be the LCA; there is no need to search below it to produce a lower answer.

For any other node, recursion asks the left and right subtrees for their results. If the left result is absent, everything relevant found below must be represented by the right result, so the helper returns `right`. The symmetric rule applies when `right` is absent. If both results are non-null, one target was represented on each side, so the current node is the first place where their routes meet and is therefore their lowest common ancestor.

The problem guarantees that both values exist and that every node value is unique. Those guarantees make a returned target unambiguous and ensure that the top-level result `g` is a real node.

**How the depth search uses minus one**

The helper `dfs(root, v)` returns the number of edges from `root` to the unique node whose value is `v`. It returns zero when the current node already has that value. It returns minus one for an empty subtree or for a completed subtree that does not contain the value.

After recursively obtaining `left` and `right`, the condition `left == right == -1` recognizes that neither child subtree contains the target. Otherwise exactly one side contains it, because values are unique. The expression `1 + max(left, right)` keeps the nonnegative depth and adds the edge from the current node to that child. The missing side contributes minus one, so `max` safely selects the found side.

For example, if a target is the current node's left child, the recursive results are zero and minus one. The helper returns `1 + max(0, -1)`, which is one edge. Each parent on the route adds one more. Although the function searches both children before deciding, its returned number still describes only the unique successful route.

**Why searching from the LCA is useful**

The solution calls `dfs(g, p)` and `dfs(g, q)` rather than measuring both depths from the original root. Any route from the original root to either target shares the prefix ending at `g`. Starting at `g` removes that common prefix automatically, so the two returned depths can be added directly.

Consider the example with targets five and zero. Their LCA is node three. The first depth is one edge from three to five, and the second is two edges from three through one to zero. Their sum is three. For targets five and seven, the LCA is five itself. The first search returns zero and the second returns two, giving the correct distance two.

When `p == q`, `lca` stops at the unique matching node. Both depth calls return zero, so the final sum is zero without a special branch. This follows naturally from the definition of distance from a node to itself.

**Why the final result is correct**

The LCA recursion returns the deepest meeting point of the two target routes: it propagates a single relevant result upward until a node receives relevant results from both sides, while also correctly handling the case where a target is the meeting point. Starting from that node, each `dfs` returns the exact number of edges to its target by induction on the subtree height.

Every path between two nodes in a tree is unique and must pass through their LCA. Therefore it consists of exactly the two legs counted by the searches. Adding those lengths neither omits an edge nor counts an edge twice, so the returned value is precisely the required distance.

## Complexity detail

Let $N$ be the number of nodes and $H$ the tree height. The LCA search visits at most every node once, taking $O(N)$ time. Each depth search visits at most the subtree rooted at `g`. There are two such searches, but a constant number of linear traversals is still $O(N)$ overall.

The recursive calls use stack space proportional to the greatest root-to-leaf depth reached, so the precise auxiliary bound is $O(H)$. A completely skewed tree has $H=N$, giving the manifest's worst-case $O(N)$ space. A balanced tree has $H=O(\log N)$. Apart from recursion, the helpers retain only a constant amount of local state per active call.

The solution does not allocate a node map, parent map, visited set, or stored path. The returned integer and node references use constant additional space outside the call stacks.

## Alternatives and edge cases

- **One postorder traversal with depths:** Distance and LCA information can be combined into one recursive pass, but the return-state logic is less direct for beginners and does not improve the asymptotic bound.
- **Parent pointers plus graph traversal:** Build a parent map, then run BFS from one target until reaching the other. This is also $O(N)$ time but explicitly stores $O(N)$ references and requires locating both nodes.
- **Store two root-to-target paths:** Remove their common prefix and add the remaining lengths. It is conceptually simple, but allocates path lists and performs extra comparison work.
- **One target is an ancestor:** The LCA is that target, its own depth contribution is zero, and the other contribution is the downward distance.
- **Equal target values:** Uniqueness means both names identify the same node; both searches return zero.
- **Targets in different root subtrees:** Both LCA child results are non-null at the root, so the root becomes `g`.
- **Single-node tree:** The guarantees force both targets to be the root value, producing distance zero.
- **Skewed tree:** Correctness is unchanged, but recursive stack depth reaches $O(N)$ and may be practically important in Python.
- **Unique values:** The code compares `root.val` rather than node identity, so uniqueness is essential to its interpretation.
- **Minus-one sentinel:** A legitimate depth is never negative, making minus one safe for “not found.”
- **Both child searches execute:** `dfs` does not short-circuit after finding the target on one side; this affects constants but not the $O(N)$ bound.
- **Guaranteed presence:** Without the problem's guarantee, adding two minus-one results could be invalid; this implementation deliberately relies on the stated contract.
