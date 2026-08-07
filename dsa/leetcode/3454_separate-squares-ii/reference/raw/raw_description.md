## Description

You are given a 2D integer array `squares`. Each `squares[i] = [x_i, y_i, l_i]` represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the **minimum** y-coordinate value of a horizontal line such that the total area covered by squares above the line *equals* the total area covered by squares below the line.

Answers within `10^-5` of the actual answer will be accepted.

**Note**: Squares **may** overlap. Overlapping areas should be counted **only once** in this version.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">squares = [[0,0,1],[2,2,1]]</span>

**Output:** <span class="example-io">1.00000</span>

**Explanation:**

![](images/4065example1drawio.png)

Any horizontal line between `y = 1` and `y = 2` results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">squares = [[0,0,2],[1,1,1]]</span>

**Output:** <span class="example-io">1.00000</span>

**Explanation:**

![](images/4065example2drawio.png)

Since the blue square overlaps with the red square, it will not be counted again. Thus, the line `y = 1` splits the squares into two equal parts.

</div>

**Constraints:**

	- `1 <= squares.length <= 5 * 10^4`

	- `squares[i] = [x_i, y_i, l_i]`

	- `squares[i].length == 3`

	- `0 <= x_i, y_i <= 10^9`

	- `1 <= l_i <= 10^9`

	- The total area of all the squares will not exceed `10^15`.
