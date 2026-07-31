## Description

You are given an integer array `nums`.

A nonempty subarray is called **stable** when it contains no inversion. Equivalently, there must not be indices $i<j$ within that subarray for which `nums[i] > nums[j]`; its values are therefore in non-decreasing order.

You are also given a two-dimensional integer array `queries` containing $q$ ranges. A query `queries[i] = [l_i,r_i]` asks for the number of stable subarrays lying completely inside the inclusive segment `nums[l_i..r_i]`.

Return an array `ans` of length $q$ in the original query order, where `ans[i]` is the count for the $i$th query.
