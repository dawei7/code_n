## General

A breadth-first traversal naturally exposes one whole tree level at a time. Keep the current frontier in a queue. Its length at the start of an iteration is exactly the number of nodes on that level, so removing that many nodes and adding their values produces one level sum while their children form the next frontier.

**Retain only relevant sums:** A min-heap of at most `k` values stores the largest level sums seen so far. Push every sum until the heap reaches size `k`. Afterward, its root is the smallest retained candidate. A new sum can affect the answer only when it is larger than that root, in which case replacing the root restores the best `k` sums.

After each processed level, the heap therefore contains exactly the `k` largest sums among the processed levels, or all sums if fewer than `k` levels have been processed. Once traversal ends, a full heap has the requested value at its root. A smaller heap proves that the tree has fewer than `k` levels, so the required result is `-1`. Equal sums remain separate heap entries and consequently retain their separate ranks.

## Complexity detail

Let $n$ be the number of nodes and $w$ the maximum number of nodes on one level. Breadth-first traversal visits each node once. Each level causes at most one $O(\log k)$ heap update, and the number of levels is at most $n$, giving $O(n \log k)$ time. The queue and heap use $O(w+k)$ auxiliary space, which is $O(n+k)$ in the manifest bound.

## Alternatives and edge cases

- **Sort every level sum:** Collecting all $h$ level sums and sorting them takes $O(n+h\log h)$ time and $O(w+h)$ space; it is simpler but retains every sum even when `k` is small.
- **Depth-first accumulation:** A depth-first traversal can add values into an array indexed by depth, but a legal skewed tree makes recursive implementations vulnerable to call-stack limits.
- **Quickselect:** Selection can find the requested rank in expected linear time after collecting every level sum, trading simpler worst-case guarantees for extra retained storage.
- **Too few levels:** The input permits `k` to exceed the tree height even though `k \leq n`; the heap then contains fewer than `k` entries and the answer is `-1`.
- **Duplicate sums:** Equal level sums are not deduplicated, so each equal value occupies its own rank.
- **Large totals:** A level may sum many values up to $10^6$, so fixed-width implementations must use 64-bit integers for level sums.
