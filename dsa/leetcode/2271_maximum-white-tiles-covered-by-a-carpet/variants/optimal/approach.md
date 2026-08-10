## General

**Sort intervals so one carpet can be swept from left to right**

The white intervals do not overlap, but they are not guaranteed to arrive in coordinate order. `tiles.sort()` orders them by left endpoint and, if necessary, right endpoint. Under the non-overlap guarantee, their right endpoints then increase in the same order.

Sorting makes it possible to maintain one forward pointer `j`. As the carpet's left edge moves right from one interval start to the next, `j` never needs to move backward.

The sort is in place. That mutation is not needed for the mathematical result, but it is observable to a caller retaining the original `tiles` list.

**Why it is enough to start at a white interval's left endpoint**

Consider any carpet placement. If its left edge is in a gap, it can slide right until it reaches the next white interval without losing white tiles on its left, because there are none there. This movement may only gain coverage on the right.

If its left edge lies inside a white interval, slide it left to that interval's left endpoint. The shift gains exactly that many white positions from the same continuous interval on the left. At the carpet's right edge, it can lose at most the same number of positions, so total white coverage does not decrease.

Therefore, some optimal placement begins at `li` for one of the sorted intervals `[li, ri]`. The outer loop tests every such anchor.

**Use a half-open carpet endpoint to simplify counting**

For a carpet starting at `li` with integer length `carpetLen`, the covered integer positions are

$$
[\texttt{li},\ \texttt{li}+\texttt{carpetLen}-1].
$$

It is convenient to define the exclusive endpoint

`E = li + carpetLen`.

Then an interval ending at `r` is fully covered when `r < E`, which the code writes as `r - li + 1 <= carpetLen`. An interval beginning at `l` overlaps partially when `l < E`, written as `li + carpetLen > l`.

The half-open viewpoint explains why the partial length is `E - l` rather than `E - l + 1`: it counts integer positions `l` through `E - 1`.

**Accumulate intervals that fit completely**

For a fixed outer index `i`, the `while` loop advances `j` across every interval whose right endpoint lies inside the carpet anchored at `li`. Each full interval contributes

`tiles[j][1] - tiles[j][0] + 1`

white tiles to `s`. The plus one is required because interval endpoints are inclusive.

When the loop ends, either `j == n` or interval `j` is the first interval not fully covered. Because intervals are sorted and disjoint, no later interval can be fully covered if this first one is not.

**Add at most one partially covered interval**

If `j < n` and the next interval starts before `E`, the carpet covers its prefix from `tiles[j][0]` through `E - 1`. Its contribution is

`li + carpetLen - tiles[j][0]`.

Interval `j` is known not to be fully covered, so this value cannot exceed its length. Every interval after `j` begins even farther right and has no overlap with the carpet. Thus, candidate coverage is the sum `s` of fully covered intervals plus at most this one partial prefix.

If `j == n` or its left endpoint is at least `E`, there is no partial overlap and the candidate is simply `s`. `ans` retains the maximum across all anchors.

**Reuse the full-coverage sum between anchors**

After evaluating the carpet beginning at interval `i`, the next outer iteration begins at interval `i + 1`. The old interval `[li, ri]` should no longer contribute to the new full-interval sum, so the code subtracts its inclusive length from `s`.

In the usual case, `j > i` and interval `i` was previously added to `s`; subtraction removes exactly the departing leftmost interval. Since the new carpet starts farther right, previously full intervals after `i` remain candidates, and `j` can continue advancing rather than restart.

**Understand the temporary negative bookkeeping case**

If `carpetLen` is shorter than interval `i`, that interval is not added by the `while` loop because it is not fully covered. The partial formula still records `carpetLen` white tiles correctly. The unconditional final subtraction then makes `s` temporarily negative even though no negative coverage exists.

On the next outer iteration, `j` still points to the preceding interval `i`. Because that interval lies completely before the new left endpoint, the `while` condition is automatically true; its full length is added back, canceling the temporary debt, and `j` advances to the current interval. Before the next candidate is evaluated, `s` again equals the true sum of fully covered intervals.

This bookkeeping is unusual but correct. It lets the same unconditional subtraction serve both the normal and too-long-current-interval cases.

**Why the two pointers cover every optimal placement**

The anchor argument proves that an optimum exists among the outer loop's starts. For each such start, the monotone `j` loop includes every interval fully inside the carpet, and the separate formula includes exactly the covered prefix of the next interval when one exists. Non-overlap means these lengths can be added without double-counting.

Thus, the candidate computed at index `i` equals the exact number of white tiles for that anchor. Taking the maximum over all anchors returns the global optimum.

**Trace the shape of one candidate**

Suppose a carpet begins at a left endpoint ten and has length ten, so `E = 20` and it covers positions ten through nineteen. Any intervals ending at or before nineteen are added fully. If the next interval begins at, say, 18 but ends beyond 19, its partial contribution is `20 - 18 = 2`. An interval beginning at 20 contributes nothing because position 20 lies just outside the carpet.

These boundary calculations are why the code uses `<=` for full inclusive length and strict `>` for partial overlap.

## Complexity detail

Let `n` be the number of intervals. Sorting costs `O(n \log n)` time. During the sweep, the outer index visits each interval once and `j` increases at most `n` times in total, even though it appears inside a nested loop. The sweep is `O(n)`, so total time is `O(n \log n)`.

The two-pointer bookkeeping itself uses `O(1)` auxiliary variables. Python's in-place Timsort can use `O(n)` temporary memory in the worst case, so including sorting internals gives `O(n)` auxiliary space, consistent with the manifest. The list is reordered in place rather than copied.

Coordinates may be as large as one billion, but the algorithm depends on the number of intervals rather than the coordinate range. It never allocates one entry per tile position.

## Alternatives and edge cases

- **Prefix sums plus binary search:** Sort intervals, build cumulative lengths, and binary-search the last fully covered interval for each anchor. This is correct but makes the post-sort phase `O(n \log n)` instead of the linear two-pointer sweep.
- **Coordinate expansion:** Marking every integer tile is impossible when coordinates reach `10^9`.
- **Try every carpet coordinate:** The coordinate domain is too large; the anchor proof reduces candidates to interval starts.
- **Restart the right pointer for each anchor:** It can degrade the sweep to `O(n^2)`. Monotonicity lets `j` advance only once overall.
- **Single interval shorter than the carpet:** The full interval is added and its entire length is a candidate.
- **Single interval longer than the carpet:** It is handled as the one partial interval and contributes exactly `carpetLen`.
- **Carpet spans every interval:** The first suitable anchor accumulates all interval lengths, and `j` reaches `n`.
- **Large gaps:** Gaps add no value but consume carpet length naturally through coordinate comparisons.
- **Partial next interval:** Only its prefix before the exclusive endpoint contributes.
- **Interval begins at the exclusive endpoint:** The strict overlap test fails, correctly contributing zero.
- **Inclusive interval endpoints:** Every full interval length needs `right - left + 1`.
- **Non-overlap guarantee:** It permits lengths to be summed directly and ensures sorted endpoints progress consistently.
- **Temporary negative** `s`: It can occur after an interval longer than the carpet; the stale `j` entry cancels it at the start of the next iteration before coverage is evaluated.
- **Equal optimal placements:** `ans` stores only the maximum count, so which anchor achieves it is irrelevant.
- **Maximum possible coverage:** It can never exceed `carpetLen` because each covered coordinate contributes at most one white tile.
- **Input mutation:** `tiles.sort()` changes interval order in the caller's list; copy before sorting if preservation is required.
