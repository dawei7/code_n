## Description

There is a circle of red and blue tiles. You are given an array of integers `colors` and an integer `k`. The color of tile `i` is represented by `colors[i]`:

	- `colors[i] == 0` means that tile `i` is **red**.

	- `colors[i] == 1` means that tile `i` is **blue**.

An **alternating** group is every `k` contiguous tiles in the circle with **alternating** colors (each tile in the group except the first and last one has a different color from its **left** and **right** tiles).

Return the number of **alternating** groups.

**Note** that since `colors` represents a **circle**, the **first** and the **last** tiles are considered to be next to each other.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">colors = [0,1,0,1,0], k = 3</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

**

![](images/screenshot-2024-05-28-183519.png)

**

Alternating groups:

![](images/screenshot-2024-05-28-182448.png)

![](images/screenshot-2024-05-28-182844.png)

![](images/screenshot-2024-05-28-183057.png)

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">colors = [0,1,0,0,1,0,1], k = 6</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

**

![](images/screenshot-2024-05-28-183907.png)

**

Alternating groups:

![](images/screenshot-2024-05-28-184128.png)

![](images/screenshot-2024-05-28-184240.png)

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">colors = [1,1,0,1], k = 4</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

![](images/screenshot-2024-05-28-184516.png)

</div>

**Constraints:**

	- `3 <= colors.length <= 10^5`

	- `0 <= colors[i] <= 1`

	- `3 <= k <= colors.length`
