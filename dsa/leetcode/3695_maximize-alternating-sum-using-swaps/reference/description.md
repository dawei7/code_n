## Description

You are given an integer array `nums`.

You want to maximize the **alternating sum** of `nums`, which is defined as the value obtained by **adding** elements at even indices and **subtracting** elements at odd indices. That is, `nums[0] - nums[1] + nums[2] - nums[3]...`

You are also given a 2D integer array `swaps` where `swaps[i] = [p_i, q_i]`. For each pair `[p_i, q_i]` in `swaps`, you are allowed to swap the elements at indices `p_i` and `q_i`. These swaps can be performed any number of times and in any order.

Return the maximum possible **alternating sum** of `nums`.
