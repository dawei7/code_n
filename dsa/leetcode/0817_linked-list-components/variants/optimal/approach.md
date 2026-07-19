## General
**Turn component counting into boundary counting**

Store the `m` selected values in a hash set, then traverse the `n` list nodes once. A selected node ends a component when its successor is absent or its successor's value is not selected. Increment the answer at exactly those endpoints.

Every induced component is a maximal consecutive run of selected nodes. Such a run has exactly one final node satisfying the endpoint test, so it contributes once. A selected node before that endpoint has a selected successor and contributes nothing, while an unselected node belongs to no component. Thus the count of selected endpoints equals the number of components.

**Use list adjacency, not numeric adjacency**

Values need not appear in sorted or numeric order. Connectivity comes only from `next` pointers in the original list, so values such as `9` and `3` are connected when their nodes are consecutive and both are selected.

**Make membership independent of selection order**

Converting `nums` to a set both ignores its input order and makes each current/next membership test constant-time on average. Scanning the list of selected values at every node would obscure the linear traversal with an additional factor of `m`.

## Complexity detail
Building the selected-value set takes $O(m)$ time and space. The linked-list traversal visits each of `n` nodes once and performs constant expected-time membership checks, for $O(n + m)$ total time and $O(m)$ auxiliary space.

## Alternatives and edge cases
- **Count component starts:** Track whether the previous node was selected and increment on an unselected-to-selected transition. It has the same complexity but requires one extra state flag.
- **Delete unselected nodes conceptually:** Relinking or constructing the induced list is unnecessary because only run boundaries matter.
- **Linear membership scans:** Checking `value in nums` while `nums` remains a list is correct but can take $O(nm)$ time.
- **One selected node:** It always forms one component.
- **All nodes selected:** The entire list is one component regardless of the order in `nums`.
- **Separated selected nodes:** Each selected node whose neighbors are unselected forms its own component.
- **Value order:** Numeric gaps or consecutive integers have no significance unless their nodes are adjacent.
