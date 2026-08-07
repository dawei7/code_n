## Description

You are given an integer array `nums` and an integer `k`. You can perform the following operation any number of times:

	- Increase or decrease any element of `nums` by 1.

Return the **minimum** number of operations required to ensure that **at least** one <span data-keyword="subarray">subarray</span> of size `k` in `nums` has all elements equal.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,-3,2,1,-4,6], k = 3</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

	- Use 4 operations to add 4 to `nums[1]`. The resulting array is <span class="example-io">`[4, 1, 2, 1, -4, 6]`.</span>

	- <span class="example-io">Use 1 operation to subtract 1 from `nums[2]`. The resulting array is `[4, 1, 1, 1, -4, 6]`.</span>

	- <span class="example-io">The array now contains a subarray `[1, 1, 1]` of size `k = 3` with all elements equal. Hence, the answer is 5.</span>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-2,-2,3,1,4], k = 2</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- The subarray `[-2, -2]` of size `k = 2` already contains all equal elements, so no operations are needed. Hence, the answer is 0.

</div>

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `-10^6 <= nums[i] <= 10^6`

	- `2 <= k <= nums.length`
