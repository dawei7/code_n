## Description

You are given an integer array `nums`.

A <span data-keyword="subarray">subarray</span> is **arithmetic** if the difference between consecutive elements in the subarray is constant.

You can replace **at most one** element in `nums` with any **integer**. Then, you select an arithmetic subarray from `nums`.

Return an integer denoting the **maximum** length of the arithmetic subarray you can select.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [9,7,5,10,1]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

	- Replace `nums[3] = 10` with 3. The array becomes `[9, 7, 5, 3, 1]`.

	- Select the subarray `[<u>**9, 7, 5, 3, 1**</u>]`, which is arithmetic because consecutive elements have a common difference of -2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,6,7]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- Replace `nums[0] = 1` with -2. The array becomes `[-2, 2, 6, 7]`.

	- Select the subarray `[<u>**-2, 2, 6**</u>, 7]`, which is arithmetic because consecutive elements have a common difference of 4.

</div>

**Constraints:**

	- `4 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
