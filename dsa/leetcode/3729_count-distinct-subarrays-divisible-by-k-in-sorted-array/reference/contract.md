## Function Contract

**Inputs**

- `nums`: An integer array already sorted in non-descending order.
- `k`: The positive divisor used to test each subarray sum.

A subarray is a nonempty contiguous sequence. Two occurrences with identical value sequences represent the same distinct subarray even when they use different indices.

**Return value**

Return the integer number of different subarray value sequences whose element sum is congruent to $0$ modulo `k`.
