## Description

You are given a **0-indexed** array of integers `nums` of length `n`, and two **positive** integers `k` and `dist`.

The **cost** of an array is the value of its **first** element. For example, the cost of `[1,2,3]` is `1` while the cost of `[3,4,1]` is `3`.

You need to divide `nums` into `k` **disjoint contiguous **<span data-keyword="subarray-nonempty">subarrays</span>, such that the difference between the starting index of the **second** subarray and the starting index of the `kth` subarray should be **less than or equal to** `dist`. In other words, if you divide `nums` into the subarrays `nums[0..(i_1 - 1)], nums[i_1..(i_2 - 1)], ..., nums[i_k-1..(n - 1)]`, then `i_k-1 - i_1 <= dist`.

Return *the **minimum** possible sum of the cost of these* *subarrays*.
