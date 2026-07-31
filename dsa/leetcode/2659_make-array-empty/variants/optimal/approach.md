## General

**Fix the removal order.** Since values are distinct, an element can be removed only when every smaller value is gone. Thus original indices are removed in ascending order of their values. Rotations change the logical front but never change the circular order of surviving original indices.

**Represent surviving positions.** Store `1` for every alive original index in a Fenwick tree. Its prefix sums count how many surviving elements lie in any index interval. Let `current` denote the original index just before the logical front: it is `0` initially for the first count formula, and after removing a target it becomes that now-dead target index, so the next alive index encountered circularly is the new front.

For a target at or after `current`, the number of rotations before its removal is the alive count strictly between those positions. For a target before `current`, split the circular path into the suffix after `current` and the prefix before the target. Add one operation for removing the target itself, delete its Fenwick-tree marker, and continue from that index.

Every counted alive position must be rotated past once before the target reaches the front, and no dead position corresponds to an array element anymore. Therefore each interval count exactly matches the real operations between consecutive removals. Processing all targets in forced value order yields the unique total operation count.

## Complexity detail

Sorting the $n$ original indices by value takes $O(n\log n)$ time. Initializing the Fenwick tree and processing $n$ targets each use $O(\log n)$ updates or prefix queries, so the total remains $O(n\log n)$. The sorted indices and tree use $O(n)$ space.

The benchmark scales `size` as $n$ and uses descending arrays. A literal deque simulation completes every tier but performs $n+(n-1)+\cdots+1=O(n^2)$ operations.

## Alternatives and edge cases

- **Literal deque simulation:** Rotate or remove exactly as stated. It is easy to verify but can execute $O(n^2)$ operations on descending input.
- **Segment tree:** Range sums and point deletion provide the same $O(n\log n)$ bound with a larger implementation.
- **Ordered set with rank queries:** A suitable order-statistics tree can count surviving circular intervals, but this structure is not built into many languages.
- An increasing array requires exactly $n$ removals and no rotations.
- A descending array forces a complete pass through the remaining elements before each removal.
- Negative values do not change the method; only their relative sorted order matters.
- After a wrap from the end to the beginning, dead indices must not contribute to the operation count.
