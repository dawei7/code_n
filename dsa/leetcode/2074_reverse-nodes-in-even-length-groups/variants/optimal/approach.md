## General
**Measure the actual group before deciding**

The first one-node group never changes, so keep a pointer to its tail and begin with target length two. From `group_tail.next`, advance a probe by at most the target length to count how many nodes the next group actually contains and to remember the first node after it. This count, not the target, determines parity for a truncated final group.

**Reverse and reconnect one even group**

For an even group, perform standard in-place pointer reversal for exactly its actual length, initializing the reversal's previous pointer to the node after the group. Connect the prior group's tail to the new group head. The old group head becomes its new tail and is the boundary pointer for the following iteration. For an odd group, simply advance the boundary pointer across its nodes.

The measurement step partitions the remaining list exactly according to the required natural-number lengths. Odd groups retain every link. Reversing exactly the measured nodes in an even group flips their internal order while the two reconnections preserve both neighboring groups. Repeating this argument across all groups yields precisely the required list.

## Complexity detail
Each node is visited at most once while measuring its group and at most once more while either reversing or advancing the boundary. The total time is $O(n)$. Only a fixed number of node pointers and counters are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Copy nodes into an array:** Group boundaries and slice reversals become simple, but the extra array requires $O(n)$ space.
- **Relocate from the head for every group:** The pointer changes can remain correct, but repeatedly traversing the processed prefix costs $O(n^{3/2})$ time across roughly $\sqrt n$ groups.
- The one-node first group is odd and never reverses.
- The last group's actual length, rather than its intended length, controls reversal.
- A truncated final group can be even even when its intended length is odd.
- Repeated values do not change the operation: node order, not value distinctness, is reversed.
- A single-node list is returned unchanged.
