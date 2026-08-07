## Description

You are given an `m x n` 2D array `grid` of **positive** integers.

Your task is to traverse `grid` in a **zigzag** pattern while skipping every **alternate** cell.

Zigzag pattern traversal is defined as following the below actions:

	- Start at the top-left cell `(0, 0)`.

	- Move *right* within a row until the end of the row is reached.

	- Drop down to the next row, then traverse *left* until the beginning of the row is reached.

	- Continue **alternating** between right and left traversal until every row has been traversed.

**Note **that you **must skip** every *alternate* cell during the traversal.

Return an array of integers `result` containing, **in order**, the value of the cells visited during the zigzag traversal with skips.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1,2],[3,4]]</span>

**Output:** <span class="example-io">[1,4]</span>

**Explanation:**

**

![](images/4012_example0.png)

**

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[2,1],[2,1],[2,1]]</span>

**Output:** <span class="example-io">[2,1,2]</span>

**Explanation:**

![](images/4012_example1.png)

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1,2,3],[4,5,6],[7,8,9]]</span>

**Output:** <span class="example-io">[1,3,5,7,9]</span>

**Explanation:**

![](images/4012_example2.png)

</div>

**Constraints:**

	- `2 <= n == grid.length <= 50`

	- `2 <= m == grid[i].length <= 50`

	- `1 <= grid[i][j] <= 2500`
