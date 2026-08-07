## Description

There are `n` mountains in a row, and each mountain has a height. You are given an integer array `height` where `height[i]` represents the height of mountain `i`, and an integer `threshold`.

A mountain is called **stable** if the mountain just before it (**if it exists**) has a height **strictly greater** than `threshold`. **Note** that mountain 0 is **not** stable.

Return an array containing the indices of *all* **stable** mountains in **any** order.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">height = [1,2,3,4,5], threshold = 2</span>

**Output:** <span class="example-io">[3,4]</span>

**Explanation:**

	- Mountain 3 is stable because `height[2] == 3` is greater than `threshold == 2`.

	- Mountain 4 is stable because `height[3] == 4` is greater than `threshold == 2`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">height = [10,1,10,1,10], threshold = 3</span>

**Output:** <span class="example-io">[1,3]</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">height = [10,1,10,1,10], threshold = 10</span>

**Output:** <span class="example-io">[]</span>

</div>

**Constraints:**

	- `2 <= n == height.length <= 100`

	- `1 <= height[i] <= 100`

	- `1 <= threshold <= 100`
