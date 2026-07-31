## Description

An integer array `nums` has length $n$. Consider a positive integer $k$ that divides $n$, so the array can be split into consecutive subarrays whose lengths are all exactly $k$.

Within each fixed subarray, any number of cyclic rotations may be performed independently, in either direction. Rotating moves values around that subarray but never transfers a value across one of its boundaries.

The integer $k$ is **sortable** when some choices of these rotations make the entire array non-decreasing. Determine every sortable divisor $k$ of $n$ and return their sum.
