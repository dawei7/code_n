## Description

Given a **circular** array `nums`, find the **maximum** absolute difference between adjacent elements.

**Note**: In a circular array, the first and last elements are adjacent.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,4]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

Because `nums` is circular, `nums[0]` and `nums[2]` are adjacent. They have the maximum absolute difference of `|4 - 1| = 3`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-5,-10,-5]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

The adjacent elements `nums[0]` and `nums[1]` have the maximum absolute difference of `|-5 - (-10)| = 5`.

</div>

**Constraints:**

	- `2 <= nums.length <= 100`

	- `-100 <= nums[i] <= 100`
