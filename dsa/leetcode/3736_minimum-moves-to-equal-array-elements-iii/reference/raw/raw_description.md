## Description

You are given an integer array `nums`.

In one move, you may **increase** the value of any single element `nums[i]` by 1.

Return the **minimum total** number of **moves** required so that all elements in `nums` become **equal**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1,3]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

To make all elements equal:

	- Increase `nums[0] = 2` by 1 to make it 3.

	- Increase `nums[1] = 1` by 1 to make it 2.

	- Increase `nums[1] = 2` by 1 to make it 3.

Now, all elements of `nums` are equal to 3. The minimum total moves is `3`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,4,5]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

To make all elements equal:

	- Increase `nums[0] = 4` by 1 to make it 5.

	- Increase `nums[1] = 4` by 1 to make it 5.

Now, all elements of `nums` are equal to 5. The minimum total moves is `2`.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`
