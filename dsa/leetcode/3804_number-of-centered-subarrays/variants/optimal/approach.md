## General

Fix a left endpoint and extend the right endpoint one position at a time. Maintain both the running sum of the current interval and a set containing every value encountered between the two endpoints.

After adding `nums[right]`, the running total is exactly the sum of `nums[left:right + 1]`, and the set contains exactly the values present in that subarray. The interval is centered precisely when the running total belongs to the set, so increment the answer on that condition.

The nested endpoint loops visit every nonempty contiguous interval once. For each one, the maintained state gives its exact sum and membership set, making the test equivalent to the definition. Therefore every centered subarray is counted once and no other interval is counted.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. There are $N(N+1)/2$ subarrays, and each extension performs expected constant-time set insertion and membership work, giving $O(N^2)$ time. The set for one fixed left endpoint can contain at most $N$ values and is discarded before moving to the next endpoint, so auxiliary space is $O(N)$.

## Alternatives and edge cases

- **Recompute each interval:** Summing and scanning every subarray from scratch is correct but takes $O(N^3)$ time.
- **Store only the running sum:** The sum alone cannot reveal whether that value occurs inside the current interval; a membership structure is still needed.
- **Single-element subarrays:** Every one is centered because its sum equals its sole element.
- **Duplicate values:** A set is sufficient because the condition asks whether the sum occurs at least once, not how often it occurs.
- **Zero and negative values:** No monotonicity is available for pruning endpoint extensions; all intervals must still be considered.
