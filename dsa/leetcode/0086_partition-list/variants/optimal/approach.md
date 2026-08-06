## General
**Stable partitioning requires tail appends, not front insertion**

Maintain head and tail pointers for a lower chain (`value < x`) and an upper chain (`value >= x`). Visit original nodes in order. Save `next_node` before detaching the current node, set its `next` to null, and append it to the appropriate tail.

Appending in encounter order preserves stability within both groups. Detaching first prevents a chain tail from retaining a stale link to a node that will ultimately belong to the other partition.

**Join the two completed chains exactly once**

After traversal, link `lower_tail` to `upper_head`. If the lower chain is empty, return `upper_head` directly; if the upper chain is empty, the lower tail remains null-terminated and `lower_head` is the result.

**Each processed node belongs to exactly one stable chain**

After processing any prefix, the two chains contain exactly its nodes classified by the pivot, and each chain preserves original order because nodes are appended only at the tail.

**Trace interleaved partition values**

For `[1,4,3,2,5,2]` with $x = 3$, the lower chain grows as `1,2,2`; the upper chain grows as `4,3,5`. Concatenating gives `[1,2,2,4,3,5]` without reordering either group.

**Two stable chains encode the partition directly**

Each node satisfies exactly one predicate—value below `x` or value at least `x`—and is appended once to that chain's tail. Tail insertion preserves the encounter order within both groups.

After the scan, joining `lower_tail` to `upper_head` places every lower node before every upper node without changing either internal order. Detaching each node before appending prevents stale original links from creating a cycle or leaking nodes past the partition.

## Complexity detail
Each node is visited and relinked once, giving $O(n)$ time. A constant number of node pointers use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Move lower nodes to the front as encountered:** reverses their relative order and violates stability.
- **Store nodes or values in arrays:** simplifies regrouping but uses $O(n)$ extra space.
- Empty input returns empty. If every node satisfies the same side of the predicate, its original order and chain are preserved.
- Values equal to `x` belong to the higher partition; using `<=` would implement a different split.
- **Repeatedly search and splice misplaced nodes:** can take $O(n^2)$ time.
