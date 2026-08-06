## Description

Given an integer array `nums` of length `n`, determine whether three indices `(i, j, k)` can divide the remaining
elements into four nonempty subarrays of equal sum. The separator elements at `i`, `j`, and `k` do not belong to any
of the four subarrays.

The indices must satisfy `0 < i`, `i + 1 < j`, and `j + 1 < k < n - 1`. The four inclusive ranges are `(0, i - 1)`,
`(i + 1, j - 1)`, `(j + 1, k - 1)`, and `(k + 1, n - 1)`, and their sums must all be equal.

Here, a subarray `(l, r)` means the contiguous slice beginning at index `l` and ending at index `r`, with both
endpoints included. Return whether any separator triple meets every condition.
