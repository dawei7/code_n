## Description

You are given an integer array `nums`.

Return the **smallest absent positive** integer in `nums` such that it is **strictly greater** than the **average** of all elements in `nums`.

The **average** of an array is defined as the sum of all its elements divided by the number of elements.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,5]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

	- The average of `nums` is `(3 + 5) / 2 = 8 / 2 = 4`.

	- The smallest absent positive integer greater than 4 is 6.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-1,1,2]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- ​​​​​​​The average of `nums` is `(-1 + 1 + 2) / 3 = 2 / 3 = 0.667`.

	- The smallest absent positive integer greater than 0.667 is 3.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,-1]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- The average of `nums` is `(4 + (-1)) / 2 = 3 / 2 = 1.50`.

	- The smallest absent positive integer greater than 1.50 is 2.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `-100 <= nums[i] <= 100`​​​​​​​
