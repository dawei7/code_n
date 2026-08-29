## General

The required path may start and end anywhere in the binary tree, and it may bend at some node by coming up from the left subtree and continuing down into the right subtree. Every node on the path must have the same value. The answer is measured in edges, not nodes.

A direct attempt to enumerate every pair of nodes would be wasteful. The depth-first search instead computes one useful summary for each subtree and combines left and right summaries at their parent.

**The exact meaning of the recursive return value**

For a non-null node `root`, `dfs(root)` returns the maximum number of edges in a downward path that:

- begins at `root`;
- repeatedly chooses only one child at each step; and
- contains nodes all equal to `root.val`.

This path is “extendable” because the caller may attach it to the edge from `root`'s parent, provided the parent has the same value.

For `None`, `dfs` returns zero. An empty subtree contributes no downward edge.

The return value cannot describe a path that uses both children. A parent can extend through its child and continue down only one branch. A forked path would have three directions at the child and would no longer be a simple path.

**Postorder traversal provides the needed information**

At a node, the code first calls

`l, r = dfs(root.left), dfs(root.right)`.

This is postorder processing: both child subtrees are solved before the current node is evaluated. At this moment, `l` is the best same-valued chain beginning at the left child, relative to that child's own value, and `r` is the corresponding chain for the right child.

Those raw child results are not automatically compatible with the current node. The connecting edge can be used only when the child exists and its value equals `root.val`.

The code transforms `l` as follows:

`l = l + 1 if root.left and root.left.val == root.val else 0`.

If values match, the edge from `root` to its left child adds one edge to the child's downward chain. If they differ or the child is absent, no same-valued path can cross that edge, so the usable left arm is zero. The right arm is handled identically.

After these transformations, `l` and `r` have a precise new meaning: they are the lengths in edges of the longest same-valued arms that leave the current node through the left and right child.

**A path whose highest node is the current node**

A simple path can enter the current node from its left arm and leave through its right arm. Because both arms have been checked against `root.val`, every node on the combined route shares the current value.

The total number of edges in that path is

$$
l+r.
$$

No extra edge is added between the arms. Each arm already includes its edge from the current node to the corresponding child.

The nonlocal variable `ans` stores the largest complete path seen anywhere in the processed part of the tree. The statement

`ans = max(ans, l + r)`

therefore considers the best path whose highest point is this node.

“Highest point” means the node on the path closest to the tree's root. Every path in a tree has exactly one such node. If a longest univalue path lies entirely in one subtree, that subtree's recursive processing has already updated `ans`. If it crosses from a left descendant to a right descendant, the current node is its highest point and `l + r` considers it.

**Why the function returns only the longer arm**

After updating the global answer, the function returns `max(l, r)`. A caller above the current node can extend only one downward arm through the current node. Returning `l + r` would incorrectly offer a branched structure to the parent.

Choosing the longer compatible arm is always safe. Both arms begin at the same current node and use the same value; the longer one gives at least as many edges to any parent that can extend through this node.

This separation is the central tree-DP idea:

- `l + r` is a complete path candidate that may use two directions and updates the global answer;
- `max(l, r)` is a one-direction chain that can be returned upward.

**Why edge counts come out correctly**

Consider a leaf. Both recursive calls return zero, and both child-existence checks set the usable arms to zero. The path consisting only of that leaf has zero edges, so `ans` need not increase. The leaf returns zero, meaning there are no downward edges beneath it.

Now consider a parent with a same-valued leaf child. The child's `dfs` result is zero, but the parent adds one for their connecting edge. Its arm length becomes one. This is exactly the required edge count.

Thus no later conversion from node count to edge count is necessary.

**A representative trace**

For a node of value `5` whose right child also has value `5` and whose right grandchild again has value `5`, the grandchild returns zero. Its parent converts that child result into an arm of one and returns one. The top node converts the returned one into an arm of two. The chain contains three nodes but two edges, which is the correct length.

If the top node also has a left same-valued arm of length one, then `ans` considers `1 + 2 = 3`, representing a path from the left child through the top node to the right grandchild.

**Why every optimal path is found**

Take any univalue path and identify its highest node `x`.

If the path extends into both child subtrees of `x`, its left segment is no longer than the best compatible left arm `l` and its right segment is no longer than `r`. Therefore its length is at most `l+r`, which the algorithm considers at `x`.

If it extends into only one child subtree, the other arm has length zero and the same `l+r` expression still considers it. If the path is a single node, its length is zero, already represented by the initial value of `ans`.

Since every possible path has a highest node and every node is processed once, the maximum cannot be missed. Conversely, each candidate `l+r` is built only from value-matching edges, so the algorithm never counts an invalid path.

## Complexity detail

Let `N` be the number of nodes and `H` the tree height measured in active recursion levels.

Every non-null node is visited once. Its work outside recursive calls consists of a constant number of child checks, additions, comparisons, and assignments. The total running time is

$$
O(N).
$$

The algorithm does not allocate a table or collection proportional to the node count. Its auxiliary storage is the recursion stack. At most one call per level is active, so stack usage is

$$
O(H).
$$

For a balanced tree, `H = O(\log N)`. For a completely skewed tree, `H = O(N)`. The returned integers and `ans` use constant space outside that stack.

## Alternatives and edge cases

- **Start a search from every node:** One could explore same-valued paths independently from each starting node, but overlapping subtrees would be revisited and the time can become quadratic.

- **Build a graph of equal-value edges:** Removing edges whose endpoint values differ leaves connected same-value components, but finding each component's diameter requires additional graph construction. The postorder DP obtains the needed diameter-like result directly.

- **Iterative postorder traversal:** An explicit stack and a map from nodes to returned arm lengths avoid Python recursion depth concerns. The reasoning is identical but the bookkeeping is more verbose.

- **Empty tree:** `dfs(None)` returns zero, `ans` remains zero, and the method correctly returns zero.

- **Single node:** A one-node path contains zero edges, so the answer is zero.

- **All values different:** Every parent-child compatibility test fails; all arms remain zero and the result is zero.

- **All values equal:** The problem becomes the diameter of the binary tree measured in edges. The same `l+r` logic computes it.

- **Negative node values:** Equality is the only value operation. Negative values require no special handling.

- **Path need not include the root:** `ans` is updated at every node, so a best path wholly inside a deep subtree is retained.

- **One matching and one nonmatching child:** The nonmatching arm becomes zero, while the matching arm may still form the best one-sided path.

- **Do not return `l+r`:** That sum represents a finished path through the current node. Passing it upward would allow a non-simple branching path to be counted.

- **Recursion depth:** The source limits depth to `1000`. This is close to Python's common recursion limit, so an iterative postorder version can be safer at the extreme even though the algorithmic space bound remains `O(H)`.
