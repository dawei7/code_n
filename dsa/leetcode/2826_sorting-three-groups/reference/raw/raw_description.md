## Description

You are given an integer array `nums`. Each element in `nums` is 1, 2 or 3. In each operation, you can remove an element from `nums`. Return the **minimum** number of operations to make `nums` **non-decreasing**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1,3,2,1]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

One of the optimal solutions is to remove `nums[0]`, `nums[2]` and `nums[3]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,2,1,3,3]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

One of the optimal solutions is to remove `nums[1]` and `nums[2]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,2,2,2,3,3]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

`nums` is already non-decreasing.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 3`

**Follow-up:** Can you come up with an algorithm that runs in `O(n)` time complexity?
