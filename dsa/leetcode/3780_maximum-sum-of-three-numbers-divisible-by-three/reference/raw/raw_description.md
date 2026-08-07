## Description

You are given an integer array `nums`.

Your task is to choose **exactly three** integers from `nums` such that their sum is divisible by three.

Return the **maximum** possible sum of such a triplet. If no such triplet exists, return 0.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,2,3,1]</span>

**Output:** <span class="example-io">9</span>

**Explanation:**

The valid triplets whose sum is divisible by 3 are:

	- `(4, 2, 3)` with a sum of `4 + 2 + 3 = 9`.

	- `(2, 3, 1)` with a sum of `2 + 3 + 1 = 6`.

Thus, the answer is 9.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1,5]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

No triplet forms a sum divisible by 3, so the answer is 0.

</div>

**Constraints:**

	- `3 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
