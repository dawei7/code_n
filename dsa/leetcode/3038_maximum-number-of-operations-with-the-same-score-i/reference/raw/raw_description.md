## Description

You are given an array of integers `nums`. Consider the following operation:

	- Delete the first two elements `nums` and define the *score* of the operation as the sum of these two elements.

You can perform this operation until `nums` contains fewer than two elements. Additionally, the **same** *score* must be achieved in **all** operations.

Return the **maximum** number of operations you can perform.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,2,1,4,5]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- We can perform the first operation with the score `3 + 2 = 5`. After this operation, `nums = [1,4,5]`.

	- We can perform the second operation as its score is `4 + 1 = 5`, the same as the previous operation. After this operation, `nums = [5]`.

	- As there are fewer than two elements, we can't perform more operations.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,5,3,3,4,1,3,2,2,3]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- We can perform the first operation with the score `1 + 5 = 6`. After this operation, `nums = [3,3,4,1,3,2,2,3]`.

	- We can perform the second operation as its score is `3 + 3 = 6`, the same as the previous operation. After this operation, `nums = [4,1,3,2,2,3]`.

	- We cannot perform the next operation as its score is `4 + 1 = 5`, which is different from the previous scores.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,3]</span>

**Output:** <span class="example-io">1</span>

</div>

**Constraints:**

	- `2 <= nums.length <= 100`

	- `1 <= nums[i] <= 1000`
