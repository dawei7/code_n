## General
**A dummy-headed chain owns all processed nodes in sorted order**

Use a dummy node before the sorted output so insertion before the current minimum needs no head special case. Take nodes one at a time from the original traversal. Starting at the dummy, advance while the next sorted value is less than or equal to the current value; the stopping link is its insertion position.

**Save the unprocessed suffix before changing the node's links**

Save `next_unsorted = current.next` first. Then assign `current.next = position.next` and `position.next = current`. Resume from the saved original successor. This order keeps the unprocessed list reachable while moving the existing node into the sorted chain.

**Every iteration transfers exactly one node between disjoint regions**

Before each iteration, the list after `dummy` contains exactly the processed nodes in nondecreasing order. The `current` pointer begins the unprocessed original suffix. Inserting at the first greater value preserves sorted order and membership.

**Trace repeated insertion before earlier nodes**

For `[4,2,1,3]`, the sorted prefix evolves as `[4]`, `[2,4]`, `[1,2,4]`, then `[1,2,3,4]`. Each step moves one existing node into place.

**The insertion boundary preserves the sorted prefix**

The scan through the sorted prefix stops after all values no greater than the current node and before the first larger value. Splicing at that boundary keeps every predecessor value at most current and every successor value greater, so the enlarged prefix remains sorted.

Each iteration removes one node from the untouched suffix and inserts that same node once. When the suffix is empty, the sorted prefix contains every original node exactly once.

## Complexity detail
The `i`th insertion may scan $O(i)$ sorted nodes, totaling $O(n^2)$ in the worst case. Only a dummy node and a constant number of pointers are used.

## Alternatives and edge cases
- **Merge sort:** sorts a linked list in $O(n \log n)$ time, but this problem specifically asks for insertion-sort behavior.
- **Copy into an array:** enables library sorting but uses $O(n)$ extra space and does not demonstrate node insertion.
- **Swap node values:** can sort values but violates the stronger node-relinking interpretation.
- Empty and one-node lists are already sorted. Equal values remain adjacent; using `<=` while scanning preserves their relative order.
- Already sorted input still performs scans and exhibits the quadratic worst case for this straightforward implementation; reverse-sorted input inserts repeatedly near the front.
