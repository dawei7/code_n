## Description

You are given an integer array `nums` of length `n`.

Your goal is to start at index `0` and reach index `n - 1`. You can only jump to indices **greater** than your current index.

The score for a jump from index `i` to index `j` is calculated as `(j - i) * nums[i]`.

Return the **maximum** possible **total score** by the time you reach the last index.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,1,5]</span>

**Output:** 7

**Explanation:**

First, jump to index 1 and then jump to the last index. The final score is `1 * 1 + 2 * 3 = 7`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,3,1,3,2]</span>

**Output:** 16

**Explanation:**

Jump directly to the last index. The final score is `4 * 4 = 16`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
