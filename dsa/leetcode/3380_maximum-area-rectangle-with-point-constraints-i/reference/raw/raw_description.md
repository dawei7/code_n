## Description

You are given an array `points` where `points[i] = [x_i, y_i]` represents the coordinates of a point on an infinite plane.

Your task is to find the **maximum **area of a rectangle that:

	- Can be formed using **four** of these points as its corners.

	- Does **not** contain any other point inside or on its border.

	- Has its edges **parallel** to the axes.

Return the **maximum area** that you can obtain or -1 if no such rectangle is possible.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">points = [[1,1],[1,3],[3,1],[3,3]]</span>

**Output: **4

**Explanation:**

**

![Example 1 diagram](images/3380_ex0.png)

**

We can make a rectangle with these 4 points as corners and there is no other point that lies inside or on the border<!-- notionvc: f270d0a3-a596-4ed6-9997-2c7416b2b4ee -->. Hence, the maximum possible area would be 4.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">points = [[1,1],[1,3],[3,1],[3,3],[2,2]]</span>

**Output:**** **-1

**Explanation:**

**

![Example 2 diagram](images/3380_ex1.png)

**

There is only one rectangle possible is with points `[1,1], [1,3], [3,1]` and `[3,3]` but `[2,2]` will always lie inside it. Hence, returning -1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]</span>

**Output: **2

**Explanation:**

**

![Example 3 diagram](images/3380_ex2.png)

**

The maximum area rectangle is formed by the points `[1,3], [1,2], [3,2], [3,3]`, which has an area of 2. Additionally, the points `[1,1], [1,2], [3,1], [3,2]` also form a valid rectangle with the same area.

</div>

**Constraints:**

	- `1 <= points.length <= 10`

	- `points[i].length == 2`

	- `0 <= x_i, y_i <= 100`

	- All the given points are **unique**.
