## General

When `k = 0`, the answer is immediately $n$ because every element has at least zero greater values.

For positive `k`, let $t$ be the $k^{\text{th}}$ largest array value when occurrences, including duplicates, occupy separate sorted positions. A value `x` is qualified exactly when `x < t`. If `x < t`, the first `k` descending positions are all strictly greater than `x`. If `x >= t`, fewer than `k` positions can be strictly greater; values equal to the threshold do not count because the comparison is strict.

The same threshold is at zero-based index `n - k` in ascending order. Use three-way Quickselect to partition a copied array into values below, equal to, and above a chosen pivot. Continue only in the partition containing index `n - k`; when that index lies inside the equal block, the pivot is the threshold. A final pass counts original values strictly below it. Three-way partitioning is essential for duplicate-heavy arrays because the entire equal block can be resolved at once.

## Complexity detail

Let $n$ be the array length. Randomized Quickselect takes expected $O(n)$ time, and the final counting pass is $O(n)$, so the expected total is $O(n)$; adversarial pivot choices can produce $O(n^2)$ in the worst case. Copying the input for in-place partitioning uses $O(n)$ auxiliary space. The manifest's bound records the expected Quickselect behavior.

## Alternatives and edge cases

- **Sort the array:** Sorting reveals the threshold directly and is simple, but costs $O(n\log n)$ time.
- **Heap of the largest values:** Maintaining `k` candidates costs $O(n\log k)$ time and $O(k)$ space.
- **Compare every pair:** Counting greater elements separately for every occurrence is correct but takes $O(n^2)$ time.
- **Zero threshold count:** If `k = 0`, return $n$ without selecting an order statistic.
- **Duplicate threshold:** Values equal to the $k^{\text{th}}$ largest value are not qualified because only strictly greater values count.
- **Largest possible `k`:** With `k = n - 1`, only a unique strict minimum can qualify; repeated minima yield no qualified occurrence.
- **Input preservation:** Partition a copy so the caller's array order and contents remain unchanged.
