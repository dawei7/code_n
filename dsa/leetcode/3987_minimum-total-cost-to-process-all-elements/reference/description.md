## Description

You are given an integer array `nums` and an integer `k`.

Initially, you have `k` units of resources.

You must process the elements of `nums` from left to right. To process the `i^th` element, you need `nums[i]` resources.

If your available resources are less than `nums[i]`, you may perform an operation that increases your available resources by `k`. The value of `k` is fixed and does not change throughout the process. The first such operation incurs a cost of 1, the second incurs a cost of 2, and so on.

After processing the `i^th` element, your available resources decrease by `nums[i]`.

Return an integer denoting the **minimum total cost** required to process all elements. Since the answer may be very large, return it **modulo** `10^9 + 7`.
