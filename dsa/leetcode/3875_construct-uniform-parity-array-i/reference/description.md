## Description

You are given an array `nums1` containing `n` distinct integers. Construct another length-`n` array, `nums2`, whose values all have the same parity: they must be either all odd or all even.

For every index `i`, choose exactly one of these assignments, in any order:

- Keep its original value: `nums2[i] = nums1[i]`.
- Subtract another original value: `nums2[i] = nums1[i] - nums1[j]` for some index `j` with $j\ne i$.

Return `true` when such a uniform-parity array can be constructed, and return `false` otherwise.
