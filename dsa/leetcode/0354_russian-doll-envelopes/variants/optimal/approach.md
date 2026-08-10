## General

An envelope `[w1, h1]` can go inside `[w2, h2]` only when both inequalities are strict: $w_1<w_2$ and $h_1<h_2$. The input order is irrelevant, so the challenge is to arrange two-dimensional objects into the longest chain without trying every permutation.

The exact solution reduces the problem to a one-dimensional longest increasing subsequence, abbreviated LIS. It first sorts envelopes by width ascending and, for equal widths, height descending. It then ignores widths and finds the length of a strictly increasing subsequence among the heights.

That tie-breaking rule is the crucial part. Sorting only by ascending width would allow the height subsequence to choose two envelopes with equal widths, even though they cannot nest. Descending heights within each equal-width group make that impossible.

**Why sorting removes one dimension.**

Every valid nesting chain has strictly increasing widths. Once all envelopes are ordered by ascending width, any valid chain must appear in that same left-to-right order; it can skip envelopes, but it never needs to move backward. The remaining requirement is to select heights that also increase strictly.

If all widths were distinct, sorting by width and taking a strict height LIS would be enough. Equal widths introduce a trap. For example, sorting `[1, 3]`, `[1, 4]`, and `[1, 5]` by both dimensions ascending produces heights `3, 4, 5`. A height LIS would incorrectly choose all three, although no envelope of width `1` can contain another width-`1` envelope.

The source sorts equal-width envelopes by negative height, which means descending actual height. That group becomes `5, 4, 3`. A strictly increasing height subsequence cannot take two values from this descending group in their left-to-right order. Therefore any height LIS selects at most one envelope of each width.

**Why the reduction works in both directions.**

Take any real nesting chain. Its widths and heights both increase strictly. Sorting the complete input by ascending width preserves the chain's width order, and its increasing heights form a valid subsequence of the sorted height sequence. Thus the height LIS is at least as long as the best envelope chain.

Now take any strictly increasing height subsequence after the special sort. It cannot contain two equal-width envelopes because equal-width heights appear in descending order. Its selected widths must therefore increase strictly. Its heights increase strictly by the subsequence definition. Every selected envelope fits into the next, so the subsequence corresponds to a valid nesting chain. Thus the height LIS is no longer than the best chain.

Since each optimal object maps to the other without changing length, the two maximum lengths are equal.

**What the `d` array represents.**

After sorting, the source initializes `d` with the first envelope's height. For every prefix processed so far, `d[t]` is the smallest possible ending height among all strictly increasing height subsequences of length `t + 1` found in that prefix.

The word “smallest” matters. A smaller ending height is easier to extend with future envelopes. If two subsequences have the same length and one ends at height `6` while another ends at height `10`, keeping `6` is never worse: any later height greater than `10` is also greater than `6`, and some heights between them can extend only the smaller tail.

`d` itself is strictly increasing. It is a compact summary of the best tail available for every achievable subsequence length. It is not necessarily the heights of one actual chain. Replacing an earlier tail can combine summaries derived from different historical subsequences, but every position still certifies that a subsequence of that length exists.

**Processing a new height.**

For each height `h` after the first envelope, there are two cases.

If `h > d[-1]`, it is greater than the smallest tail of the longest length found so far. Appending `h` creates a strictly increasing subsequence one element longer, so the solution calls `d.append(h)`.

Otherwise, the longest known subsequence cannot be extended. The source uses `bisect_left(d, h)` to find the first index whose value is greater than or equal to `h`, then replaces that value with `h`. Every earlier tail is strictly less than `h`, so `h` can end a subsequence of length `idx + 1`. Replacing the old tail preserves that achievable length while making its endpoint no larger and therefore at least as extendable.

Using `bisect_left` rather than `bisect_right` enforces strict growth. If `h` equals an existing tail, it replaces that tail instead of being appended after it. Equal heights cannot nest because the height inequality must be strict.

