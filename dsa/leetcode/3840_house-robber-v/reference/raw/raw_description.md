## Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed and is protected by a security system with a color code.

You are given two integer arrays `nums` and `colors`, both of length `n`, where `nums[i]` is the amount of money in the `i^th` house and `colors[i]` is the color code of that house.

You **cannot rob two adjacent** houses if they share the **same color** code.

Return the **maximum** amount of money you can rob.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,4,3,5], colors = [1,1,2,2]</span>

**Output:** <span class="example-io">9</span>

**Explanation:**

	- Choose houses `i = 1` with `nums[1] = 4` and `i = 3` with `nums[3] = 5` because they are non-adjacent.

	- Thus, the total amount robbed is `4 + 5 = 9`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,1,2,4], colors = [2,3,2,2]</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

	- Choose houses `i = 0` with `nums[0] = 3`, `i = 1` with `nums[1] = 1`, and `i = 3` with `nums[3] = 4`.

	- This selection is valid because houses `i = 0` and `i = 1` have different colors, and house `i = 3` is non-adjacent to `i = 1`.

	- Thus, the total amount robbed is `3 + 1 + 4 = 8`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [10,1,3,9], colors = [1,1,1,2]</span>

**Output:** <span class="example-io">22</span>

**Explanation:**

	- Choose houses `i = 0` with `nums[0] = 10`, `i = 2` with `nums[2] = 3`, and `i = 3` with `nums[3] = 9`.

	- This selection is valid because houses `i = 0` and `i = 2` are non-adjacent, and houses `i = 2` and `i = 3` have different colors.

	- Thus, the total amount robbed is `10 + 3 + 9 = 22`.

</div>

**Constraints:**

	- `1 <= n == nums.length == colors.length <= 10^5`

	- `1 <= nums[i], colors[i] <= 10^5`
