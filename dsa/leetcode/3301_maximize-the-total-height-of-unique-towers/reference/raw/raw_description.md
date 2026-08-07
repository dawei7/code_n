## Description

You are given an array `maximumHeight`, where `maximumHeight[i]` denotes the **maximum** height the `i^th` tower can be assigned.

Your task is to assign a height to each tower so that:

	- The height of the `i^th` tower is a positive integer and does not exceed `maximumHeight[i]`.

	- No two towers have the same height.

Return the **maximum** possible total sum of the tower heights. If it's not possible to assign heights, return `-1`.

**Example 1:**

<div class="example-block">
**Input:** maximumHeight<span class="example-io"> = [2,3,4,3]</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

We can assign heights in the following way: `[1, 2, 4, 3]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** maximumHeight<span class="example-io"> = [15,10]</span>

**Output:** <span class="example-io">25</span>

**Explanation:**

We can assign heights in the following way: `[15, 10]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** maximumHeight<span class="example-io"> = [2,2,1]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

It's impossible to assign positive heights to each index so that no two towers have the same height.

</div>

**Constraints:**

	- `1 <= maximumHeight.length <= 10^5`

	- `1 <= maximumHeight[i] <= 10^9`
