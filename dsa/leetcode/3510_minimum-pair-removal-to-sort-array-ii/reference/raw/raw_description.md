## Description

Given an array `nums`, you can perform the following operation any number of times:

	- Select the **adjacent** pair with the **minimum** sum in `nums`. If multiple such pairs exist, choose the leftmost one.

	- Replace the pair with their sum.

Return the **minimum number of operations** needed to make the array **non-decreasing**.

An array is said to be **non-decreasing** if each element is greater than or equal to its previous element (if it exists).

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,2,3,1]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- The pair `(3,1)` has the minimum sum of 4. After replacement, `nums = [5,2,4]`.

	- The pair `(2,4)` has the minimum sum of 6. After replacement, `nums = [5,6]`.

The array `nums` became non-decreasing in two operations.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,2]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The array `nums` is already sorted.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`
