## Description

You are given an integer array `nums` and an integer `k`. One operation chooses any element and changes it by exactly `k`, either increasing or decreasing it.

You are also given an array `queries`, where `queries[i] = [l_i, r_i]` identifies the inclusive subarray `nums[l_i..r_i]`. For each query independently, determine the minimum number of operations needed to make every value in that subarray equal. If no sequence of permitted operations can do so, its answer is `-1`.

Return an array `ans` in query order, with `ans[i]` holding the result for the $i^{\text{th}}$ query.
