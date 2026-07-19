## General
**Convert every length-k choice into a window sum**

Use a rolling sum to build `window[i]`, the sum of the subarray starting at `i`. The original problem then becomes choosing three start indices at least `k` apart.

**Precompute the best window on each side**

Scan left to right so `left[i]` stores the earliest maximum-sum window among starts `0..i`. Update only for a strictly greater sum, preserving the earlier index on ties. Scan right to left so `right[i]` stores the earliest maximum-sum start among `i..end`. Update on greater or equal sums because the newly visited index is smaller and therefore lexicographically preferable.

**Enumerate the middle window**

For every legal middle start `m`, the best compatible left start is `left[m-k]` and the best compatible right start is `right[m+k]`. Add their three window sums. Process middle starts in increasing order and replace the answer only for a strictly larger total; all tie rules already favor the smallest left, then middle, then right indices.

**Why independently best sides are sufficient**

Once the middle start is fixed, every left window ending before it and every right window beginning after it are independent choices. Replacing either side with its maximum compatible window cannot reduce feasibility and can only improve the total. Thus the best triple for each middle uses the precomputed sides, and checking all middle starts covers the global optimum. The directional tie rules produce the lexicographically smallest optimum.

## Complexity detail
Rolling window sums and both best-index arrays take $O(N)$ time. The middle scan is another $O(N)$ pass, so total time is $O(N)$. The window, left, and right arrays use $O(N)$ auxiliary space.

## Alternatives and edge cases
- **Three-stage dynamic programming:** for one, two, and three selected windows, compare skipping the current start with taking it after the best compatible prior state; it also runs in $O(N)$ time and space.
- **Rescan both sides for every middle:** is conceptually direct but repeats maximum searches and takes $O(N^2)$ time.
- **Enumerate all triples:** checks the definition literally but takes $O(N^3)$ time.
- Windows may touch at their boundaries; starts differing by exactly `k` do not overlap.
- Equal totals require lexicographic tie-breaking, not whichever triple was evaluated last.
- When $N = 3k$, the only legal answer is `[0, k, 2k]`.
