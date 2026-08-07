## Description

You are given an integer `n` representing the dimensions of an `n x n`<!-- notionvc: fa9fe4ed-dff8-4410-8196-346f2d430795 --> grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates `rectangles`, where `rectangles[i]` is in the form `[start_x, start_y, end_x, end_y]`, representing a rectangle on the grid. Each rectangle is defined as follows:

	- `(start_x, start_y)`: The bottom-left corner of the rectangle.

	- `(end_x, end_y)`: The top-right corner of the rectangle.

**Note **that the rectangles do not overlap. Your task is to determine if it is possible to make **either two horizontal or two vertical cuts** on the grid such that:

	- Each of the three resulting sections formed by the cuts contains **at least** one rectangle.

	- Every rectangle belongs to **exactly** one section.

Return `true` if such cuts can be made; otherwise, return `false`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

![](images/tt1drawio.png)

The grid is shown in the diagram. We can make horizontal cuts at `y = 2` and `y = 4`. Hence, output is true.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

![](images/tc2drawio.png)

We can make vertical cuts at `x = 2` and `x = 3`. Hence, output is true.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.

</div>

**Constraints:**

	- `3 <= n <= 10^9`

	- `3 <= rectangles.length <= 10^5`

	- `0 <= rectangles[i][0] < rectangles[i][2] <= n`

	- `0 <= rectangles[i][1] < rectangles[i][3] <= n`

	- No two rectangles overlap.
