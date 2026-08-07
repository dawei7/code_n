## Description

You are given an integer array `nums`.

An array is called **parity alternating** if for every index `i` where `0 <= i < n - 1`, `nums[i]` and `nums[i + 1]` have different parity (one is even and the other is odd).

In one operation, you may choose any index `i` and either increase `nums[i]` by 1 or decrease `nums[i]` by 1.

Return an integer array `answer` of length 2 where:

	- `answer[0]` is the **minimum** number of operations required to make the array parity alternating.

	- `answer[1]` is the **minimum** possible value of `max(nums) - min(nums)` taken over all arrays that are parity alternating and can be obtained by performing **exactly** `answer[0]` operations.

An array of length 1 is considered parity alternating.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-2,-3,1,4]</span>

**Output:** <span class="example-io">[2,6]</span>

**Explanation:**

Applying the following operations:

	- Increase `nums[2]` by 1, resulting in `nums = [-2, -3, 2, 4]`.

	- Decrease `nums[3]` by 1, resulting in `nums = [-2, -3, 2, 3]`.

The resulting array is parity alternating, and the value of `max(nums) - min(nums) = 3 - (-3) = 6` is the minimum possible among all parity alternating arrays obtainable using exactly 2 operations.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,2,-2]</span>

**Output:** <span class="example-io">[1,3]</span>

**Explanation:**

Applying the following operation:

	- Decrease `nums[1]` by 1, resulting in `nums = [0, 1, -2]`.

The resulting array is parity alternating, and the value of `max(nums) - min(nums) = 1 - (-2) = 3` is the minimum possible among all parity alternating arrays obtainable using exactly 1 operation.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7]</span>

**Output:** <span class="example-io">[0,0]</span>

**Explanation:**

No operations are required. The array is already parity alternating, and the value of `max(nums) - min(nums) = 7 - 7 = 0`, which is the minimum possible.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`
