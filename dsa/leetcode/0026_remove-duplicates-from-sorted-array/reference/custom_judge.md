## Custom Judge

LeetCode validates the in-place result by performing these checks:

1. Call `removeDuplicates(nums)` and store its returned value as `k`.
2. Require `k` to equal the expected number of distinct values.
3. For every index from `0` through `k-1`, require `nums[i]` to equal the corresponding expected sorted value.

Values stored at indices $k$ and beyond are never examined.
