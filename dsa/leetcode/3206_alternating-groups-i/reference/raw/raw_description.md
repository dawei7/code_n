## Description

There is a circle of red and blue tiles. You are given an array of integers `colors`. The color of tile `i` is represented by `colors[i]`:

	- `colors[i] == 0` means that tile `i` is **red**.

	- `colors[i] == 1` means that tile `i` is **blue**.

Every 3 contiguous tiles in the circle with **alternating** colors (the middle tile has a different color from its **left** and **right** tiles) is called an **alternating** group.

Return the number of **alternating** groups.

**Note** that since `colors` represents a **circle**, the **first** and the **last** tiles are considered to be next to each other.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">colors = [1,1,1]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

![](images/image_2024-05-16_23-53-171.png)

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">colors = [0,1,0,0,1]</span>

**Output:** 3

**Explanation:**

![](images/image_2024-05-16_23-47-491.png)

Alternating groups:

**

![](images/image_2024-05-16_23-50-441.png)

**

![](images/image_2024-05-16_23-48-211.png)

**

![](images/image_2024-05-16_23-49-351.png)

**

</div>

**Constraints:**

	- `3 <= colors.length <= 100`

	- `0 <= colors[i] <= 1`
