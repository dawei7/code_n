## Description

You are given an integer array `nums`.

A **<span data-keyword="subarray-nonempty">subarray</span>** of `nums` is called **centered** if the sum of its elements is **equal to at least one** element within that **same subarray**.

Return the number of **centered subarrays** of `nums`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-1,1,0]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

	- All single-element subarrays (`[-1]`, `[1]`, `[0]`) are centered.

	- The subarray `[1, 0]` has a sum of 1, which is present in the subarray.

	- The subarray `[-1, 1, 0]` has a sum of 0, which is present in the subarray.

	- Thus, the answer is 5.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,-3]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

Only single-element subarrays (`[2]`, `[-3]`) are centered.

</div>

**Constraints:**

	- `1 <= nums.length <= 500`

	- `-10^5 <= nums[i] <= 10^5`
