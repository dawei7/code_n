## General
**Give every ungrouped item its own block.** An item labeled `-1` has no contiguity obligation with any other ungrouped item. Assigning each such item a fresh group identifier therefore preserves every valid answer while making every item belong to exactly one group.

**Separate the two kinds of precedence.** For every relation from `previous` to `current`, add an edge to an item graph. This graph captures the exact order required among individual items. If the endpoints belong to different groups, also add an edge from `group[previous]` to `group[current]` in a group graph. Parallel group edges are harmless: each contributes once to the indegree and is removed once during traversal.

**Topologically sort both graphs.** Kahn's algorithm repeatedly removes a zero-indegree vertex and releases its outgoing edges. If it cannot emit every item, the original dependencies contain an item cycle. If it cannot emit every group, the cross-group requirements force a group cycle. Either condition makes a valid answer impossible.

**Combine compatible orders.** Bucket the items according to their groups while visiting them in item topological order. Then visit groups in group topological order and append each group's bucket. The group order makes every block contiguous and respects every cross-group edge. Within a block, the item topological order respects every same-group edge. A cross-group item edge is also respected because its source block precedes its destination block, so the combined result satisfies all dependencies.

## Complexity detail
Assigning groups and building the two graphs takes $O(n+e)$ time. Their topological sorts visit $n+g$ vertices and at most $2e$ stored edges, and bucketing plus assembly takes $O(n+g)$ time. The total is $O(n+g+e)$. The graphs, indegrees, orders, and buckets occupy $O(n+g+e)$ space.

## Alternatives and edge cases
- **Depth-first topological sorting:** DFS with three-state cycle detection gives the same asymptotic bounds, but Kahn's algorithm exposes cycle detection directly through the emitted vertex count.
- **Topologically sort only items:** A valid item order can interleave two groups; regrouping it afterward may violate a cross-group dependency, so the group graph is also necessary.
- **Treat each group as one graph vertex only:** This preserves block order but loses dependencies among items inside the same group, so an item-level graph is also necessary.
- **Repeated dependency scans:** Repeatedly searching for currently eligible items is correct but can take $O(n^2+ne)$ time on a reverse chain.
- **Ungrouped items:** Each receives a distinct fresh group and may therefore appear independently.
- **Empty original groups:** They participate as isolated vertices and contribute no items when the final buckets are joined.
- **Parallel cross-group relations:** Keeping duplicate group edges is valid as long as indegrees and adjacency entries count them consistently.
- **Item cycle:** No linear ordering can satisfy all individual precedence relations, so the result is empty.
- **Group cycle without an item cycle:** The item relations may be acyclic yet require group blocks to precede one another cyclically; contiguity still makes the result impossible.
