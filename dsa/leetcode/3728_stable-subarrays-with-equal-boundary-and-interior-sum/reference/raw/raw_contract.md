## Function Contract

**Inputs**

- `capacity`: The integer array in which stable contiguous ranges are counted.

Each candidate is a nonempty contiguous subarray identified by inclusive endpoints `l` and `r`. Only candidates with `r - l + 1 >= 3` qualify for consideration. Values and interior sums may be negative, zero, or positive.

**Return value**

Return the integer count of all endpoint pairs `(l, r)` whose subarray satisfies both stability conditions. Overlapping and nested stable subarrays are counted separately.
