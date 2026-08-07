## Description

Given an array `nums`, you have to get the **maximum** score starting from index 0 and **hopping** until you reach the last element of the array.

In each **hop**, you can jump from index `i` to an index `j > i`, and you get a **score** of `(j - i) * nums[j]`.

Return the *maximum score* you can get.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,5,8]</span>

**Output:** <span class="example-io">16</span>

**Explanation:**

There are two possible ways to reach the last element:

	- `0 -> 1 -> 2` with a score of `(1 - 0) * 5 + (2 - 1) * 8 = 13`.

	- `0 -> 2` with a score of `(2 - 0) * 8 = 16`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,5,2,8,9,1,3]</span>

**Output:** <span class="example-io">42</span>

**Explanation:**

We can do the hopping `0 -> 4 -> 6` with a score of `(4 - 0) * 9 + (6 - 4) * 3 = 42`.

</div>

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
