## General
**Enforce the parent rule while reading edges.** Allocate an indegree value for every node. For each nonnegative left or right child, increment that child's indegree. Reject immediately if it becomes greater than one, because a tree node other than the root cannot have multiple parents.

**Identify the unique root.** After processing all links, collect nodes with indegree zero. A valid tree has exactly one such node. Zero candidates indicates a directed cycle covering every component, while multiple candidates prove that at least two components are disconnected.

**Verify one connected acyclic traversal.** Start from the unique root and visit its nonnegative children with a stack or queue. If a node is encountered twice, reject the cycle or repeated path. Finally require exactly $n$ visited nodes. The indegree and unique-root checks constrain parentage, and the traversal proves reachability and absence of a reachable cycle; together these conditions are precisely one binary tree.

## Complexity detail
There are at most $2n$ child entries. Building indegrees and traversing all reachable nodes each take $O(n)$ time. The indegree array, visited set, and traversal stack use $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Union-find:** Union each parent-child edge while rejecting a repeated component connection, then verify one root and one component. This is near-linear but requires careful directed-parent checks in addition to connectivity.
- **Repeated parent scans:** Count a node's occurrences across both child arrays for every label. It is correct but costs $O(n^2)$ time.
- **DFS color states:** Three colors can detect directed cycles, but parent uniqueness and one-root coverage must still be checked.
- **Multiple parents:** Reject as soon as any child's indegree exceeds one, even if all nodes remain connected.
- **Disconnected cycle:** A unique apparent root elsewhere does not suffice; the final visited count detects unreachable cyclic components.
- **Single node:** With both child entries equal to `-1`, node `0` is a valid one-node tree.
- **Self-loop:** A node naming itself as a child creates a cycle and cannot form a valid tree.
