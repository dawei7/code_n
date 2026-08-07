## Description

You are given an integer array `nums` consisting of **unique** integers.

Originally, `nums` contained **every integer** within a certain range. However, some integers might have gone **missing** from the array.

The **smallest** and **largest** integers of the original range are still present in `nums`.

Return a **sorted** list of all the missing integers in this range. If no integers are missing, return an **empty** list.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,4,2,5]</span>

**Output:** <span class="example-io">[3]</span>

**Explanation:**

The smallest integer is 1 and the largest is 5, so the full range should be `[1,2,3,4,5]`. Among these, only 3 is missing.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7,8,6,9]</span>

**Output:** <span class="example-io">[]</span>

**Explanation:**

The smallest integer is 6 and the largest is 9, so the full range is `[6,7,8,9]`. All integers are already present, so no integer is missing.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,1]</span>

**Output:** <span class="example-io">[2,3,4]</span>

**Explanation:**

The smallest integer is 1 and the largest is 5, so the full range should be `[1,2,3,4,5]`. The missing integers are 2, 3, and 4.

</div>

**Constraints:**

	- `2 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`
