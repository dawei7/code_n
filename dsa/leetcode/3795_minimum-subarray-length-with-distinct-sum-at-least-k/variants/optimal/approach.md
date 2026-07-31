## General

All array values are positive, so enlarging a window cannot decrease its distinct-value sum: a newly seen value adds a positive amount, while another copy of an existing value changes nothing. This monotonicity makes a sliding window possible.

Maintain `frequencies` for the current interval, its `distinct_sum`, and a left boundary. When the right boundary receives a value whose frequency was zero, add that value to `distinct_sum`; every additional copy only increments its frequency. Whenever `distinct_sum >= k`, record the current length and advance the left boundary greedily. Removing a value decreases `distinct_sum` only when its frequency becomes zero, because only then has the value disappeared from the window's set.

For each fixed right endpoint, the shrinking loop stops immediately after crossing below `k`, so the final qualifying interval considered before that crossing is the shortest one ending there. Every possible right endpoint is processed, and the best of those endpoint-specific minima is therefore the global minimum. If the threshold is never reached, the sentinel remains unchanged and the algorithm returns `-1`.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. The right pointer visits every element once, and the left pointer also advances at most $N$ times over the entire run. Hash-map operations take expected $O(1)$ time, giving expected $O(N)$ total time. At most $N$ distinct values can be represented in the frequency map, so the auxiliary space is $O(N)$.

## Alternatives and edge cases

- **Enumerate every subarray:** Extending a set from each left endpoint is straightforward but takes $O(N^2)$ time even when the distinct sum is maintained incrementally.
- **Ordinary element sum:** Adding every occurrence solves a different problem; duplicates must contribute only once to the current interval.
- **Frequency exactly one:** A value with frequency two or more is still present and still contributes once. Subtract it only when its frequency falls to zero.
- **One-element answer:** Any `nums[i] >= k` immediately permits a length-one optimum.
- **Impossible threshold:** If the sum of all distinct values in the complete array is below `k`, no subarray qualifies and the answer is `-1`.
- **Exact threshold:** The comparison is inclusive, so `distinct_sum == k` must enter the shrinking loop.
