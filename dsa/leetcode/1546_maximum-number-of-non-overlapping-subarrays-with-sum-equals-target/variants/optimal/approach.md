## General
**Recognize a target-sum interval with prefix sums**

Within the portion of the array that remains available, maintain the running prefix sum and a set of prefix sums seen since the last selected interval ended. A subarray ending at the current position sums to `target` exactly when an earlier prefix equals `prefix - target`. Initializing the set with zero also recognizes an interval that starts at the beginning of the currently available portion.

**Greedily take the earliest finishing interval**

As soon as any target-sum subarray ends, select one and increment the answer. This is the standard earliest-finish rule for maximizing the number of non-overlapping intervals: if an optimal selection uses a first interval ending later, replacing it with the currently found interval cannot invalidate any subsequent interval and leaves at least as much suffix available. Repeating the exchange argument after each selection proves that the greedy count is optimal.

The exact starting boundary of the chosen interval does not need to be recovered, because all earlier positions become unavailable regardless. Only its earliest possible ending matters to the remaining capacity.

**Reset state at the chosen boundary**

After accepting an interval, clear all prior prefix sums and restart with prefix zero immediately after its end. This prevents every later recognized interval from reaching back into already consumed positions. If no interval ends at the current element, add the current prefix to the set and continue.

This scan recognizes the earliest possible finishing interval in each remaining suffix, selects it, and then applies the same argument independently to what remains. Therefore every counted interval is valid and disjoint, and no alternative selection can contain more intervals.

## Complexity detail
The algorithm visits each of the $n$ values once. Prefix addition, set membership, insertion, and reset take expected constant time, giving $O(n)$ expected time. At most $n+1$ distinct prefix sums can be stored before a selection, so auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Dynamic programming over all intervals:** test every start and end while tracking the best count before each start; this is correct but takes $O(n^2)$ time.
- **Enumerate then schedule intervals:** collecting every target-sum interval can itself require $O(n^2)$ output space before interval scheduling begins.
- **Sliding window:** shrinking based on whether the sum is too large fails when negative values destroy monotonicity.
- A selected subarray may contain one element.
- The answer can be zero when no contiguous sum equals `target`.
- When `target = 0`, individual zeroes and longer cancelling ranges must both be handled.
- Resetting the prefix set after a selection is essential; retaining old prefixes can count overlapping intervals.
- Repeated prefix sums are valid and naturally handled by a set because only existence, not multiplicity, is needed.
- Negative targets and negative array values require no special branch.
