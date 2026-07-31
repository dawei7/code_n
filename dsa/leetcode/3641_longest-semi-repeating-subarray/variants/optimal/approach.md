## General

Maintain a sliding window `[left, right]` with a frequency map and a counter `repeating_values` for how many distinct values currently have frequency at least two.

When a new rightmost value raises its frequency from one to two, increment `repeating_values`. Later copies do not increment it again because the value was already classified as repeating.

If the counter exceeds `k`, advance `left`. When removing a value whose current frequency is exactly two, its new frequency becomes one, so decrement `repeating_values`. Removing from any other frequency does not change whether that value repeats.

Once the window is feasible, record its length. For each right endpoint, the shrinking loop stops at the smallest left endpoint that restores the limit, so this is the longest feasible window ending there. Taking the maximum over all endpoints yields the global optimum.

## Complexity detail

Let $n$ be the array length. Each endpoint moves forward at most $n$ times, so time is $O(n)$. The frequency map stores at most the number of distinct values in the current window, bounded by $O(n)$ auxiliary space.

The benchmark uses $S=n$. The accepted window is $O(S)$, while extending a frequency count from every left endpoint takes $O(S^2)$ time.

## Alternatives and edge cases

- **Enumerate every subarray:** Maintaining counts avoids recomputing them from scratch but still examines $O(n^2)$ endpoint pairs.
- **Count duplicate occurrences:** This misreads the contract; one value contributes exactly one to the limit whenever its frequency is greater than one.
- **Frequency reaches two:** This is the only insertion transition that increases the repeating-value count.
- **Frequency falls to one:** This is the only removal transition that decreases the count.
- **k equals zero:** The window must contain only distinct values.
- **Many copies of one value:** They consume one repeating-value allowance regardless of multiplicity.
- **All unique values:** The entire array is feasible even when `k = 0`.
- **Large k:** If it covers every repeated distinct value, the full array is optimal.
