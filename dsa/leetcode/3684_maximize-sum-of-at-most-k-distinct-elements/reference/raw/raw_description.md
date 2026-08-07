## Description

You are given a **positive** integer array `nums` and an integer `k`.

Choose at most `k` elements from `nums` so that their sum is maximized. However, the chosen numbers must be **distinct**.

Return an array containing the chosen numbers in **strictly descending** order.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [84,93,100,77,90], k = 3</span>

**Output:** <span class="example-io">[100,93,90]</span>

**Explanation:**

The maximum sum is 283, which is attained by choosing 93, 100 and 90. We rearrange them in strictly descending order as `[100, 93, 90]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [84,93,100,77,93], k = 3</span>

**Output:** <span class="example-io">[100,93,84]</span>

**Explanation:**

The maximum sum is 277, which is attained by choosing 84, 93 and 100. We rearrange them in strictly descending order as `[100, 93, <span class="example-io">84</span>]`. We cannot choose 93, 100 and 93 because the chosen numbers must be distinct.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1,2,2,2], k = 6</span>

**Output:** <span class="example-io">[2,1]</span>

**Explanation:**

The maximum sum is 3, which is attained by choosing 1 and 2. We rearrange them in strictly descending order as `[2, 1]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 10^9`

	- `1 <= k <= nums.length`
