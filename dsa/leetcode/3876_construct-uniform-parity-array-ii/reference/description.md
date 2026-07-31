## Description

You are given an array `nums1` containing `n` distinct integers. Construct another length-`n` array, `nums2`, whose elements are either all odd or all even.

For each index `i`, choose exactly one of these assignments, in any order:

- Keep its original value: `nums2[i] = nums1[i]`.
- Subtract another original value: `nums2[i] = nums1[i] - nums1[j]` for an index $j\ne i$, provided that `nums1[i] - nums1[j] >= 1`.

Return `true` if a uniform-parity array can be constructed under those rules. Otherwise, return `false`.
