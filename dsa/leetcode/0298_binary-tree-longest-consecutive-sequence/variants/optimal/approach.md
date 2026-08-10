## General

A valid path moves only from a node to one of its children, and every next value must be exactly one larger than the previous value. The path may begin anywhere, so the answer is not necessarily a path that begins at the tree's root.

The exact source uses a bottom-up depth-first search. Each recursive call first learns what paths its children can start, then decides whether the current node can be placed in front of one of those paths. A separate best-so-far value records valid paths found anywhere in the tree.

The local manifest describes carrying a parent's value and length downward, which is another valid method, but `solution.py` implements the bottom-up recurrence described here.

**What one recursive call returns**

For a real node `root`, `dfs(root)` returns the number of nodes in the longest consecutive path that:

- starts at `root` itself;
- moves only downward;
- chooses at most one child at each step;
- increases by exactly one across every chosen edge.

The phrase “starts at `root`” is crucial. A child's returned path can be extended through the current node only if the edge from current node to that child has the required value difference.

For `None`, the function returns 0. An absent child contributes no nodes. This base value lets a leaf compute a one-node path by adding its own node.

**Building the left candidate**

The statement `l = dfs(root.left) + 1` initially proposes placing the current node before the best path starting at the left child. The added 1 counts the current node.

That proposal is valid only when a left child exists and

$$
\texttt{root.left.val}-\texttt{root.val}=1.
$$

Equivalently, the child value must equal the parent value plus one. If a left child exists but the difference is anything else, the edge breaks the required sequence. The source then sets `l = 1`: a path can still start at the current node, but it cannot continue into that left child.

When the left child is absent, `dfs(None)` is 0, so the initial calculation already gives `l = 1`. The condition guarded by `root.left` does not run, and one correctly represents the path containing only the current node.

The right candidate `r` is constructed in exactly the same way from `root.right`.

**Why the two child lengths are not added**

After validating the two edges, `t = max(l, r)` selects the better downward continuation. A path in this problem cannot travel upward from a child to its parent and then downward into the other child. It must begin at some node and repeatedly move from parent to child.

Therefore, a path starting at `root` may use the left branch or the right branch, but not both. Adding `l + r` would describe a bent child-to-parent-to-child path and would also count the current node twice. Taking the maximum respects the directed path rule.

This differs from problems such as binary-tree diameter, where a valid path may connect a left descendant through a node to a right descendant. Here the direction and increasing-value requirement forbid that combination.

**Why a global answer is needed**

The value returned to a parent has a restricted purpose: it must start at the current node so the parent can decide whether to extend it. The longest path anywhere in the subtree might start below the current node and be blocked by the edge leading into it. Such a path cannot be returned as though it started at the current node.

For this reason, the source keeps `ans` outside the recursive function and declares it `nonlocal` inside. At every real node, `ans = max(ans, t)` records the best valid start-at-this-node path seen so far. The recursive return remains `t`, preserving the exact information the parent needs.

Without `ans`, returning only `dfs(root)` would miss a longest sequence that starts deeper. For example, suppose the root value is 1 and its child value is 3, followed by descendants 4 and 5. The path `3 -> 4 -> 5` has length three, but it cannot be extended to start at 1 because $3-1\ne1$. The root's own returned length is only one, while `ans` correctly retains three.

**Tracing the first example**

In the tree containing the path `3 -> 4 -> 5`, processing occurs from the leaves upward:

- Node 5 has no children, so both candidates are 1. It returns 1 and raises `ans` to 1.
- Node 4 can extend through child 5 because $5-4=1$. Its best candidate is 2, so it returns 2 and raises `ans` to 2.
- Node 3 can extend through child 4 because $4-3=1$. Its best candidate is 3, so it returns 3 and raises `ans` to 3.
- If node 3's parent is node 1, the difference is $3-1=2$, so the parent resets that branch's candidate to 1. This does not erase `ans`; the already completed path of length three remains the global best.

The second example also shows why direction matters. Values `3 -> 2 -> 1` decrease as the traversal moves downward, so those edges fail the difference-of-one check. A visually consecutive set of numbers is not enough; the values must increase by one in the permitted parent-to-child direction.

**Why every possible answer is considered**

Depth-first search visits every node. Every valid path has a unique starting node. When that starting node is processed, the recurrence examines both possible first child edges, retains every extendable child path through the appropriate candidate, and chooses the longer legal branch. Thus, `t` is the longest valid path starting at that node.

Updating `ans` with every such `t` compares the best paths for all possible starting nodes. Invalid edges are reset to length one, so no returned candidate includes a forbidden value jump. Consequently, after the traversal, `ans` is exactly the maximum length among all valid downward consecutive paths.

## Complexity detail

Let $n$ be the number of tree nodes and $h$ the tree height.

Each real node is visited exactly once. At that node, the algorithm performs two recursive-result additions, at most two edge-value checks, one maximum for `t`, and one update of `ans`. All of this local work is constant time. The total time complexity is therefore $O(n)$.

The recursion stack holds one active call per node along the current root-to-descendant route, so its depth is $O(h)$. No list, map, or per-node memo table is created. Auxiliary space is therefore $O(h)$.

For a balanced tree, $h=O(\log n)$. For a completely skewed tree, $h=O(n)$, so the worst-case auxiliary space becomes $O(n)$. The returned integer from each call and the scalar variables `l`, `r`, and `t` use constant space per active stack frame.

## Alternatives and edge cases

- **Top-down DFS:** Pass the parent value and current streak length into each child. Continue the streak when the child equals parent plus one; otherwise reset it to one. This matches the manifest summary and has the same $O(n)$ time and $O(h)$ stack space, but it is not the exact source's recurrence.
- **Iterative DFS with explicit state:** Store tuples containing a node, its parent value, and the incoming streak length. This avoids Python recursion-depth limits while preserving $O(n)$ time and $O(h)$ typical stack storage, with up to $O(n)$ in a broad or skewed tree.
- **Breadth-first traversal:** A queue can carry the path length reaching each node. It is correct, but its queue can hold an entire wide level and the top-down state is less directly aligned with this source.
- **Adding left and right candidates:** This is incorrect because it creates a path that moves from one child up to the parent and down to the other child. Only one downward child may continue a path.
- **Using absolute difference one:** The condition is directional. A child smaller by one must not continue the sequence; only `child.val - parent.val == 1` is valid.
- **Returning the subtree's global maximum:** A parent needs a path that begins exactly at its child. Returning a deeper path that does not start there could allow the parent to join disconnected values incorrectly.
- **Leaf node:** Both recursive child calls return zero, so the leaf returns one. Every single node is a valid path of length one.
- **Empty root:** Although the stated tree contains at least one node, the source handles `None`: the traversal returns zero and `ans` remains zero.
- **All equal values:** Every parent-to-child difference is zero. Each edge resets the candidate, so the answer is one.
- **Strictly decreasing chain:** No downward edge qualifies, even if values decrease by exactly one. The answer is one.
- **Strictly increasing chain by one:** Every edge extends the child result. A chain of $n$ nodes produces answer $n$.
- **A break followed by a long sequence:** The candidate resets at the break, while `ans` still records the long sequence that begins below it.
- **Negative node values:** Subtraction works identically for negative values. For example, `-3 -> -2 -> -1` is valid because each child-parent difference is one.
- **Duplicate branches of equal length:** `max(l, r)` may choose either numeric length because the function returns only the length, not the actual path.
- **Large skewed tree:** The algorithmic space is $O(h)$, but a height near $3\cdot10^4$ can exceed Python's default recursion limit. An explicit stack is the robust iterative adaptation when runtime recursion limits are part of the environment.
