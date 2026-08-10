## General

The task asks for exactly three length-`k` subarrays. They must not overlap, their total sum must be as large as possible, and ties must be resolved by the lexicographically smallest triple of starting indices.

Because the number of subarrays is fixed at three, the solution does not need a general multi-dimensional dynamic-programming table. It slides three length-`k` windows together and progressively remembers:

- the best first window seen so far;
- the best compatible pair of first and second windows seen so far; and
- the best compatible triple seen so far.

This turns an apparently combinatorial search into one left-to-right scan.

**How the three current windows are positioned**

The loop variable `i` is the ending index of the current third window. Once `i >= 3 * k - 1`, all three maintained window sums have reached length `k`:

- `s1` covers indices `i - 3k + 1` through `i - 2k`;
- `s2` covers indices `i - 2k + 1` through `i - k`;
- `s3` covers indices `i - k + 1` through `i`.

These windows are adjacent. The first ends immediately before the second starts, and the second ends immediately before the third starts. Adjacency is not a restriction on the final answer, because `mx1` and `mx12` remember earlier best windows rather than forcing the selected first and second windows to remain the current adjacent ones.

At the top of every iteration, the code adds:

- `nums[i - 2 * k]` to `s1`;
- `nums[i - k]` to `s2`;
- `nums[i]` to `s3`.

The loop begins at `i = 2k`. During the first `k` iterations, each sum grows from one element to a complete window. Updates to the best answers begin only when `i >= 3k - 1`, exactly when all three sums contain `k` elements.

After processing a complete triple position, the code subtracts the leftmost element of each current window. On the next iteration, adding the new rightmost elements slides all three windows one position to the right while preserving their length.

**Best one-window state**

The variable `mx1` is the greatest sum of any first-window candidate encountered up to the current position. `idx1` is the starting index of that best window.

At the current triple position, `s1` starts at

`i - 3 * k + 1`.

If `s1 > mx1`, the code replaces both `mx1` and `idx1`. Otherwise, it keeps the earlier best first window.

This state means that when the current second window is considered, `mx1` is the best length-`k` window that ends before that second window begins. Compatibility is automatic: every candidate summarized in `mx1` appeared no later than the current `s1` position.

**Best two-window state**

The current `s2` begins at

`i - 2 * k + 1`.

Combining it with `mx1` gives the best compatible pair whose second window is the current `s2`. The code compares `mx1 + s2` with the best pair sum `mx12`.

If the new pair is strictly better, it records:

`idx12 = (idx1, i - 2 * k + 1)`.

Thus `idx12` always identifies two non-overlapping windows, and `mx12` is their total. Because `mx1` was updated immediately before this comparison, a newly superior first window can participate in the current pair.

The order of these updates is essential. Updating the one-window state first, then the two-window state, and finally the triple state allows information to flow from earlier regions to later regions without ever allowing overlap.

**Best three-window state**

The current third window starts at

`i - k + 1`.

The best triple ending with this window has total

`mx12 + s3`.

If that value is strictly greater than `s`, the stored best total, the code updates `s` and creates

`ans = [*idx12, i - k + 1]`.

The starred expansion places the first two indices from `idx12` before the current third start. The resulting list is already in increasing order because each summarized state was constructed from non-overlapping windows to the left.

**Why gaps are still possible**

The three live sums are adjacent at every scan position, but the remembered choices need not be. Suppose an early window is best for `mx1`. As `s2` continues sliding right, that same early first window remains available until a strictly better first window appears. A gap can therefore form between `idx1` and the current second window.

Likewise, `idx12` can remain unchanged while `s3` slides farther right, creating a gap between the selected second and third windows. The current adjacent windows are only a mechanism for exposing candidates in a valid chronological order.

**How strict comparisons enforce lexicographic tie-breaking**

Candidate starting positions appear from left to right. When two first windows have equal sums, the code does not update `mx1` because it uses `>` rather than `>=`. The earlier start is kept, which is lexicographically preferable.

The same rule applies to pairs. If a later pair has the same total as `mx12`, the previously stored pair is kept. Since candidates are generated in increasing second-start order and each first choice is already the earliest optimal one, the existing pair is lexicographically no larger.

