## Description

You are given an integer array `nums`.

In one operation, you remove the **first three elements** of the current array. If there are fewer than three elements remaining, **all** remaining elements are removed.

Repeat this operation until the array is empty or contains no duplicate values.

Return an integer denoting the number of operations required.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,8,3,6,5,8]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

In the first operation, we remove the first three elements. The remaining elements `[6, 5, 8]` are all distinct, so we stop. Only one operation is needed.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,2]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

After one operation, the array becomes empty, which meets the stopping condition.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,3,5,1,2]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

All elements in the array are distinct, therefore no operations are needed.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