**A full trace of the first example.**

The input `[[5,4],[6,4],[6,7],[2,3]]` becomes `[[2,3],[5,4],[6,7],[6,4]]`. Width `6` appears twice, so height `7` comes before height `4`.

- Start with height `3`: `d = [3]`.
- Height `4` exceeds `3`, so `d = [3, 4]`.
- Height `7` exceeds `4`, so `d = [3, 4, 7]`.
- Height `4` does not exceed `7`. `bisect_left` finds index `1`, and replacing `d[1]` with `4` leaves the summary `[3, 4, 7]` unchanged.

The final length is three, represented by the valid chain `[2,3]`, `[5,4]`, `[6,7]`. The later `[6,4]` cannot be added after another width-`6` envelope, and the descending tie order prevents that mistake.

**Why the final length is the answer.**

Initially `d` correctly represents the one subsequence containing the first height. Each append records the discovery of a longer strict subsequence. Each replacement preserves all achievable lengths and improves or maintains one tail. Therefore, after all heights have been processed, `len(d)` is exactly the strict height LIS length. The sorting reduction proves that this is exactly the maximum number of nestable envelopes.

The implementation returns only the maximum count, so it does not keep predecessor links needed to reconstruct a particular chain. It also sorts `envelopes` in place, changing the caller's array order.

## Complexity detail

Let $n$ be the number of envelopes. Sorting by the tuple `(width, -height)` takes $O(n\log n)$ time. The loop processes $n-1$ heights, and each `bisect_left` search over `d` costs $O(\log n)$. Appending or replacing one list element is constant time. Total running time is therefore $O(n\log n)$.

The `d` list can grow to $n$ elements, so it uses $O(n)$ space. The expression `envelopes[1:]` creates a shallow slice containing $n-1$ references, which also uses $O(n)$ temporary space. Python's in-place Timsort may require $O(n)$ auxiliary storage in the worst case. Thus the manifest's $O(n)$ space bound accurately describes this exact source.

The sort mutates the input list but not the two-element envelope lists themselves. If mutation were disallowed, sorting a copy would still require $O(n)$ space and the same asymptotic time.

## Alternatives and edge cases

- **Quadratic dynamic programming:** After the same careful sort, let `dp[i]` be the longest valid chain ending at envelope `i` and compare every earlier envelope. This is easier to reconstruct and reason about directly but costs $O(n^2)$ time, which is too slow for $10^5$ envelopes.

- **Sort equal widths ascending:** This is incorrect with a one-dimensional height LIS because it can select multiple envelopes that share a width. Equal widths must appear with descending heights.

- **Use `bisect_right`:** That computes a non-decreasing height subsequence and can count equal heights. The nesting condition is strictly greater in both dimensions, so `bisect_left` is required.

- **Fenwick or segment tree over heights:** After coordinate compression and width-grouped updates, one can query the best chain below each height. This also reaches $O(n\log n)$ but has more machinery than the tails method.

- **All envelopes identical:** Descending tie order changes nothing because all heights are equal. Every new height replaces index zero, so the answer remains `1`.

- **Equal widths with different heights:** At most one can enter a valid chain. Descending height order ensures the LIS cannot take two from that group.

- **Different widths with equal heights:** `bisect_left` prevents both from appearing in a strict height subsequence, correctly enforcing the height condition.

- **A single envelope:** The constraints guarantee nonempty input. `d` starts with its height, the loop is empty, and the answer is `1`.

- **No rotation:** Width and height retain their supplied roles throughout sorting and comparison. Swapping dimensions to improve fit would solve a different problem.

- **Negative-height sort key:** `-x[1]` is only a sorting device that reverses height order among equal widths. Heights themselves stay positive and are inserted into `d` without negation.

- **The tails list is not a reconstructed solution:** Its length is exact, but its entries should not automatically be presented as one chosen envelope chain. Reconstruction requires tracking indices and predecessors separately.
