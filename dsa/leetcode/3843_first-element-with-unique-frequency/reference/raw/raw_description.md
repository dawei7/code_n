## Description

You are given an integer array `nums`.

Return an integer denoting the **first** element (scanning from left to right) in `nums` whose **frequency** is **unique**. That is, no other integer appears the same number of times in `nums`. If there is no such element, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [20,10,30,30]</span>

**Output:** <span class="example-io">30</span>

**Explanation:**

	- 20 appears once.

	- 10 appears once.

	- 30 appears twice.

	- The frequency of 30 is unique because no other integer appears exactly twice.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [20,20,10,30,30,30]</span>

**Output:** <span class="example-io">20</span>

**Explanation:**

	- 20 appears twice.

	- 10 appears once.

	- 30 appears 3 times.

	- The frequency of 20, 10, and 30 are unique. The first element that has unique frequency is 20.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [10,10,20,20]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

	- 10 appears twice.

	- 20 appears twice.

	- No element has a unique frequency.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
