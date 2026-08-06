## Description

Given an integer array `nums` and an integer `k`, consider two indices $i < j$. For every such pair, define `sum = nums[i] + nums[j]`. The index relation makes the two positions distinct even when their stored integer values happen to be equal.

Only sums that are strictly less than `k` are eligible; equality does not satisfy the comparison. Return the greatest eligible sum across all pairs. If no pair of indices produces a sum below `k`, return `-1`.
