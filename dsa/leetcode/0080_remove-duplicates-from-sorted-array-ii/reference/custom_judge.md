## Custom Judge

LeetCode evaluates the in-place result with these checks:

1. Call `removeDuplicates(nums)` and store its return value as `k`.
2. Require `k` to equal the expected retained length.
3. For every index from `0` through `k - 1`, require `nums[i]` to equal the corresponding expected value.

The judge ignores every array position at index `k` or later.
