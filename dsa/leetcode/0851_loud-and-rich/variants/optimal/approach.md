## General
**Orient edges toward eligible richer people**

For every observation `[rich, poor]`, add `rich` to an adjacency list for `poor`. Following edges from a person now enumerates people definitely richer than that person. Logical consistency makes this directed graph acyclic.

**Memoize the quietest reachable representative**

Initialize `answer[person]` lazily. A depth-first search begins with the person themself as the best candidate. For every directly richer neighbor, recursively obtain that neighbor's already-complete answer. If its quietness value is smaller, replace the current candidate. Store the final person index before returning it.

Every definitely richer person is reachable along an observation chain. The recursion compares the quietest representative of each outgoing subgraph plus the starting person, so it selects the minimum quietness over exactly the eligible set. Conversely, it never visits an incomparable person. Unique `quiet` values ensure the selected index is unambiguous.

Memoization matters when richer subgraphs overlap: once a person's best representative is computed, all poorer descendants reuse it rather than traversing that subgraph again.

## Complexity detail
Each of the $n$ people is completed once, and each of the $m$ directed observations is examined once during those searches. The time is $O(n+m)$. Adjacency lists, memoized answers, and a recursion stack of at most $n$ people use $O(n+m)$ space.

## Alternatives and edge cases
- **Topological propagation:** Start with richest sources and propagate their quietest representative toward poorer neighbors in $O(n+m)$ time without recursion.
- **Fresh search for every person:** Running an independent DFS or BFS from each person is correct but can take $O(n(n+m))$ time.
- **Transitive-closure matrix:** Floyd–Warshall can determine every richer relation, but costs $O(n^3)$ time and $O(n^2)$ space.
- **No observations:** Each person's eligible set contains only themself, so every answer is its own index.
- **Single person:** The only output is `[0]`.
- **Incomplete comparisons:** A globally quieter person is irrelevant when no richer path proves that they have at least as much money.
- **Transitive relation:** A person reached through several richer edges is just as eligible as a direct neighbor.
- **Multiple richer branches:** Compare the memoized representative from every branch; the branches may later merge.
- **Quietness direction:** Smaller `quiet` values mean quieter people.
- **Unique quietness values:** No tie-breaking rule is needed.
