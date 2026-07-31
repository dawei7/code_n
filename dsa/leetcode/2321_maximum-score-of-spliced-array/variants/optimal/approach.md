## General

**Express a swap as a gain**

Suppose the first array is the score target. Swapping index `i` changes its sum
by `nums2[i] - nums1[i]`. Therefore, swapping one contiguous interval adds the
sum of the corresponding contiguous interval in this difference sequence.
The best improvement is its maximum subarray sum, with zero allowed to
represent no swap.

Run Kadane's algorithm while generating differences directly: extend the
current positive-gain interval or restart at zero, and retain the greatest
gain. Add it to `sum(nums1)`. Repeat with the difference direction reversed to
find the best score when the second array is the target, then take the larger
candidate.

Every legal swap corresponds to exactly one contiguous difference sum for each
target. Kadane's recurrence finds the greatest such sum, and including zero
also covers the no-operation choice. Considering both target arrays therefore
covers the definition of the final score.

## Complexity detail

Let $n$ be the common array length. The sums and two gain scans each take
$O(n)$ time. Kadane's algorithm retains only a current and best gain, so
auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate every interval:** Incrementally summing all possible swaps is correct but takes $O(n^2)$ time.
- **Prefix differences:** Prefix sums can evaluate an interval in constant time, but examining all interval pairs remains quadratic.
- **Store difference arrays:** This preserves linear time but spends unnecessary $O(n)$ auxiliary space.
- **No profitable swap:** A zero gain leaves the larger original sum unchanged.
- **Single element:** The operation merely exchanges the two values, so the larger score cannot improve.
- **Whole-array swap:** Exchanging every position only swaps the two total sums and cannot change their maximum.
