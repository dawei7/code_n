## Description

You are given an integer array `nums`.

A <span data-keyword="subarray">subarray</span> `nums[l..r]` is **alternating** if one of the following holds:

	- `nums[l] < nums[l + 1] > nums[l + 2] < nums[l + 3] > ...`

	- `nums[l] > nums[l + 1] < nums[l + 2] > nums[l + 3] < ...`

In other words, if we compare adjacent elements in the subarray, then the comparisons alternate between **strictly** greater and **strictly** smaller.

You can remove **at most one** element from `nums`. Then, you select an alternating subarray from `nums`.

Return an integer denoting the **maximum** **length** of the alternating subarray you can select.

A subarray of length 1 is considered alternating.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1,3,2]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

	- Choose not to remove elements.

	- Select the entire array `[<u>**2, 1, 3, 2**</u>]`, which is alternating because `2 > 1 < 3 > 2`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,2,1,2,3,2,1]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

	- Choose to remove `nums[3]` i.e., `[3, 2, 1, <u>**2**</u>, 3, 2, 1]`. The array becomes `[3, 2, 1, 3, 2, 1]`.

	- Select the subarray `[3, **<u>2, 1, 3, 2</u>**, 1]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [100000,100000]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- Choose not to remove elements.

	- Select the subarray `[100000, <u>**100000**</u>]`.

</div>

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
