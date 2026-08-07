## Description

You are given an **undirected tree** with `n` nodes, numbered from 0 to `n - 1`. It is represented by a 2D integer array `edges`​​​​​​​ of length `n - 1`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

You are also given two **binary** strings `start` and `target` of length `n`. For each node `x`, `start[x]` is its initial color and `target[x]` is its desired color.

In one operation, you may pick an edge with index `i` and **toggle **both of its endpoints. That is, if the edge is `[u, v]`, then the colors of nodes `u` and `v` **each** flip from `'0'` to `'1'` or from `'1'` to `'0'`.

Return an array of edge indices whose operations transform `start` into `target`. Among all valid sequences with **minimum possible length**, return the edge indices in **increasing**​​​​​​​ order.

If it is impossible to transform `start` into `target`, return an array containing a single element equal to -1.

**Example 1:**

**

![](images/example1.png)

​​​​​​​**

<div class="example-block">
**Input:** <span class="example-io">n = 3, edges = [[0,1],[1,2]], start = "010", target = "100"</span>

**Output:** <span class="example-io">[0]</span>

**Explanation:**

Toggle edge with index 0, which flips nodes 0 and 1.

​​​​​​​The string changes from `"010"` to `"100"`, matching the target.

</div>

**Example 2:**

**

![](images/example2.png)

**

<div class="example-block">
**Input:** <span class="example-io">n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[3,5],[1,6]], start = "0011000", target = "0010001"</span>

**Output:** <span class="example-io">[1,2,5]</span>

**Explanation:**

	- Toggle edge with index 1, which flips nodes 1 and 2.

	- Toggle edge with index 2, which flips nodes 2 and 3.

	- Toggle edge with index 5, which flips nodes 1 and 6.

After these operations, the resulting string becomes `"0010001"`, which matches the target.

</div>

**Example 3:**

**

![](images/example3.png)

​​​​​​​**

<div class="example-block">
**Input:** <span class="example-io">n = 2, edges = [[0,1]], start = "00", target = "01"</span>

**Output:** <span class="example-io">[-1]</span>

**Explanation:**

There is no sequence of edge toggles that transforms `"00"` into `"01"`. Therefore, we return `[-1]`.

</div>

**Constraints:**

	- `2 <= n == start.length == target.length <= 10^5`

	- `edges.length == n - 1`

	- `edges[i] = [a_i, b_i]`

	- `0 <= a_i, b_i < n`

	- `start[i]` is either `'0'` or `'1'`.

	- `target[i]` is either `'0'` or `'1'`.

	- The input is generated such that `edges` represents a valid tree.
