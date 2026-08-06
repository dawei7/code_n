## Description

We have an array of integers, `nums`, and an array of `requests` where `requests[i] = [start_i, end_i]`. The `i^th` request asks for the sum of `nums[start_i] + nums[start_i + 1] + ... + nums[end_i - 1] + nums[end_i]`. Both `start_i` and `end_i` are *0-indexed*.

Return *the maximum total sum of all requests **among all permutations** of* `nums`.

Since the answer may be too large, return it **modulo** `10^9 + 7`.
