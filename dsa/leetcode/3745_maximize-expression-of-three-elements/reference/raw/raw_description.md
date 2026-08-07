## Description

You are given an integer array `nums`.

Choose three elements `a`, `b`, and `c` from `nums` at **distinct** indices such that the value of the expression `a + b - c` is maximized.

Return an integer denoting the **maximum possible value** of this expression.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,4,2,5]</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

We can choose `a = 4`, `b = 5`, and `c = 1`. The expression value is `4 + 5 - 1 = 8`, which is the maximum possible.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-2,0,5,-2,4]</span>

**Output:** <span class="example-io">11</span>

**Explanation:**

We can choose `a = 5`, `b = 4`, and `c = -2`. The expression value is `5 + 4 - (-2) = 11`, which is the maximum possible.

</div>

**Constraints:**

	- `3 <= nums.length <= 100`

	- `-100 <= nums[i] <= 100`
