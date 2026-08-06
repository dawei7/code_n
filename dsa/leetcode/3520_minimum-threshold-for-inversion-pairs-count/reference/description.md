## Description

Given an integer array `nums`, an inversion pair is a pair of indices $(i,j)$ with $i<j$ and `nums[i] > nums[j]`. A threshold $x$ further restricts an inversion pair by requiring its value difference to be at most $x$, so `nums[i] - nums[j] <= x` must also hold.

Find the minimum integer threshold for which at least `k` inversion pairs satisfy all three conditions. If the array contains fewer than `k` inversion pairs even when every positive difference is allowed, return `-1`.
