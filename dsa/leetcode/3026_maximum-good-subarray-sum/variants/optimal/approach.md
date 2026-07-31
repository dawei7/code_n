## General

**Express every interval through prefix sums.** Let $P[t]$ be the sum of the first $t$ array values. Then the sum of `nums[i..j]` is $P[j+1]-P[i]$. For a fixed right endpoint `j`, a good left endpoint must have value `nums[j] - k` or `nums[j] + k`. The problem is therefore to subtract the smallest eligible $P[i]$ seen for either value.

**Retain only the best prefix for each value.** Maintain a hash map from an encountered array value `v` to the minimum prefix sum immediately before any occurrence of `v`. Before recording the current value, query both values exactly `k` away. Subtracting their stored minima from the prefix through the current element produces the largest good-subarray sum ending here. Keeping a larger prefix for the same `v` could never improve a future answer, so discarding it is safe.

**Distinguish absence from a negative maximum.** A good subarray may have a negative sum, as in the third example. Track whether any eligible endpoint was found instead of initializing the answer to zero. Return zero only if no lookup ever succeeds; otherwise return the best candidate even when it is negative.

For every right endpoint, the map contains exactly the best prefix from every earlier occurrence of each possible left-end value. The two lookups therefore examine all and only legal left endpoints, and selecting their minimum prefixes maximizes the sum. Taking the maximum over all right endpoints proves the final result is optimal.

## Complexity detail

The scan performs two expected $O(1)$ hash lookups and one expected $O(1)$ update per element, giving expected $O(N)$ time. The map stores at most one entry for each distinct value, so it uses $O(N)$ auxiliary space in the worst case.

## Alternatives and edge cases

- **Enumerate every subarray:** Accumulating the sum for every pair of endpoints is correct but costs $O(N^2)$ time.
- **Store every prefix per value:** This preserves enough information but wastes space and later comparison work; only the minimum prefix for a value can maximize a future difference.
- **Maximum prefix instead of minimum:** Because the interval sum subtracts the earlier prefix, retaining the maximum reverses the optimization and can miss the best interval.
- **No good endpoints:** If neither value exactly `k` away has appeared for any right endpoint, return `0`.
- **All good sums are negative:** Return the least negative valid sum rather than clamping the answer to zero.
- **Repeated endpoint values:** A later occurrence can replace an earlier one when its preceding prefix sum is smaller, allowing a shorter or differently positioned interval to win.
- **Both orientations:** Querying `value - k` and `value + k` handles whether the left endpoint is smaller or larger than the right endpoint.
