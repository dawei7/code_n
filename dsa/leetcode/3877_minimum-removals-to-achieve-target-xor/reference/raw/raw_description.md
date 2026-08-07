## Description

You are given an integer array `nums` and an integer `target`.

You may remove **any** number of elements from `nums` (possibly zero).

Return the **minimum** number of removals required so that the **bitwise XOR** of the remaining elements equals `target`. If it is impossible to achieve `target`, return -1.

The bitwise XOR of an empty array is 0.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3], target = 2</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- Removing `nums[1] = 2` leaves `[nums[0], nums[2]] = [1, 3]`.

	- The XOR of `[1, 3]` is 2, which equals `target`.

	- It is not possible to achieve XOR = 2 in less than one removal, therefore the answer is 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,4], target = 1</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

It is impossible to remove elements to achieve `target`. Thus, the answer is -1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7], target = 7</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The XOR of all elements is `nums[0] = 7`, which equals `target`. Thus, no removal is needed.

</div>

**Constraints:**

	- `1 <= nums.length <= 40`

	- `0 <= nums[i] <= 10^4`

	- `0 <= target <= 10^4`
