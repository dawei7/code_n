## Description

You are given a **0-indexed** integer array `nums`.

We say that an integer x is **expressible** from `nums` if there exist some integers `0 <= index_1 < index_2 < ... < index_k < nums.length` for which `nums[index_1] | nums[index_2] | ... | nums[index_k] = x`. In other words, an integer is expressible if it can be written as the bitwise OR of some subsequence of `nums`.

Return *the minimum **positive non-zero integer** that is not **expressible from *`nums`.
