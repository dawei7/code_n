### 1. Description

You are given an array `points` where $\text{points}[i] = [x_{i}, y_{i}]$ represents the coordinates of a point on an infinite plane.

Your task is to find the **maximum **area of a rectangle that:

- Can be formed using **four** of these points as its corners.

- Does **not** contain any other point inside or on its border.

- Has its edges **parallel** to the axes.

Return the **maximum area** that you can obtain or -1 if no such rectangle is possible.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** points = [[1,1],[1,3],[3,1],[3,3]]

**Output: **4

**Explanation:**

**

![Example 1 diagram](images/3380_ex0.png)

**

We can make a rectangle with these 4 points as corners and there is no other point that lies inside or on the border<!-- notionvc: f270d0a3-a596-4ed6-9997-2c7416b2b4ee -->. Hence, the maximum possible area would be 4.

</div>
#### Example 2

<div class="example-block">
**Input:** points = [[1,1],[1,3],[3,1],[3,3],[2,2]]

**Output:**** **-1

**Explanation:**

**

![Example 2 diagram](images/3380_ex1.png)

**

There is only one rectangle possible is with points `[1,1], [1,3], [3,1]` and `[3,3]` but `[2,2]` will always lie inside it. Hence, returning -1.

</div>
#### Example 3

<div class="example-block">
**Input:** points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]

**Output: **2

**Explanation:**

**

![Example 3 diagram](images/3380_ex2.png)

**

The maximum area rectangle is formed by the points `[1,3], [1,2], [3,2], [3,3]`, which has an area of 2. Additionally, the points `[1,1], [1,2], [3,1], [3,2]` also form a valid rectangle with the same area.

</div>

### 4. Constraints

- $1 \le \text{points.length} \le 10$

- $\text{points}[i].length = 2$

- $0 \le x_{i}, y_{i} \le 100$

- All the given points are **unique**.