## Description

You are given a string `road`, consisting only of characters `"x"` and `"."`, where each `"x"` denotes a *pothole* and each `"."` denotes a smooth road, and an integer `budget`.

In one repair operation, you can repair `n` **consecutive** potholes for a price of `n + 1`.

Return the **maximum** number of potholes that can be fixed such that the sum of the prices of all of the fixes **doesn't go over** the given budget.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">road = "..", budget = 5</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

There are no potholes to be fixed.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">road = "..xxxxx", budget = 4</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

We fix the first three potholes (they are consecutive). The budget needed for this task is `3 + 1 = 4`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">road = "x.x.xxx...x", budget = 14</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

We can fix all the potholes. The total cost would be `(1 + 1) + (1 + 1) + (3 + 1) + (1 + 1) = 10` which is within our budget of 14.

</div>

**Constraints:**

	- `1 <= road.length <= 10^5`

	- `1 <= budget <= 10^5 + 1`

	- `road` consists only of characters `'.'` and `'x'`.
