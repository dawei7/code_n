## General

**Paths may move upward, so make every tree edge bidirectional**

A root-directed recursion naturally explores ancestor-to-descendant paths. This problem also permits a path from one branch up through a parent and down another branch.

The first helper `dfs(node,p)` builds an undirected adjacency list `g`. For every non-null node, it stores its parent, left child, and right child. Child recursion passes the current node as the child's parent.

The list may include `None` for a missing parent or child. The path search checks `node is None` before doing any work, so these entries are harmless.

Tree nodes are used as dictionary keys by object identity. Values cannot identify nodes because different tree nodes may contain the same integer.

**Search the best path starting from every possible endpoint**

The second helper `dfs2(node)` returns the maximum sum of a valid path that begins at `node` and continues through at most one available neighboring direction, subject to the values already used in the current recursion path.

The set `vis` contains node values, not node objects. If `node.val` is already present, including the node would repeat a value, so the helper returns zero and does not enter that node.

Otherwise it adds the value, recursively evaluates every graph neighbor, chooses the largest extension, removes the value during backtracking, and returns

$$
\texttt{node.val}+\max(0,\text{best neighbor extension}).
$$

The source expresses the zero option by initializing `best=0` and taking maxima against recursive results.

**Why only one neighbor extension is chosen**

A path cannot branch. Once a path reaches `node` from its starting endpoint, it may leave through at most one other edge. Summing two neighbor results would create a Y-shaped connected subgraph rather than a sequence of nodes.

The helper therefore takes the maximum single neighbor. The graph is an undirected tree, so there is a unique route between nodes. The previous node's value is in `vis`, preventing immediate traversal back along the same edge. Earlier duplicate values also stop traversal, exactly as the distinctness rule requires.

**How paths crossing two child branches are still found**

Starting a search at an internal node and choosing only one neighbor would not combine its left and right branches. The outer loop compensates by starting `dfs2` at every node.

Take any valid path, including one that goes from a node in the left subtree through their ancestor into the right subtree. Orient the path from either endpoint. Starting `dfs2` at that endpoint allows the recursion to follow the unique route through the ancestor and into the other branch, always choosing one next neighbor at each node.

Thus every valid path appears as a one-directional continuation from one of its endpoints. Trying all nodes as possible starts covers all endpoints and all paths.

**Backtracking preserves branch independence**

Before descending from a node, its value is inserted into `vis`. Every recursive neighbor search sees all values on the path prefix and rejects a repetition.

After one neighbor returns, its recursive calls have removed their own values. The current node's value remains while another neighbor is explored, so sibling alternatives share only the true common prefix. After all neighbors are evaluated, removing `node.val` restores the set to exactly its caller's state.

The outer `vis.clear()` after each starting node is defensive; correct backtracking should already leave it empty. It guarantees a fresh set for the next start.

**Negative values and the option to stop**

A valid path must be nonempty, but it never has to extend into a negative contribution. `best` begins at zero, so if every legal neighbor path has a negative sum, `dfs2` returns only `node.val`.

The global answer starts at negative infinity rather than zero. If every node value is negative, a one-node path containing the least negative value must win. Initializing the answer to zero would incorrectly allow an empty path, which the contract does not permit.

For example, in a tree with values minus five and minus two, searches return at least their starting node values, and the global maximum becomes minus two.

**Why the returned value is optimal**

For a fixed start and current visited-value set, every valid continuation either stops at the current node or chooses exactly one neighbor whose value is unused. `dfs2` evaluates all those possibilities and selects the best. Induction on the remaining reachable tree establishes its return value.

Every global valid path has an endpoint that appears in the outer loop. From that endpoint, it is one of the continuations considered by `dfs2`. Conversely, every recursion route follows connected tree edges and contains no repeated value because of `vis`. The maximum over starts is therefore exactly the requested answer.

**Examples**

In `[2,2,1]`, entering a second node valued two is blocked when two is already in `vis`. A path containing one two and the node valued one remains legal and sums to three.

In the second example, a route through values one, five, and three has distinct values and sum nine. A route attempting to include both nodes valued five is pruned at the second five.

In the third example, starting at the endpoint valued nine allows the search to move through its parent six and root four. It cannot continue to the other six because that value is already in `vis`. The valid sum nineteen is retained.

**Source dependencies and recursion**

The exact code relies on `defaultdict`, `inf`, `Optional`, and the platform-provided `TreeNode`. Both tree-building and path searches are recursive.

A maximally skewed 1,000-node tree approaches Python's default recursion-depth limit. The logical algorithm is correct, but a production implementation may need an iterative traversal or an increased safe recursion limit for that boundary shape.

## Complexity detail

Building the adjacency list visits every node and edge once, taking `O(N)` time and space.

For one starting node, the backtracking search visits at most all `N` nodes and constant-many adjacency entries per node, so it is `O(N)`. Repeating for every one of `N` starts yields `O(N^2)` worst-case time.

The adjacency list, visited-value set, and recursion stack each use `O(N)` space. They are reused across starts, not multiplied by `N`, so peak auxiliary space is `O(N)`. These bounds match the manifest.

The sum may be negative or positive and can have magnitude up to about one million under the constraints, well within ordinary integer ranges.

## Alternatives and edge cases

- **Rooted downward DP only:** It misses paths that travel from one branch through a parent into another branch unless state is greatly enriched for value distinctness.
- **Enumerate every endpoint pair explicitly:** Recover the unique path and test values, which can take `O(N^3)` without reuse. Repeated-start DFS reduces this to `O(N^2)`.
- **Use node identities in `vis`:** This prevents graph cycles but does not reject different nodes carrying the same value. The set must store values.
- **Sum two best neighbors:** That creates a branched structure from a fixed starting endpoint. A path continuation selects only one; cross-branch paths are captured from an endpoint elsewhere.
- **Memoize `dfs2(node)` only by node:** Incorrect because legality and best continuation depend on the values already in `vis`.
- **All values distinct:** Every simple tree path is valid, but negative nodes may still make shorter paths preferable.
- **Duplicate value on a route:** Traversal stops before including the repeated node; it cannot skip over a node because paths must be connected.
- **Duplicate values in separate branches:** They matter only if the selected path includes both; backtracking allows either branch separately.
- **All negative:** The zero extension permits stopping, while global negative-infinity initialization ensures a nonempty one-node answer.
- **Single node:** Its graph entry is built, `dfs2` returns its value, and that is the answer.
- **Path not through root:** Starting at every node and using undirected edges covers it normally.
- **Skewed tree recursion:** Depth can reach `N`; iterative stack conversion avoids environment recursion limits.
- **Clearing `vis`:** Backtracking should empty it, and the explicit clear guarantees isolation between start nodes.
