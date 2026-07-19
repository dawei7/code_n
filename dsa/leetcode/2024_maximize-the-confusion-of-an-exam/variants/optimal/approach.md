## General
**Reduce the goal to two uniform targets**

First seek the longest window that can become all `T`. Its exact replacement
cost is the number of `F` characters inside it. Then perform the symmetric
search for a window that can become all `F`, where the cost is its count of
`T` characters. The better of the two searches is the overall answer.

**Maintain the longest affordable window**

For one target symbol, move a right boundary across the key and count
characters that would need replacement. Whenever this cost exceeds `k`, move
the left boundary forward, decreasing the cost when a replaceable character
leaves. Once affordable again, record the window length.

For each right boundary, shrinking stops at the smallest left boundary whose
window costs at most `k`; it is therefore the longest valid window ending
there. Both boundaries only move forward, and the cost always equals the
number of opposite answers in the current window. Each pass finds every
candidate for its chosen target, so their maximum is exactly the best block
of either symbol.

## Complexity detail
Each of the two sliding-window passes moves its left and right boundaries at
most $N$ times, so the total time is $O(N)$. The boundaries, replacement
counter, and best length use $O(1)$ space.

## Alternatives and edge cases
- **One window with symbol counts:** Track both frequencies and keep a window
  valid when its length minus its majority count is at most `k`. This is also
  linear but its stale-maximum optimization requires a subtler argument.
- **Binary search on the answer:** Prefix counts can test whether any window of
  a chosen length is feasible, giving $O(N\log N)$ time.
- **Expand from every start:** This is correct but repeats overlapping work and
  can take $O(N^2)$ time.
- If `k` covers every occurrence of the minority symbol, the entire key is
  achievable.
- An already uniform key returns its full length without needing a change.
- Using at most `k` changes means unused operations never need to be forced.
