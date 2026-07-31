## General

First find the maximum value of the entire input; the contract refers to this
fixed global maximum, not the maximum chosen separately by each subarray.
Process right endpoints from left to right while counting occurrences of that
value in the current window.

After adding a right endpoint, advance `left` while the window still contains
at least `k` maxima. When the loop stops, `left` is the number of valid starting
positions for this right endpoint: every start before `left` retains at least
`k` maxima, while the window beginning at `left` has fewer than `k`. Add `left`
to the answer.

This partitions all qualifying subarrays by their unique right endpoint and
counts each exactly once. Both boundaries move only forward, so shrinking over
the complete scan performs at most $N$ steps.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Finding the global maximum and scanning
the sliding window each take $O(N)$ time. The algorithm stores only counters
and indices, using $O(1)$ space.

## Alternatives and edge cases

- **Enumerate all subarrays:** Maintaining the maximum's count while extending every start is correct but takes $O(N^2)$ time.
- **Store maximum positions:** Using the positions of each occurrence can count contributions combinatorially in $O(N)$ time but requires $O(N)$ additional space.
- **Fewer than `k` maxima globally:** No subarray can qualify, so the answer is zero.
- **`k = 1`:** Every subarray containing at least one occurrence of the global maximum qualifies.
- **All values equal:** The condition becomes a minimum subarray-length condition because every position is a maximum.
- **Large answer:** Up to $N(N+1)/2$ subarrays may qualify, so the result can exceed 32-bit signed range.
