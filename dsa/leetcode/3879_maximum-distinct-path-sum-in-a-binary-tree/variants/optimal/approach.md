## General

**Treat every node as a possible first endpoint**

A tree has exactly one simple route between any two nodes. If a traversal starts at node `s`, reaching another node `t` therefore examines the only possible `s`-to-`t` path; no alternative route can produce a different value set or sum for those endpoints.

First convert the rooted binary tree into an undirected adjacency list, because a legal path may travel from a child through its parent and into another branch. Then start a depth-first search at every node. The running sum is the sum from that fixed start to the current node, and a set stores exactly the values on the active route.

When the current value is already in the active set, the route is invalid. The entire continuation beyond that node can be skipped for this start: every descendant route would still include both equal occurrences. Otherwise, add the value, update the global maximum with the new sum, and visit every neighbor except the node just used to enter.

**Backtrack one set instead of copying it**

Each stack entry is marked either as an entry or an exit. An entry adds its value and schedules a matching exit below all of its children on the stack. After every continuation from that node has finished, the exit removes the value. Sibling routes therefore see only their shared ancestors, exactly as recursive backtracking would, while the explicit stack remains safe for a 1000-node chain.

For any ordered endpoint pair, the search started at the first endpoint follows their unique route. If its values are distinct, no node on that route is pruned, its sum is evaluated at the second endpoint, and the candidate is considered. Every reported sum comes from one connected route whose maintained set has no duplicate. Consequently, the maximum examined sum is exactly the maximum valid path sum.

## Complexity detail

For each of $n$ starts, the traversal enters each node at most once, so the total time is $O(n^2)$. The adjacency list, explicit traversal stack, and active-value set each use $O(n)$ space.

The benchmark defines size as the number of nodes and uses distinct positive left chains of `8`, `24`, and `72` nodes. No route is pruned. The accepted backtracking traversal and an independent same-class traversal should exhibit quadratic scaling. A correct traversal that explicitly copies the entire active set at every reached node performs $O(n^3)$ aggregate copying on these chains and should fail only the scaling verdict.

## Alternatives and edge cases

- **Copy a set per stack entry:** This simplifies backtracking but copies a route of up to $O(n)$ values at each of $O(n^2)$ visits, producing $O(n^3)$ time in the worst case.
- **Reconstruct every endpoint path:** Finding or rebuilding the path separately for all $O(n^2)$ endpoint pairs also reaches $O(n^3)$ time.
- **Rooted downward-path dynamic programming:** Keeping only the best child contribution misses paths crossing between branches, and a scalar state cannot express which values are already present.
- **Negative values:** The answer starts from a real node rather than zero, so an all-negative tree returns its greatest node value.
- **Duplicate values:** Equal values at different nodes conflict whenever both occur on the same path, even though the nodes themselves are distinct.
- **Duplicate blocker:** Once a repeated value is met from a fixed start, continuing beyond it cannot restore distinctness and is safely pruned.
- **Single node:** Its one-node path is valid and supplies the answer directly.
- **Deep tree:** Iterative entry/exit events avoid recursion-depth failure on a maximally skewed tree.
