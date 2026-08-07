## Description

You are given an **undirected tree** with `n` nodes, numbered from 0 to `n - 1`. It is represented by a 2D integer array `edges`​​​​​​​ of length `n - 1`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

A node is called **special** if it is an **endpoint** of any** diameter path** of the tree.

Return a binary string `s` of length `n`, where `s[i] = '1'` if node `i` is special, and `s[i] = '0'` otherwise.

A **diameter path** of a tree is the **longest** simple path between any two nodes. A tree may have multiple diameter paths.

An **endpoint** of a path is the **first** or **last** node on that path.

**Example 1:**

**

![](images/pic1.png)

**

<div class="example-block">
**Input:** <span class="example-io">n = 3, edges = [[0,1],[1,2]]</span>

**Output:** <span class="example-io">"101"</span>

**Explanation:**

	- The diameter of this tree consists of 2 edges.

	- The only diameter path is the path from node 0 to node 2

	- The endpoints of this path are nodes 0 and 2, so they are special.

</div>

**Example 2:**

**

![](images/pic2.png)

**

<div class="example-block">
**Input:** <span class="example-io">n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[3,5],[1,6]]</span>

**Output:** <span class="example-io">"1000111"</span>

**Explanation:**

The diameter of this tree consists of 4 edges. There are 4 diameter paths:

	- The path from node 0 to node 4

	- The path from node 0 to node 5

	- The path from node 6 to node 4

	- The path from node 6 to node 5

The special nodes are nodes `0, 4, 5, 6`, as they are endpoints in at least one diameter path.

</div>

**Example 3:**

**

![](images/pic3.png)

​​​​​​​**

<div class="example-block">
**Input:** <span class="example-io">n = 2, edges = [[0,1]]</span>

**Output:** <span class="example-io">"11"</span>

**Explanation:**

	- The diameter of this tree consists of 1 edge.

	- The only diameter path is the path from node 0 to node 1

	- The endpoints of this path are nodes 0 and 1, so they are special.

</div>

**Constraints:**

	- `2 <= n <= 10^5`

	- `edges.length == n - 1`

	- `edges[i] = [a_i, b_i]`

	- `0 <= a_i, b_i < n`

	- The input is generated such that `edges` represents a valid tree.
