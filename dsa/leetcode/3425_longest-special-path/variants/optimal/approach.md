## General

Root the tree at node `0` and perform a depth-first traversal. At any enter event, the active DFS branch is exactly one root-to-current-node path. This turns the uniqueness condition into the familiar longest unique window problem, except the window lies along tree depth rather than an array index.

Maintain `last_depth[value]`, the most recent depth at which each value occurs on the active branch. Also carry a left boundary: the shallowest depth that may begin a special path ending at the current node. If the current value last appeared at depth $p$, advance the boundary to at least $p+1$. Because the boundary never moves upward while descending one branch, every value inside the resulting suffix is unique.

Store the root-to-node distance at every active depth. If the current node has depth $d$, total root distance $D_d$, and the unique window starts at depth $L$, its weighted length is $D_d-D_L$ and its node count is $d-L+1$. Positive edge lengths mean that, among valid starts for this endpoint, the shallowest allowed start gives the greatest length. Compare that candidate with the global best and minimize its node count on a length tie.

An explicit stack holds both enter and exit events. Enter events update the sliding window and push children; exit events restore the previous occurrence of the node value and remove its distance from the active path. This restoration is what keeps sibling branches independent. Every node and edge is processed a constant number of times.

## Complexity detail

Building the adjacency list and traversing the tree each take $O(n)$ time. Dictionary lookup and update are expected $O(1)$. The graph, explicit DFS stack, active distance path, and last-occurrence map together use $O(n)$ space. The explicit stack also avoids recursion overflow on a legal 50,000-node chain.

## Alternatives and edge cases

- **Restart DFS from every ancestor:** Enumerating every downward path is correct but takes $O(n^2)$ time on a chain.
- **Recursive sliding-window DFS:** It has the same asymptotic bounds, but a maximally deep legal tree can exceed Python's call-stack capacity unless recursion is managed carefully.
- **Global visited-value set:** A set can detect duplicates but cannot identify how far the left boundary must move after a repeat; the most recent depth is required.
- **Sibling restoration:** A value recorded in one child subtree must be restored on exit or it will incorrectly constrain paths in another subtree.
- **Equal maximum lengths:** Compare node counts only after weighted lengths tie; edge weights mean fewer nodes do not imply a shorter path.
- **All adjacent values equal:** No multi-node path is special, so the correct result is `[0,1]`.
