## Hint

**Hint 1:** Ask whether any directed cycle is reachable from `source`.

**Hint 2:** If such a cycle is reachable, the answer is `false` because a path can remain trapped in that cycle forever.

**Hint 3:** If no reachable cycle exists, inspect every node reachable from `source` and ensure that `destination` is the only reachable node with no outgoing edges.

The live source's third hint renders the terminal condition as `indegree = 0`. Under the stated edge direction `[a_i, b_i]` from `a_i` to `b_i`, a node with no outgoing edges has **outdegree** zero; this is also the terminal condition stated in the problem description.
