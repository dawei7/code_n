## General
**Count valid subarrays by their right endpoint**

Track `last_too_large`, the most recent index whose value exceeds `right`, and `last_in_range`, the most recent index whose value lies in `[left, right]`. Values below `left` update neither position.

**Choose every legal starting index**

For a subarray ending at the current index to be valid, it must start after `last_too_large` and at or before `last_in_range`. The number of such starts is `last_in_range - last_too_large` when the in-range index is newer; add that quantity to the answer.

Starting after the too-large value guarantees every element is at most `right`. Starting no later than the latest in-range value guarantees the subarray contains a value at least `left`, while every later element that is not in range is below `left`. These conditions are exactly equivalent to a maximum in `[left, right]`, so each valid subarray is counted once at its unique ending index.

## Complexity detail
The scan processes each of the `n` elements once, taking $O(n)$ time. It stores two indices and the running total, for $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Difference of upper-bound counts:** Count subarrays with maximum at most `right` and subtract those with maximum below `left`; two linear run-length scans give the same result.
- **Monotonic stack:** Contribution counting by each element's maximum span is possible but unnecessarily complex here.
- **Enumerate all subarrays:** Updating a running maximum for every start is correct but takes $O(n^2)$ time.
- **All values below `left`:** No subarray contains a qualifying maximum.
- **Value above `right`:** It resets the earliest allowed starting boundary.
- **Values equal to a bound:** Both `left` and `right` are inclusive and update `last_in_range`.
- **Trailing small values:** They extend every valid subarray whose latest qualifying value remains after the last too-large value.
