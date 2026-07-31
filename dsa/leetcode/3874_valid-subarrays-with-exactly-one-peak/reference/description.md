## Description

You are given an integer array `nums` of length `n` and an integer `k`.

An index `i` is a **peak** of the original array when it is strictly inside the array and `nums[i]` is strictly greater than both adjacent values. In other words, $0<i<n-1$, `nums[i] > nums[i - 1]`, and `nums[i] > nums[i + 1]` must all hold.

A non-empty contiguous subarray `[l, r]` is **valid** when it contains exactly one of those original-array peak indices, say `i`, and neither endpoint is more than `k` positions from that peak: $i-l\le k$ and $r-i\le k$.

Return the number of valid subarrays of `nums`.
