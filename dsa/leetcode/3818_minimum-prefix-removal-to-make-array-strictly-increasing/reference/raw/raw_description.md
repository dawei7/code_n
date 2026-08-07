## Description

You are given an integer array `nums`.

You need to remove **exactly** one prefix (possibly empty) from nums.

Return an integer denoting the **minimum** length of the removed <span data-keyword="array-prefix">prefix</span> such that the remaining array is **<span data-keyword="strictly-increasing-array">strictly increasing</span>**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,-1,2,3,3,4,5]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Removing the `prefix = [1, -1, 2, 3]` leaves the remaining array `[3, 4, 5]` which is strictly increasing.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,3,-2,-5]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

Removing the `prefix = [4, 3, -2]` leaves the remaining array `[-5]` which is strictly increasing.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The array `nums = [1, 2, 3, 4]` is already strictly increasing so removing an empty prefix is sufficient.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9​​​​​​​`
