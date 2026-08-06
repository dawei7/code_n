## Description

Two 0-indexed integer arrays, `nums1` and `nums2`, have the same length $n$.
For an inclusive range $[l,r]$, choose exactly one value at every index: either
`nums1[i]` or `nums2[i]`.

The range and its choices are balanced when the sum of values chosen from
`nums1` equals the sum chosen from `nums2`. If no value is chosen from one
array, its sum is zero. Two balanced selections are different when either
endpoint differs or at least one index chooses the other array, even when the
two values at that index are equal.

Return the number of different balanced range selections modulo $10^9+7$.
