## Description

You are given an integer array `nums`.

Rearrange elements of `nums` in **non-decreasing** order of their absolute value.

Return **any** rearranged array that satisfies this condition.

**Note**: The absolute value of an integer x is defined as:

	- `x` if `x >= 0`

	- `-x` if `x < 0`

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,-1,-4,1,5]</span>

**Output:** <span class="example-io">[-1,1,3,-4,5]</span>

**Explanation:**

	- The absolute values of elements in `nums` are 3, 1, 4, 1, 5 respectively.

	- Rearranging them in increasing order, we get 1, 1, 3, 4, 5.

	- This corresponds to `[-1, 1, 3, -4, 5]`. Another possible rearrangement is `[1, -1, 3, -4, 5].`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-100,100]</span>

**Output:** <span class="example-io">[-100,100]</span>

**Explanation:**

	- The absolute values of elements in `nums` are 100, 100 respectively.

	- Rearranging them in increasing order, we get 100, 100.

	- This corresponds to `[-100, 100]`. Another possible rearrangement is `[100, -100]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `-100 <= nums[i] <= 100`
