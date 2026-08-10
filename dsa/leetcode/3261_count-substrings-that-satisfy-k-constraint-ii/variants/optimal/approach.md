## General

A substring is invalid only when it contains more than $k$ zeros and more than $k$ ones. For a fixed ending index, valid starts form one contiguous suffix of start positions. The solution performs one global sliding-window pass, then combines a first-invalid-ending array with prefix sums so each range query is answered in constant time.

During preprocessing, `i` is the earliest valid start for the current ending `j`, and `cnt` stores character counts in `s[i:j+1]`. After adding `s[j]`, the while loop runs while both counts exceed $k$.

Before advancing one invalid start `i`, the code sets `d[i] = j`. This records that `j` is the first ending for which a substring beginning at that `i` becomes invalid. Earlier endings were processed while that start remained valid. Future endings cannot restore validity because counts only grow when the right boundary advances. Starts that never become invalid retain sentinel `n`.

After shrinking, all starts from `i` through `j` produce valid substrings ending at `j`, and every earlier start is invalid. Their number is `j - i + 1`. The prefix array stores cumulative counts:

`pre[j + 1] = pre[j] + j - i + 1`.

Thus `pre[b] - pre[a]` counts globally valid substrings whose ending indices lie from `a` through `b - 1`.

Now consider query `[l,r]`. Set

`p = min(r + 1, d[l])`.

For every ending `e` from `l` through `p - 1`, substring `s[l:e+1]` is valid because `e < d[l]`. If the longest one from `l` is valid, every later start through `e` is also valid. Therefore all substrings entirely inside the triangular region with starts at least `l` and endings below `p` are valid.

There are one valid substring ending at `l`, two ending at `l + 1`, and so on through `p - l` ending at `p - 1`. Their count is

$$
1+2+\cdots+(p-l)=\frac{(p-l)(p-l+1)}2,
$$

implemented as `a = (1 + p - l) * (p - l) // 2`.

For endings from `p` through `r`, start `l` is no longer guaranteed valid. But the global sliding-window earliest valid start for each such ending is strictly after `l` once `p = d[l]`. Therefore every globally valid substring counted in the prefix contribution already lies inside the query. The count is

`b = pre[r + 1] - pre[p]`.

The two ending ranges are disjoint and cover the entire query, so `a + b` is exact.

If `d[l] > r`, then `p = r + 1`. Every substring inside the query is valid, the prefix difference `b` is zero, and `a` becomes the total number of substrings of a length `r-l+1` interval.

For `s = "0001111"` and `k=2`, start zero first becomes invalid when the third one arrives at ending five, so `d[0]=5`. Query `[0,6]` counts the full triangle through ending four, then uses prefix data for endings five and six. The two invalid substrings beginning at zero are excluded, leaving twenty-six.

**Why using only `d[l]` is enough.** The split is based on endings, not on every query start separately. Before `d[l]`, all query-contained starts are valid. At and after it, the global earliest-valid-start prefix counts are safe because that earliest start has moved beyond `l`. Monotonicity bridges the two regions.

The preprocessing loop is the same sliding-window invariant as version I, but `d` and `pre` preserve enough information to reuse it for up to $10^5$ queries.

## Complexity detail

Let $n$ be the string length and $q$ the number of queries. Right boundary `j` advances $n$ times, and left boundary `i` advances at most $n$ times total, so preprocessing is $O(n)$. Each query performs constant arithmetic and array accesses, taking $O(1)$. Total time is $O(n+q)$.

Arrays `d` and `pre` use $O(n)$ auxiliary space. The two counters and pointers are constant. The returned answer uses $O(q)$ required output space; excluding output, auxiliary space is $O(n)$.

Counts of substrings can be quadratic in $n$, and Python integers safely store them.

## Alternatives and edge cases

- **Run a sliding window for every query:** This repeats character scans and can cost $O(nq)$.
- **Enumerate query substrings with prefix character counts:** Constant-time validity checks still leave a quadratic number of substrings per query.
- **Binary search with per-start valid ends:** One can store maximum valid ends and prefix sums, then binary-search a split for each query in $O(\log n)$. The exact source's `d[l]` gives the needed split directly for $O(1)$.
- **All characters equal:** One count remains zero, so every substring satisfies the “or” condition and all `d` entries stay `n`.
- **Entire query valid:** `p = r + 1` and the triangular term alone supplies all substrings.
- **First invalid ending inside the query:** `p = d[l]` cleanly separates fully valid early endings from prefix-counted later endings.
- **Threshold equality:** A count equal to $k$ is allowed; invalidity and shrinking use strict greater-than comparisons.
- **Single-position query:** Its one substring always has one character type count zero and is valid.
- **Distinct queries:** The algorithm does not rely on distinctness and would return repeated answers correctly if duplicates existed.
- **Sentinel `n`:** It acts as an ending just beyond the string, so `min(r+1,d[l])` works without a separate “never invalid” branch.
