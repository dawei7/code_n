## Description

You are given an array of points on the **X-Y** plane `points` where `points[i] = [x_i, y_i]`. The points form a polygon when joined sequentially.

Return `true` if this polygon is <a href="http://en.wikipedia.org/wiki/Convex_polygon" target="_blank">convex</a> and `false` otherwise.

You may assume the polygon formed by given points is always a <a href="http://en.wikipedia.org/wiki/Simple_polygon" target="_blank">simple polygon</a>. In other words, we ensure that exactly two edges intersect at each vertex and that edges otherwise don't intersect each other.

**Example 1:**

![](images/covpoly1-plane.jpg)

```
**Input:** points = [[0,0],[0,5],[5,5],[5,0]]
**Output:** true
```

**Example 2:**

![](images/covpoly2-plane.jpg)

```
**Input:** points = [[0,0],[0,10],[10,10],[10,0],[5,5]]
**Output:** false
```

**Constraints:**

	- `3 <= points.length <= 10^4`

	- `points[i].length == 2`

	- `-10^4 <= x_i, y_i <= 10^4`

	- All the given points are **unique**.
