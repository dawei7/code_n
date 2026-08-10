## General

**Decode coordinates without building TreeNode objects**

Each three-digit integer stores three facts:

- hundreds digit: depth;
- tens digit: position within that depth;
- units digit: node value.

The tree's connections are determined entirely by depth and position. The solution therefore stores nodes in a dictionary keyed by their two-digit coordinate rather than constructing pointer-based node objects.

For encoded integer `num`:

- `num // 10` removes the units digit and gives coordinate `10 * depth + position`;
- `num % 10` gives the node value.

The comprehension:

`mp = {num // 10: num % 10 for num in nums}`

creates constant-time expected lookup from a coordinate to its value.

**Why coordinate `11` is the root**

The root is at depth one and position one, so its key is `10 * 1 + 1 = 11`. The input is guaranteed to represent a valid connected tree, so the exact traversal can begin with `dfs(11, 0)` rather than deriving the first key dynamically.

**Recover child coordinates**

Suppose a node key represents depth `d` and position `p`. The code extracts those values with:

`d, p = divmod(node, 10)`.

In a full binary-tree positioning scheme:

- the left child is at the next depth and position `2p - 1`;
- the right child is at the next depth and position `2p`.

Their keys are therefore:

`l = (d + 1) * 10 + 2 * p - 1`

`r = l + 1`.

The input tree may be sparse, so a calculated key is only a possible child. Dictionary membership tells whether the node actually exists.

**Carry the path sum downward**

`dfs(node, t)` receives the sum of values on the path before the current coordinate. If the coordinate is absent, it returns immediately.

For a present node, it adds `mp[node]` to `t`. The updated value is now the sum from the root through this node, inclusive.

This running sum avoids reconstructing a path list or summing ancestors again at every leaf.

**Recognize leaves by child absence**

A node is a leaf exactly when neither its possible left key nor its possible right key exists in `mp`.

When both are absent, the current root-to-node path is a complete root-to-leaf path. The solution adds its accumulated `t` to the nonlocal total `ans` and returns.

If at least one child exists, the node is not a leaf. The code calls `dfs` for both possible children. An absent-child call is safely ignored by the helper's first membership check, while every present child continues the path.

**A walkthrough**

For `nums = [113, 215, 221]`, the map is:

- key eleven has value three;
- key twenty-one has value five;
- key twenty-two has value one.

Traversal begins at key eleven with running sum zero. It adds three. The possible children are twenty-one and twenty-two.

Key twenty-one adds five, has no children, and contributes path sum eight. Key twenty-two adds one, has no children, and contributes path sum four. The final answer is twelve.

**Why zero-valued nodes work**

The code tests `node not in mp` and child-key membership, not whether `mp[node]` is truthy. A node whose stored value is zero is still present and traversed correctly. Using value truthiness to detect existence would incorrectly erase such nodes.

**Why every path is counted once**

The coordinate formulas reproduce the unique parent-child relationships of the represented tree. Starting at key eleven, depth-first search follows every existing child edge.

Every root-to-leaf path ends at one unique leaf. When traversal reaches that leaf, `t` contains exactly the sum of nodes on that path and is added once. Internal nodes do not add partial paths, and absent coordinates add nothing.

Conversely, every contribution comes from a present node with no present children, which is exactly a leaf. Therefore, `ans` is the sum of all and only root-to-leaf path sums.

**Why shared prefixes are handled correctly**

Two leaf paths may share several ancestor nodes. Their values should contribute once to each path. Passing `t` by value into each recursive branch naturally duplicates the prefix sum conceptually: each child receives the same ancestor total and adds its own continuation.

Integer arguments are immutable in Python, so updating `t` in one call does not mutate the sibling call's value.

## Complexity detail

Let `N` be the number of encoded nodes and `H` the represented tree height.

Building `mp` processes each encoding once, taking expected `O(N)` time. DFS visits every present node once. It may also make calls for absent children, but there are only a constant number per real node, so traversal remains `O(N)`.

The dictionary stores `N` coordinate-value entries, using `O(N)` space. Recursion depth is `O(H)`. Under the source encoding, depth is below five, but the general combined bound remains `O(N)` because the dictionary dominates.

All child calculations and hash lookups are constant-time for these bounded integer keys.

## Alternatives and edge cases

- **Construct explicit tree nodes:** Decode every coordinate, connect parent and children, then run ordinary DFS. This works but allocates objects and performs an unnecessary construction phase when the coordinate map already supports traversal.

- **Breadth-first traversal:** A queue can carry each node's running sum and add sums at leaves. It has the same `O(N)` time and space.

- **Accumulate path sums while reading sorted input:** Parent coordinates appear earlier, so a map of coordinate-to-running-sum can be built. Leaf detection still requires knowing which nodes have children.

- **Enumerate all possible depth positions:** The tree is sparse; dictionary membership lets the algorithm visit only encoded nodes instead of a full layout.

- **Single root node:** Both child keys are absent, so its value is the only path sum and is returned.

- **Only one child:** The existing branch is traversed; the absent-child call returns immediately. The internal parent is not misclassified as a leaf.

- **Zero node value:** Presence is determined by dictionary keys, so zero contributes correctly without hiding the node.

- **Root value zero:** Running sum begins and remains valid; descendant path values still accumulate normally.

- **Multiple leaves sharing ancestors:** The shared prefix value contributes to every root-to-leaf path, as required.

- **Maximum encoded depth:** Coordinate arithmetic still fits the two-digit key scheme because the contract limits depth and position.

- **Ascending input order:** The dictionary construction does not depend on it, though it is guaranteed. Connectivity and coordinate validity are the important assumptions.

- **Disconnected or malformed encoding:** The source excludes it. Nodes unreachable from key eleven would remain in the map but would not be visited by the exact method.

- **Duplicate coordinate encoding:** The dictionary would keep the last value, but valid input has one node per coordinate.

- **Using the full three-digit number as a node key:** The units digit is a value, not part of identity. Parent-child formulas must operate on depth-position coordinates only.
