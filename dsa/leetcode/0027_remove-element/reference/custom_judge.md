## Custom Judge

LeetCode checks the in-place result as follows:

1. Build the expected collection of values not equal to `val` and sort it.
2. Call `removeElement(nums, val)` and require its result `k` to equal the expected collection length.
3. Sort only `nums[0:k]`, then compare that prefix element by element with the expected collection.

The judge therefore accepts any order for the first $k$ retained values and ignores every later position.
