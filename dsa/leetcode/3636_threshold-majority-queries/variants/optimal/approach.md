## General

**Compress values while preserving tie order.** Map the distinct array values to ranks in ascending numeric order. A smaller rank is therefore the correct choice when frequencies tie. Store the sorted occurrence positions of every rank so any candidate's exact frequency in `[l, r]` is available through two binary searches.

**Precompute modes of full block ranges.** Split the array into blocks of about $\sqrt n$ positions. For every starting block, scan to the right while maintaining frequencies and record the mode after each complete ending block. This table supplies the maximum-frequency, smallest-value rank for any range consisting solely of consecutive full blocks.

**Reduce each query to a middle mode and boundary values.** If a query has no full block strictly between its endpoint blocks, scan its at most two partial blocks directly. Otherwise, begin with the precomputed mode of the full middle blocks. The only other values that need consideration are those appearing in the left or right partial boundary.

To see why, suppose a possible winner $x$ does not occur in either boundary. Its full-query frequency equals its middle frequency. The precomputed middle mode $y$ has at least that middle frequency and is smaller if the frequencies tie. Boundary occurrences can only increase $y$ further, so $x$ cannot outrank $y$. Therefore, any value that beats the middle mode must occur on a boundary.

Deduplicate boundary ranks, count each candidate exactly with its occurrence-position list, and apply the same frequency-then-smallest comparison. Finally compare the winning frequency with the query threshold.

## Complexity detail

Let $n$ be the array length, $q$ the query count, and choose block size $B=\Theta(\sqrt n)$. Mode-table construction costs $O(n^2/B)=O(n\sqrt n)$ time. A query examines $O(B)$ boundary positions and performs binary searches for distinct candidates, costing $O(\sqrt n\log n)$. Total time is $O(n\sqrt n+q\sqrt n\log n)$.

Occurrence lists, compressed values, temporary frequency storage, and the $O((n/B)^2)$ mode table use $O(n)$ auxiliary space for $B=\Theta(\sqrt n)$.

The benchmark sets $n=q=S$. The accepted method grows as $O(S\sqrt S\log S)$, whereas recounting each long query from scratch takes $O(S^2)$ time.

## Alternatives and edge cases

- **Count every query directly:** A frequency map gives simple correct answers but repeats work proportional to the total queried length.
- **Boyer-Moore majority vote:** It finds a candidate only when a strict majority is promised; arbitrary thresholds and mode tie-breaking invalidate that shortcut.
- **Random sampling:** It can be fast probabilistically but cannot guarantee the required deterministic answer for low thresholds.
- **Mo's algorithm:** Reordering queries and maintaining frequencies is another deterministic square-root approach, but selecting the smallest value at the maximum frequency needs an additional ordered structure.
- **Frequency tie:** Compare original values, represented here by ascending compressed ranks.
- **Threshold check:** Select the true mode first, then return `-1` if even its frequency is too small.
- **Short range:** Direct scanning avoids consulting a nonexistent full middle block.
- **Repeated boundary values:** Deduplicate them before binary-search counting.
