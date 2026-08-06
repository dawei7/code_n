## Description

An inaccessible integer array contains equal values at every position except one, whose value is strictly larger. Locate the index of that unique larger integer without reading individual elements directly.

The supplied `ArrayReader` reports the array length and compares the sums of two inclusive subarrays. `compareSub(l, r, x, y)` returns 1, 0, or -1 according to whether the first sum is greater than, equal to, or less than the second. Use at most 20 sum-comparison calls and return the large value's index.
