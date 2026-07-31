## General

Every candidate has the same length, so two consecutive candidates differ by only one outgoing value and one incoming value. Maintain the sum of the current window and a frequency map for exactly the values in that window instead of rebuilding both pieces of information for every starting position.

For each new right endpoint, add its value to the sum and increment its frequency. Once more than $k$ elements have been processed, remove `nums[right - k]` from the sum and decrement its frequency. Delete the map entry when that count reaches zero; therefore, the number of keys always equals the number of distinct values currently inside the window.

After the removal, any window ending at `right` has length exactly $k$. It is almost unique precisely when the map contains at least $m$ keys, so its maintained sum is eligible to update the answer. Each length-$k$ subarray appears once as this current window, which means the greatest eligible sum cannot be missed. All values are positive, so retaining the initial answer `0` gives the required result when no window qualifies.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each array value enters the window once and leaves it at most once. With expected constant-time hash-map operations, the total time is $O(n)$.

The frequency map contains at most the $k$ distinct values in the current window, so the auxiliary space is $O(k)$.

## Alternatives and edge cases

- **Rebuild every candidate:** Slicing each length-$k$ window and recomputing its set and sum is straightforward, but it takes $O(nk)$ time.
- **Prefix sums plus rebuilt sets:** Prefix sums make each window sum constant-time, yet rebuilding a set for every window still leaves $O(nk)$ work in the worst case.
- **Threshold rather than exact count:** A window with more than $m$ distinct values is valid; checking equality would reject legitimate candidates.
- **Repeated values:** Frequencies, rather than a plain set, are needed because removing one occurrence must not remove a value that remains elsewhere in the window.
- **Zero-count entries:** An exhausted frequency must be deleted or the map's key count will overstate the current number of distinct values.
- **No qualifying window:** If every candidate has fewer than $m$ distinct values, the answer remains `0`.
- **Single-element window:** When $k=m=1$, every individual value is a candidate and the maximum array value is returned.
