## Description

You are given an integer array `nums` containing only positive values. Every non-empty contiguous subarray contributes one sum, and equal sums from different subarray positions remain separate entries.

Arrange all $N(N+1)/2$ subarray sums in non-decreasing order and return the value at rank `k`, where ranks are one-based.

The choice concerns values rather than intervals: the function returns only the selected sum, not the subarray that produced it. If several subarrays have the same sum, each occurrence keeps its own place in the ordering.
