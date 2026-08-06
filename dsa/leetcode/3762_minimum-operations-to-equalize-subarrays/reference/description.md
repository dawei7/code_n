## Description

You are given an integer array `nums` and an integer `k`.

In one operation, you can **increase or decrease **any element of `nums` by **exactly** `k`.

You are also given a 2D integer array `queries`, where each `queries[i] = [l_i, r_i]`.

For each query, find the **minimum** number of operations required to make **all** elements in the **<span data-keyword="subarray-nonempty">subarray</span>** `nums[l_i..r_i]` **equal**. If it is impossible, the answer for that query is `-1`.

Return an array `ans`, where `ans[i]` is the answer for the `i^th` query.
