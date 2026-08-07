## Description

You are given an integer array `nums`.

In one operation, you can choose any two **distinct** indices `i` and `j` and swap `nums[i]` and `nums[j]`.

Return an integer denoting the **minimum** number of operations required to move all 0s to the end of the array.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,1,0,3,12]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

We perform the following swap operations:

	- Swap `nums[0]` and `nums[3]`, giving `nums = [3, 1, 0, 0, 12]`.

	- Swap `nums[2]` and `nums[4]`, giving `nums = [3, 1, 12, 0, 0]`.

Thus, the answer is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,1,0,2]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

We perform the following swap operations:

	- Swap `nums[0]` and `nums[3]`, giving `nums = [2, 1, 0, 0]`.

Thus, the answer is 1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,0]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The array already satisfies the condition. Therefore, no swap operations are needed.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 100`
