## Description

You are given two arrays `nums` and `andValues` of length `n` and `m` respectively.

The **value** of an array is equal to the **last** element of that array.

You have to divide `nums` into `m` **disjoint contiguous** <span data-keyword="subarray-nonempty">subarrays</span> such that for the `i^th` subarray `[l_i, r_i]`, the bitwise `AND` of the subarray elements is equal to `andValues[i]`, in other words, `nums[l_i] & nums[l_i + 1] & ... & nums[r_i] == andValues[i]` for all `1 <= i <= m`, where `&` represents the bitwise `AND` operator.

Return *the **minimum** possible sum of the **values** of the *`m`* subarrays *`nums`* is divided into*. *If it is not possible to divide *`nums`* into *`m`* subarrays satisfying these conditions, return* `-1`.