Finally, equal triple totals do not replace `ans`. The previously recorded triple has an earlier third position, or an already lexicographically smaller prefix. Therefore, strict improvement at all three levels yields the lexicographically smallest triple among maximum-sum answers.

This works especially cleanly because all `nums[i]` values are positive. The initial best sums of zero are below every valid one-window, pair, and triple total, so the first legal candidates are always recorded.

**A trace of the main example**

For `nums = [1, 2, 1, 2, 6, 7, 5, 1]` and `k = 2`, the first complete three-window position has:

- `s1 = 1 + 2 = 3` at start `0`;
- `s2 = 1 + 2 = 3` at start `2`;
- `s3 = 6 + 7 = 13` at start `4`.

The initial triple `[0, 2, 4]` has total `19`.

After sliding once, the current window sums are `3`, `8`, and `12`. The tied first sum keeps start `0`. The best pair becomes starts `[0, 3]` with sum `11`, and combining it with the third window at start `5` produces total `23`. The answer becomes `[0, 3, 5]`.

The final position may improve intermediate states, but it does not produce a triple above `23`, so the stored answer is returned.

**Why the progressive maxima are sufficient**

Consider any optimal triple with starts `a < b < c`. When the live third window reaches start `c`, every legal first window before `b` has already been considered by `mx1`. Thus `mx1` is at least as good as the triple's first window, with an earlier start on a tie.

By the time the live second window reached `b`, `mx12` considered the best compatible first window together with that second window. As scanning continued toward `c`, `mx12` retained or improved that pair. Therefore, when `s3` reaches the optimal third window, `mx12 + s3` is at least the optimal triple's total.

The algorithm cannot exceed the true optimum with an invalid combination because every state transition preserves window order and non-overlap. Hence the best stored total equals the optimum, and the strict tie rules select its lexicographically smallest indices.

## Complexity detail

Let `N = len(nums)`.

The loop advances `i` once from `2k` through `N-1`. Each iteration performs a constant number of additions, subtractions, comparisons, and small tuple or list assignments. Sliding-window sums prevent any length-`k` range from being recomputed element by element. The running time is

$$
O(N).
$$

The exact solution stores three current sums, three best sums, a few indices, one two-index tuple, and a three-index result. Their sizes do not grow with `N`. Its auxiliary space usage is therefore

$$
O(1).
$$

The returned list itself always contains exactly three integers and is also constant-sized. No prefix-sum array or DP table is allocated.

## Alternatives and edge cases

- **Prefix sums with best-left and best-right arrays:** Fix every possible middle window and look up the best non-overlapping window on each side. This is also `O(N)` time but uses `O(N)` auxiliary space.

- **General dynamic programming:** A table for the best total using a certain number of windows up to each position handles a variable number of subarrays. With the count fixed at three, the rolling maxima in this solution are simpler and use constant space.

- **Enumerating triples:** Trying all three starting positions takes cubic time, and even precomputed window sums do not remove the combinatorial number of choices.

- **Exactly `N = 3k`:** There is only one possible triple of non-overlapping length-`k` windows. The first complete iteration records and returns starts `[0, k, 2k]`.

- **Equal window sums:** Strict `>` comparisons retain earlier indices and are required for lexicographic minimality.

- **Gaps between chosen windows:** Remembered best states allow gaps even though the three live windows are adjacent.

- **Positive input values:** Positivity makes zero a safe initial value for `mx1`, `mx12`, and `s`. If negative values were allowed, these should start at negative infinity or be initialized from the first legal windows.

- **Order of updates:** `mx1` must be updated before `mx12`, and `mx12` before the triple. Reversing this order would delay useful candidates or combine states from the wrong scan position.

- **Subtracting after evaluation:** The leftmost values are removed only after all states use the full current windows. Subtracting earlier would make the sums represent only `k-1` elements.

- **Index formulas:** The starts `i - 3k + 1`, `i - 2k + 1`, and `i - k + 1` correspond to windows ending at `i - 2k`, `i-k`, and `i`. An off-by-one error would either overlap windows or shift their recorded starts.
