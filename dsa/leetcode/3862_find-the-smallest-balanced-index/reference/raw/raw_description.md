## Description

You are given an integer array `nums`.

An index `i` is **balanced** if the sum of elements **strictly** to the left of `i` equals the product of elements **strictly** to the right of `i`.

If there are no elements to the left, the sum is considered as 0. Similarly, if there are no elements to the right, the product is considered as 1.

Return an integer denoting the **smallest** balanced index. If no balanced index exists, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1,2]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

For index `i = 1`:

	- Left sum = `nums[0] = 2`

	- Right product = `nums[2] = 2`

	- Since the left sum equals the right product, index 1 is balanced.

No smaller index satisfies the condition, so the answer is 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,8,2,2,5]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

For index `i = 2`:

	- Left sum = `2 + 8 = 10`

	- Right product = `2 * 5 = 10`

	- Since the left sum equals the right product, index 2 is balanced.

No smaller index satisfies the condition, so the answer is 2.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1]</span>

**Output:** <span class="example-io">-1</span>

For index `i = 0`:

	- The left side is empty, so the left sum is 0.

	- The right side is empty, so the right product is 1.

	- Since the left sum does not equal the right product, index 0 is not balanced.

Therefore, no balanced index exists and the answer is -1.</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`
