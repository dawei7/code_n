## Description

You are given an integer array `nums` and a positive integer `k`.

You must choose **exactly** one <span data-keyword="subarray-nonempty">subarray</span> of `nums` and perform **exactly** one of the following operations:

	- Multiply each number in the chosen subarray by `k`.

	- Divide each number in the chosen subarray by `k`.

		<li>When dividing a positive number by `k`, use the **floor** value of the division result.

		- When dividing a negative number by `k`, use the **ceiling** value of the division result.

	</li>

Return the **maximum** possible sum of a **non-empty** subarray in the resulting array.

Note that the subarray chosen for the operation and the subarray chosen for the sum may be **different**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,-2,3,4,-5], k = 2</span>

**Output:** <span class="example-io">14</span>

**Explanation:**

	- Multiply each number in the subarray `[3, 4]` by 2.

	- This results in `nums = [1, -2, 6, 8, -5]`.

	- The subarray with the largest sum is `[6, 8]`, so the output is `6 + 8 = 14`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-5,-4,-3], k = 2</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

	- Divide each number in the subarray `[-3]` by 2.

	- This results in `nums = [-5, -4, -1]`.

	- The subarray with the largest sum is `[-1]`, so the output is -1.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^5 <= nums[i] <= 10^5`

	- `1 <= k <= 10^5`
