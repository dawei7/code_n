## General
**Summarize each subtree by its greatest downward height**

For a node, define its height as the maximum number of edges from that node down to a descendant leaf. Once every child's height is known, the node's height is one plus the largest child height, or zero for a leaf.

Any path whose highest node is the current node uses at most two child branches. Its length is the sum of the two greatest values `child_height + 1`; when fewer than two children exist, the missing branch contributes zero. Taking the maximum of this sum over all nodes considers every possible diameter path, including paths that do not pass through the root.

**Evaluate children before parents without recursion**

First traverse from the root and record nodes in parent-before-child order. Process that list in reverse, so every child height is available before its parent. At each node, retain only the two largest downward candidates rather than sorting all children.

The native Accepted artifact applies this logic to node objects. The app-local adapter infers the root as the only value absent from all child lists and performs the same postorder calculation over value records. An explicit stack avoids recursion failure near the permitted depth of 1000.

## Complexity detail
The initial traversal and reverse postorder each visit every node and child edge once. Selecting the two largest child branches is constant work per edge, so total time is $O(n)$.

The traversal order, stack, and height map each store at most $n$ entries, giving $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Two graph sweeps:** from any node, find a farthest endpoint, then find the farthest node from that endpoint. This also computes a tree diameter in linear time but requires treating child links as undirected edges.
- **All-pairs searches:** running a traversal from every node is correct but takes $O(n^2)$ time.
- **Recursive height DFS:** concise, but the maximum legal depth is close to Python's default recursion limit.
- **Single node:** no edge exists, so the diameter is zero.
- **Chain:** the diameter is the chain's edge count, $n-1$.
- **Wide star:** the two deepest branches are two leaves, giving diameter 2 when at least two leaves exist.
- **One child:** the second branch is zero, so a root-to-leaf path may be the diameter.
- **Node values:** values do not influence distance; only parent-child structure matters.
