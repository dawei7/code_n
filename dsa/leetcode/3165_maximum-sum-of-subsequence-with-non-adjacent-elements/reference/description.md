## Description

You are given an array `nums` consisting of integers. You are also given a 2D array `queries`, where `queries[i] = [pos_i, x_i]`.

For query `i`, we first set `nums[pos_i]` equal to `x_i`, then we calculate the answer to query `i` which is the **maximum** sum of a <span data-keyword="subsequence-array">subsequence</span> of `nums` where **no two adjacent elements are selected**.

Return the *sum* of the answers to all queries.

Since the final answer may be very large, return it **modulo** `10^9 + 7`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
