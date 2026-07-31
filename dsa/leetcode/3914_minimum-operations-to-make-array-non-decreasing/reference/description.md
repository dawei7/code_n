## Description

Given an integer array `nums`, an operation selects any non-empty contiguous subarray `nums[l..r]` and adds the same positive integer `x` to every selected element. Operations may use different subarrays and different positive values.

The goal is to make `nums` non-decreasing, meaning `nums[i] <= nums[i + 1]` at every adjacent pair. The cost is the sum of the chosen `x` values—not the number of operations or the number of elements changed. Return the smallest possible total cost over all valid operation sequences.
