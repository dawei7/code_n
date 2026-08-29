## General

**Measure paths in edges, not nodes**

A ZigZag path alternates left and right child edges. Its length is the number of edges, which is one less than the number of visited nodes. The exact DFS carries edge counts, so a single starting node has length zero and moving to one child creates length one.

At each node, the helper receives two state values:

- `l` is the length of the longest alternating path ending at this node whose final move was a left edge.
- `r` is the corresponding length when the final move was a right edge.

At the initial root there is no incoming edge, so both values begin at zero. In calls below the root, normally one state is the meaningful continued length and the other is zero. Passing both makes the transition compact and symmetric.

**Why moving left continues `r`**

If the DFS moves from the current node to `root.left`, the new final edge points left. To keep alternating, the preceding edge must have pointed right. Therefore the continued length is the parent's `r + 1`. The left-child call is `dfs(root.left, r + 1, 0)`.

Its second state is reset to zero because the new path did not end with a right edge. If there was no useful right-ending path at the parent, `r` is zero and the new value becomes one. That correctly starts a fresh ZigZag containing just the current-to-left-child edge.

The right transition is the mirror image. A right edge can extend only a path whose previous edge was left, so `dfs(root.right, 0, l + 1)` passes `l + 1` as the new right-ending length.

This reset behavior is what allows a best path to begin anywhere. The DFS does not need to launch a separate search from every node. Whenever two consecutive tree edges would have the same direction, the nonmatching state is zero, and adding one automatically starts a new length-one path at the latest edge.

**Updating the answer at every real node**

The helper first returns immediately for `None`, because a missing child contributes no node and no edge. At each real node, `ans = max(ans, l, r)` records the best alternating path ending there. A globally longest path has some final node, so it will be considered when DFS reaches that node.

`nonlocal ans` allows the nested helper to update the variable created by `longestZigZag`. The traversal visits the left and right subtrees regardless of the current answer because a longer path may start deeper in either subtree.

Consider a route right, then left, then right. The root begins with states zero and zero. Its right child receives right length one. Moving left next uses that right length and produces left length two. Moving right then uses the left length and produces right length three. The answer becomes three, matching the three edges and four visited nodes.

**Why the states are sufficient**

Future continuation from a node needs only two facts: the last edge's direction and the current alternating length. Earlier node values and the full path are irrelevant. The two counters encode exactly those possibilities. Tree node values do not participate at all because the ZigZag definition depends only on edge directions.

**Why the algorithm is correct**

Inductively, whenever `dfs(node, l, r)` begins, `l` and `r` correctly describe the best alternating paths ending at `node` with the stated final directions. For a left child, any alternating path ending through the new left edge must either extend a right-ending path at the parent or consist only of this new edge. `r + 1` represents both cases because a missing continued state has value zero. The right-child transition is symmetric. Thus the invariant remains true at every descendant.

Every possible path ending at every tree node is represented by one of these states, and `ans` takes their maximum. Conversely, every positive state was formed by adding an edge in the opposite direction from the previous one, so it describes a genuine ZigZag. The maximum is therefore neither too small nor invalid, and the returned value is exactly the longest ZigZag length.

## Complexity detail

Let $N$ be the number of nodes and $H$ the tree height. Each real node is visited once and performs constant work, so time is $O(N)$. Null-child calls add at most a constant amount per edge and do not change the bound.

The algorithm stores no per-node table. Recursive calls follow one root-to-leaf route at a time, so the active stack has $O(H)$ frames. This matches the manifest. A balanced tree has $H=O(\log N)$, while a skewed tree has $H=O(N)$.

## Alternatives and edge cases

- **Bottom-up DFS:** Return the best left-first and right-first lengths from each node. It is equally linear but requires carefully translating returned child states into a global maximum.
- **Iterative stack:** Store each node with its two directional lengths. It uses $O(H)$ to $O(N)$ explicit space and avoids Python recursion-depth failures.
- **Separate search from every node:** Attempt a left-starting and right-starting path at each node. Without shared state this repeats work and can become $O(N^2)$.
- **Single node:** Both initial states are zero, so the answer correctly remains zero.
- **Only left children:** Every second left move breaks alternation. The longest valid path has at most one edge.
- **Perfect alternation in a chain:** The continued counter increases by one at every node and reaches the chain's full edge count.
- **Direction repetition:** A left edge after a left-ending path cannot continue it; the transition uses the zero right state and restarts at one.
- **Best path below the root:** Reset states naturally start new paths on deeper edges, so the root need not belong to the answer.
- **Node values:** They are intentionally ignored because only tree structure and edge directions matter.
- **Recursion limit:** With up to 50,000 nodes, a skewed tree can exceed Python's default recursion limit; an iterative stack is operationally safer.
- **Null root outside the contract:** The helper returns immediately and the method returns zero.
