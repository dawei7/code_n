## General

**Order subarrays by a fixed left endpoint.** Fix a left endpoint $l$ and consider subarrays `[l, r]` while $r$ moves from $l$ toward the end. Extending an interval can only keep or increase its maximum and can only keep or decrease its minimum, so the range value never decreases. Therefore, reading right endpoints from $n-1$ down to $l$ produces one non-increasing sequence of values for each $l$.

**Merge the monotone sequences with a max-heap.** The problem becomes merging $n$ sorted sequences and taking their first `k` values. Seed a max-heap with `[l, n - 1]` for every left endpoint. Repeatedly remove the greatest available range, add it to the answer, and advance only that sequence by inserting `[l, r - 1]` when it exists. Every interval belongs to exactly one sequence, so heap entries always represent distinct endpoint pairs.

**Evaluate exposed ranges with a segment tree.** A segment tree stores the minimum and maximum of every range, allowing the newly exposed predecessor interval to be valued in $O(\log n)$ time. The initial full-suffix values are computed in one reverse scan. At any moment, the heap contains the largest not-yet-selected value from every nonempty sequence. Its maximum is therefore the largest unselected subarray value globally. Repeating this argument proves that the first `k` removals are exactly the `k` values whose sum is optimal.

## Complexity detail

Building the min/max segment tree, suffix extrema, and initial heap takes $O(n)$ time. Each of the `k` selections performs one heap removal, at most one segment-tree query, and at most one heap insertion, each bounded by $O(\log n)$. The total time is $O(n+k\log n)$, and the trees, suffix arrays, and heap use $O(n)$ space.

## Alternatives and edge cases

- **Enumerate and sort every subarray:** This directly obtains the largest values but materializes $\Theta(n^2)$ intervals and cannot meet the input bound.
- **Sparse-table range queries:** They reduce each range query to $O(1)$ after $O(n\log n)$ preprocessing and space; the segment tree retains linear storage and already matches the heap cost.
- **Singleton intervals:** Their range is zero and they naturally appear at the end of each fixed-left sequence.
- **All values equal:** Every heap key is zero, so the required total is zero for any legal `k`.
- **Maximum `k`:** The process continues until exactly `k` distinct endpoint pairs have been removed, including zero-valued intervals when necessary.
- **Large total:** Up to $10^5$ values of size $10^9$ may be added, requiring a wide integer type outside Python.
