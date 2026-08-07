## Description

You are given an array `start` where `start = [startX, startY]` represents your initial position `(startX, startY)` in a 2D space. You are also given the array `target` where `target = [targetX, targetY]` represents your target position `(targetX, targetY)`.

The **cost** of going from a position `(x1, y1)` to any other position in the space `(x2, y2)` is `|x2 - x1| + |y2 - y1|`.

There are also some **special roads**. You are given a 2D array `specialRoads` where `specialRoads[i] = [x1_i, y1_i, x2_i, y2_i, cost_i]` indicates that the `i^th` special road goes in **one direction** from `(x1_i, y1_i)` to `(x2_i, y2_i)` with a cost equal to `cost_i`. You can use each special road any number of times.

Return the **minimum** cost required to go from `(startX, startY)` to `(targetX, targetY)`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

	- (1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1.

	- (1,2) to (3,3). Use `<span class="example-io">specialRoads[0]</span>`<span class="example-io"> with</span><span class="example-io"> the cost 2.</span>

	- <span class="example-io">(3,3) to (3,4) with a cost of |3 - 3| + |4 - 3| = 1.</span>

	- <span class="example-io">(3,4) to (4,5). Use </span>`<span class="example-io">specialRoads[1]</span>`<span class="example-io"> with the cost</span><span class="example-io"> 1.</span>

<span class="example-io">So the total cost is 1 + 2 + 1 + 1 = 5.</span>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">start = [3,2], target = [5,7], specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

It is optimal not to use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7.

Note that the <span class="example-io">`specialRoads[0]` is directed from (5,7) to (3,2).</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">start = [1,1], target = [10,4], specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

	- (1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1.

	- (1,2) to (7,4). Use `<span class="example-io">specialRoads[1]</span>`<span class="example-io"> with the cost</span><span class="example-io"> 4.</span>

	- (7,4) to (10,4) with a cost of |10 - 7| + |4 - 4| = 3.

</div>

**Constraints:**

	- `start.length == target.length == 2`

	- `1 <= startX <= targetX <= 10^5`

	- `1 <= startY <= targetY <= 10^5`

	- `1 <= specialRoads.length <= 200`

	- `specialRoads[i].length == 5`

	- `startX <= x1_i, x2_i <= targetX`

	- `startY <= y1_i, y2_i <= targetY`

	- `1 <= cost_i <= 10^5`
