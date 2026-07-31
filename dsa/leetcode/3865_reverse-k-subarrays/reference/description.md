## Description

You are given an integer array `nums` containing $n$ elements together with an integer `k`.

Partition the original array into exactly `k` contiguous subarrays. Every subarray must have the same length, and their left-to-right order and boundaries are fixed by the original positions.

The input guarantees that $n$ is divisible by `k`, so each subarray contains exactly $n/k$ elements. Reverse the element order inside every subarray without moving an element across a subarray boundary.

Return the array obtained by joining the reversed subarrays in their original block order.
