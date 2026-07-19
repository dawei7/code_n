## General
**Partition the array at every failed comparison**

Whenever `nums[i] <= nums[i - 1]`, no strictly ascending subarray can cross that boundary. The array is therefore partitioned into maximal ascending runs, and every valid ascending subarray lies entirely inside one of them.

**Keep only the current run sum**

Scan from left to right. If the current value is greater than the previous value, add it to the current run sum. Otherwise begin a new run whose sum is the current value. Track the largest run sum seen.

All values are positive, so within one maximal ascending run its complete sum is at least the sum of any shorter subarray inside it. Consequently, comparing the sums of maximal runs is sufficient. The scan constructs exactly those sums, which proves the reported maximum is correct.

## Complexity detail
The scan visits each of the $n$ values once, taking $O(n)$ time. It retains only the current sum and the best sum, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate every starting position:** Extending each possible ascending subarray is correct but can take $O(n^2)$ time on a fully ascending array.
- **Prefix sums plus boundary search:** Prefix sums can evaluate a known run, but finding and storing all boundaries adds machinery without improving the linear bound.
- **Single element:** Its value is the only valid subarray sum.
- **Equal adjacent values:** Equality breaks the run because ascending means strictly greater, not non-decreasing.
- **Fully descending array:** Every maximal run has length one, so the answer is the largest element.
- **Best run at either edge:** Update the maximum throughout the scan so no special finalization case is needed.
