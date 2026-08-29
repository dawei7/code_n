## General

**Treat each interval as a constant-density block.** An interval `[left, right, value]` contributes `value` coins at every integer coordinate from `left` through `right`. The intervals do not overlap, and gaps contribute zero. A chosen window is an inclusive coordinate range of length $k$, so if it starts at $a$, it ends at $a+k-1$.

The protected source solves a restricted version first: among windows whose left edge equals the left edge of some coin interval, find the maximum. It then reflects the number line to turn right-edge-aligned windows into left-edge-aligned windows and takes the better result.

**Precompute complete interval sums.** Inside `best_starting_at_left`, the interval list is sorted by left endpoint. The array `starts` contains those left endpoints for binary search. The prefix array stores the total coins in complete intervals:

$$
\texttt{prefix}[i+1]
=
\texttt{prefix}[i]
+(r_i-l_i+1)c_i.
$$

Thus, `prefix[b] - prefix[a]` gives the coins in all complete intervals with sorted indices from $a$ through $b-1$. Gaps need no special entries because they add zero.

For every interval index `index`, the helper anchors the window at that interval's left endpoint. Its inclusive right edge is

`window_right = intervals[index][0] + k - 1`.

The binary search

`bisect_right(starts, window_right) - 1`

finds `last`, the final interval whose start lies inside the window. Every interval from `index` through `last - 1` is fully covered. The prefix difference `prefix[last] - prefix[index]` adds them in constant time.

The final interval `last` may extend past `window_right`, so it is handled separately. Its covered length is

`min(right, window_right) - left + 1`.

When positive, multiplying by `value` adds the covered coins. If the final interval ends within the window, this formula simply adds its full amount. This also handles `last == index`: the prefix difference is empty, and the separate overlap adds the only interval.

For the first example, anchoring at coordinate $3$ is not a left edge of an original interval, so the forward helper alone need not inspect the optimal window `[3,6]`. This is exactly why a second orientation is required.

**Why an optimum aligns with at least one coin boundary.** Imagine sliding a fixed-length window one coordinate at a time. Between points at which one edge crosses an interval boundary, the amount leaving on the left and entering on the right has constant per-coordinate density. The window sum therefore changes at a constant rate over that region. A linear change reaches its maximum at one end of the region, unless it is flat, in which case either end is equally good. Repeating this movement shows that some optimal window has either:

- its left edge equal to an interval's left edge; or
- its right edge equal to an interval's right edge.

The first family is exactly what `best_starting_at_left(coins)` checks.

**Reflection handles the second family without new logic.** Map every coordinate $x$ to $-x$. Original interval $[l,r]$ becomes $[-r,-l]$ with the same coin density, which the source constructs as `[-right, -left, value]`. An original window ending at $r$ becomes a reflected window beginning at $-r$. Therefore, calling the same helper on reflected intervals checks every original window aligned to an interval's right edge.

The method returns the maximum of the forward and reflected answers, covering an optimal boundary alignment in either direction. In the example, original window `[3,6]` ends at interval endpoint $6$; reflection converts it into a left-anchored window and recovers its value $10$.

**Why every computed sum is correct.** For a left-anchored window, non-overlap and sorted starts mean all intervals before `last` that begin at or after the anchor are fully covered. Only `last` can be partially covered on the right. The prefix sum plus its overlap therefore counts every bag in the window exactly once and counts no bag outside it. The boundary-alignment argument proves at least one globally optimal window is evaluated across the two calls.

The helper sorts its argument in place, but the first call receives `[interval[:] for interval in coins]`, a copied list of copied rows. The reflected call uses newly created rows. Thus the caller's original `coins` order and rows are not changed.

## Complexity detail

Let $n=\lvert\texttt{coins}\rvert$. Each helper sorts $n$ intervals in $O(n\log n)$ time, builds starts and prefix arrays in $O(n)$ time, and performs $n$ binary searches of $O(\log n)$ each. It therefore costs $O(n\log n)$ time. Calling it twice changes only the constant factor, so total time remains $O(n\log n)$.

Each call stores sorted intervals, starts, and prefix sums using $O(n)$ space. The reflected list and copied original list also contain $O(n)$ rows; although their lifetimes overlap at the outer call, total auxiliary space remains $O(n)$. Arithmetic uses Python integers, which safely hold coordinate-length times coin-value sums.

## Alternatives and edge cases

- **Two-pointer sweep:** After sorting, a carefully maintained sliding window can avoid binary search and achieve $O(n)$ after sorting. Prefix sums plus binary search are simpler to verify and preserve the same $O(n\log n)$ total bound.
- **Expand every bag:** Coordinates reach $10^9$, so materializing a value for each coordinate is impossible. Interval length must be handled arithmetically.
- **Check only left boundaries:** This misses optima such as a window whose right edge aligns with an interval while its left edge cuts another interval. Reflection is necessary.
- **Check only right boundaries:** Symmetrically, some optimum begins at an interval left edge. Both orientations cover all cases.
- **Window inside one interval:** The separate overlap calculation returns $k\cdot c$ when the interval is at least $k$ long, without needing another interval.
- **Large gaps:** Prefix sums omit gaps because they contain zero coins. Binary search may jump over any gap length without affecting the total.
- **Window longer than all occupied coordinates:** Every interval is fully included when reachable; empty coordinates contribute nothing, and the method returns the total coin count.
- **Adjacent intervals:** Non-overlap still permits one ending immediately before another starts. Sorting and prefix sums count both correctly with inclusive lengths `right - left + 1`.
- **Input preservation:** The helper mutates lists by sorting, so copied rows protect the supplied `coins` object from reordering.
- **Inclusive endpoints:** The `+ 1` in both window end and overlap length is essential. Omitting it would treat integer-coordinate bags as half-open intervals and undercount.
