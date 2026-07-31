## Description

You are given an integer array `nums` containing $n$ elements and an integer `k`.

An **inversion** consists of two indices $(i,j)$ for which $i<j$ while `nums[i] > nums[j]`. For any subarray, its inversion count is the number of such index pairs formed entirely by elements of that subarray. Indices in this definition refer to positions within the sequence being examined.

Consider every contiguous subarray of `nums` whose length is exactly `k`. Return the smallest inversion count attained by any one of those fixed-length subarrays.
