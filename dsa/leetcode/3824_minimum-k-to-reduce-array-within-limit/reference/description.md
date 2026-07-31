## Description

You are given a positive integer array `nums`.

For any positive integer `k`, let `nonPositive(nums, k)` be the minimum number of operations required to make every element of `nums` non-positive. During one operation, choose an index `i` and subtract `k` from `nums[i]`.

The same `k` is used throughout the operation sequence; each operation may choose its index independently.

Return the smallest positive integer `k` for which

$$
\texttt{nonPositive(nums, k)} \le k^2.
$$
