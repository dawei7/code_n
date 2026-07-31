## General

**Valid starts form a suffix for each right endpoint**

Fix a right endpoint `right` and consider moving a candidate left endpoint to the right. Removing elements cannot increase the maximum-minus-minimum range, and it decreases the length. Consequently, the cost cannot increase. The valid starts for this endpoint therefore form a suffix: once `nums[left..right]` is valid, every subarray ending at `right` and starting after `left` is also valid.

Maintain `left` as the smallest valid start for the current `right`. After extending the window, move `left` forward while the cost exceeds `k`. When the window becomes valid, exactly `right - left + 1` subarrays ending at `right` qualify, so add that quantity to the answer.

**Maintain both extrema without rescanning**

Use an increasing deque of indices for the window minimum and a decreasing deque for the maximum. Before appending `right`, remove indices from the back whose values are no better extrema than `nums[right]`. The front of each deque then identifies the current minimum or maximum. When `left` advances past a deque front, remove that expired index.

Every invalid start is discarded because its full window cost exceeds `k`. The monotonicity argument shows that the first remaining start and all later starts are valid, so the per-endpoint addition counts exactly the qualifying subarrays ending there. Summing these disjoint groups over all right endpoints counts every valid subarray once.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Each index enters and leaves each monotonic deque at most once, and both window boundaries move only forward. The total time is $O(N)$. In the worst case the two deques store $O(N)$ indices, so auxiliary space is $O(N)$.

The benchmark defines size as $N$ and uses `nums = [1, 2, ..., N]`. With $t=N/4$ and `k = t * (t - 1)`, exactly the subarrays of lengths at most $t$ qualify, giving $tN-t(t-1)/2$ results. The accepted window and an independent pair-deque implementation scale linearly, while direct endpoint expansion maintains extrema but examines $O(N^2)$ subarrays.

## Alternatives and edge cases

- **Direct endpoint expansion:** Extend every start through every possible end while maintaining its extrema. This is a clear oracle, but it still visits $\Theta(N^2)$ subarrays.
- **Balanced multiset window:** A sorted multiset can expose both extrema while the window moves, but insertions and removals raise the running time to $O(N\log N)$.
- **Range queries plus binary search:** A sparse table can answer min/max queries quickly and binary-search the first valid start for each endpoint, but preprocessing and searches also cost $O(N\log N)$ overall.
- **Single-element subarrays:** Their maximum equals their minimum, so their cost is always zero and they always qualify.
- **`k = 0`:** Only subarrays whose values are all equal have zero cost; duplicate runs can contribute more than their singletons.
- **Duplicate extrema:** Monotonic deques must retain a valid representative until every equal occurrence that could serve as the extremum has expired.
- **Inclusive threshold:** A cost exactly equal to `k` qualifies; shrink only while the cost is strictly greater.
- **Large arithmetic:** The cost can reach nearly $10^{14}$ and the answer can reach $N(N+1)/2$, so fixed-width implementations need 64-bit arithmetic.

