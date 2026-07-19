## General
**The right endpoint identifies which rotation segment contains `mid`**

A rotated distinct array consists of a high-valued sorted segment followed by a low-valued sorted segment beginning at the minimum. Maintain a closed interval containing that boundary and compare its midpoint with `nums[right]`, which belongs to the interval's ending segment.

**Strict comparison decides whether `mid` is before or at/after the pivot**

If `nums[mid] > nums[right]`, `mid` lies in the high segment while the right endpoint lies in the low segment, so the minimum is strictly to the right and `left = mid + 1`. Otherwise distinctness gives `nums[mid] < nums[right]`; `mid` lies in the low segment and may itself be the minimum, so preserve it with `right = mid`.

The asymmetric updates are deliberate: the greater case proves `mid` is not the minimum, while the lower case does not.

**Boundary convergence leaves the unique pivot index**

The minimum's index always lies in the closed interval `[left, right]`. Every update preserves that index and strictly shortens the interval.

**Trace a pivot between midpoint and right endpoint**

For `[3,4,5,1,2]`, middle value `5` exceeds right value `2`, so discard through `5`. In `[1,2]`, middle value `1` is no greater than `2`, so retain its index as the right boundary; both boundaries meet at `1`.

**The right endpoint reveals which sorted segment contains `mid`**

Distinct values divide a rotated array into a higher-valued prefix followed by a lower-valued suffix whose first element is the minimum. If `nums[mid] > nums[right]`, then `mid` is in the high segment and the minimum must lie strictly to its right. Otherwise `mid` is already in the low segment—or the array is unrotated—so `mid` may itself be the minimum and the search keeps it.

Both updates preserve the minimum inside the closed interval. When the boundaries meet, that interval contains only the minimum's index.

## Complexity detail
Each comparison removes at least half the remaining interval, producing $O(\log n)$ time. Only boundary indices are stored.

## Alternatives and edge cases
- **Linear scan or `min`:** is correct but violates the required logarithmic time.
- **Search for the unique drop:** also takes $O(n)$ if inspected sequentially.
- **Compare only with the first value:** can work with extra boundary handling, but the right-end comparison gives a compact invariant.
- A one-element or unrotated array returns its first value. The minimum may occur at the final index after a rotation by one position.
- Distinctness eliminates the equality case; problem 154 must handle it explicitly and loses logarithmic worst-case time.
