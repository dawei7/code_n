## General

Let $n$ be the number of elements.

**Summarize all windows ending at one index**

Maintain the length of the longest suffix ending at the current element in which every adjacent value rises by exactly one. If the current value equals the previous value plus one, extend that length. Otherwise reset it to one, because the current element alone begins the next possible run.

After processing index \`i\`, a complete length-$k$ window ends there when \`i >= k - 1\`. Every adjacent pair in that window is valid exactly when the maintained suffix length is at least $k$. In that case the window is ascending, and its final value \`nums[i]\` is its maximum and power. Otherwise emit \`-1\`.

The suffix summary starts correctly at one for the first element. Each later comparison either proves that the previous valid suffix extends through the new element or proves that no suffix containing the previous boundary remains valid, so resetting to one is exact. Therefore the length test recognizes precisely the valid windows. Processing every possible ending index emits all $n-k+1$ answers in order.

**Why the expanded limits matter**

The output itself can contain nearly $10^5$ entries. Rechecking $k-1$ pairs for each overlapping window can become quadratic when $k$ grows with $n$, whereas the suffix length shares all adjacency work across windows.

## Complexity detail

Each element participates in one adjacent comparison and at most one output append, giving $O(n)$ time. Excluding the required result, only a counter and loop variables are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Rescan each window:** Directly checking every adjacent pair costs $O(nk)$ and is too slow at the larger limits.
- **Prefix count of broken boundaries:** Recording cumulative invalid-pair counts also answers each window in $O(1)$ after $O(n)$ preprocessing, but uses $O(n)$ extra space.
- **Deque for window maxima:** A monotonic deque finds maxima but does not verify exact consecutive order.
- Every singleton window is valid when $k=1$.
- A run longer than $k$ supports several overlapping valid windows.
- Equal values, decreases, and upward gaps all reset the run.
- When $k=n$, the result contains exactly one entry.
- Values near $10^6$ follow the same adjacency rule without overflow in supported languages.
- Only complete windows produce output entries.
