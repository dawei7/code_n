## General

**Represent the changing minimums with a heap.** Copy all values into a min-heap. Its root is always the smallest current value, and removing the root twice yields the two values mandated by the operation. Because the first removal is no larger than the second, the replacement is `first * 2 + second`; push that value back into the same heap.

**Stop from the root condition.** Repeat while the heap root is below `k`. When the root reaches `k`, every other heap value is at least as large, so the entire collection satisfies the goal. Count one operation for each pop-pop-push cycle.

The heap contains exactly the current multiset after every iteration: it starts with all original values, and each cycle removes precisely the required two smallest occurrences before inserting precisely their specified combination. Thus the simulation follows the only value transition allowed by the problem. Before the stopping point, the smallest value violates the threshold, so another operation is necessary. At the stopping point all values qualify, making the accumulated count both sufficient and minimal.

## Complexity detail

Let $n$ be the original array length. Heap construction takes $O(n)$ time. Each operation reduces the heap size by one and uses two removals plus one insertion, each costing $O(\log n)$. At most $n-1$ operations occur, so total time is $O(n \log n)$. The copied heap stores at most $n$ values, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Repeatedly sort the array:** Sorting exposes the two smallest values but repeating it after every insertion can cost $O(n^2 \log n)$ time.
- **Two linear minimum scans:** Avoiding a heap still finds the mandated values, but repeated scans lead to quadratic time.
- **Balanced ordered multiset:** It supports minimum removal and insertion in $O(\log n)$ time, matching the asymptotic bound with a more complex structure.
- **Already qualified:** If the initial minimum is at least `k`, no operation is necessary.
- **New value below `k`:** A combination may remain below the threshold and must participate in a later operation.
- **Duplicate minimums:** Both occurrences are removed independently, including when their values are equal.
- **Two remaining values:** The guaranteed-existence condition ensures that if the smaller one is below `k`, combining the final pair eventually produces a valid result.
