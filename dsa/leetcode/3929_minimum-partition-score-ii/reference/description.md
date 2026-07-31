## Description

Given a positive integer array `nums`, divide the array in its original order into exactly `k` nonempty contiguous subarrays. Every element must belong to one subarray, so a valid partition is determined by placing `k - 1` cuts between adjacent elements.

If a subarray has element sum $s$, its value is the triangular quantity

$$
T(s)=\frac{s(s+1)}{2}.
$$

The score of a partition is the sum of this value over all `k` subarrays. Return the smallest score attainable by any valid placement of the cuts.
