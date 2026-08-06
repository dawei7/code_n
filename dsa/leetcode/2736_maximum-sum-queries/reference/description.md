## Description

You are given two **0-indexed** integer arrays `nums1` and `nums2`, each of length `n`, and a **1-indexed 2D array** `queries` where `queries[i] = [x_i, y_i]`.

For the `i^th` query, find the **maximum value** of `nums1[j] + nums2[j]` among all indices `j` `(0 <= j < n)`, where `nums1[j] >= x_i` and `nums2[j] >= y_i`, or **-1** if there is no `j` satisfying the constraints.

Return *an array *`answer`* where *`answer[i]`* is the answer to the *`i^th`* query.*
