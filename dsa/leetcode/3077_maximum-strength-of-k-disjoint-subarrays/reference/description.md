## Description

You are given an array of integers `nums` with length `n`, and a positive **odd** integer `k`.

Select exactly **`k`** disjoint <span data-keyword="subarray-nonempty">subarrays</span> **`sub_1, sub_2, ..., sub_k`** from `nums` such that the last element of `sub_i` appears before the first element of `sub_{i+1}` for all `1 <= i <= k-1`. The goal is to maximize their combined strength.

The strength of the selected subarrays is defined as:

`strength = k * sum(sub_1)- (k - 1) * sum(sub_2) + (k - 2) * sum(sub_3) - ... - 2 * sum(sub_{k-1}) + sum(sub_k)`

where **`sum(sub_i)`** is the sum of the elements in the `i`-th subarray.

Return the **maximum** possible strength that can be obtained from selecting exactly **`k`** disjoint subarrays from `nums`.

**Note** that the chosen subarrays **don't** need to cover the entire array.
