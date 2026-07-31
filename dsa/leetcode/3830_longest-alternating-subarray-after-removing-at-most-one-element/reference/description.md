## Description

You are given an integer array `nums`.

A subarray `nums[l..r]` is **alternating** when it follows either of these two patterns:

- `nums[l] < nums[l + 1] > nums[l + 2] < nums[l + 3] > ...`
- `nums[l] > nums[l + 1] < nums[l + 2] > nums[l + 3] < ...`

Equivalently, every comparison between adjacent elements must be strict, and the direction of those comparisons must alternate between greater and smaller.

Before choosing the subarray, you may remove **at most one** element from `nums`; choosing not to remove anything is also allowed. Select an alternating subarray from the array that remains.

Return the maximum possible length of the selected alternating subarray.

A subarray of length $1$ is alternating.
