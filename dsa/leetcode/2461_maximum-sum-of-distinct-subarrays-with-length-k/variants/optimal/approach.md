## General

Every candidate has the same length, so consecutive candidates differ in only two elements: one value leaves from the left and one enters from the right. Maintain a sliding window sum together with a frequency map for the values currently inside the window.

For each new right endpoint, add its value to both structures. Once more than $k$ values have been seen, remove `nums[right - k]`; delete its map entry when its frequency reaches zero. The maintained sum and map then describe exactly the current suffix of length $k$.

A length-$k$ window contains only distinct elements exactly when its frequency map has $k$ keys. In that case compare its maintained sum with the best valid sum seen so far. Since every array value is positive, initializing the answer to zero also supplies the required result when no valid window exists.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each value enters and leaves the sliding window once, and expected hash-map operations are constant time, so total expected time is $O(n)$.

The map stores at most $k$ distinct values from the current window, giving $O(k)$ auxiliary space.

## Alternatives and edge cases

- **Rebuild every window:** Taking a slice, set, and sum for every start is direct but costs $O(nk)$ time.
- **Last-position window:** Moving a variable left boundary past duplicates can also track distinct segments, but the sum must still be evaluated only when the selected suffix has exactly length $k$.
- **No valid window:** Repeated values may invalidate every length-$k$ candidate, in which case the answer remains `0`.
- **Single-element windows:** When $k=1$, every window is distinct, so the result is the maximum array value.
- **Frequency deletion:** Zero-count keys must be removed; otherwise the number of map keys would not equal the number of distinct values currently in the window.
- **Fixed length:** A distinct window shorter or longer than $k$ is not a candidate.
