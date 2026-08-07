## Description

You are given an **undirected weighted** tree with `n` nodes, numbered from `0` to `n - 1`. It is represented by a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i, w_i]` indicates that there is an edge between nodes `u_i` and `v_i` with weight `w_i`.​

Additionally, you are given a 2D integer array `queries`, where `queries[j] = [src1_j, src2_j, dest_j]`.

Return an array `answer` of length equal to `queries.length`, where `answer[j]` is the **minimum total weight** of a subtree such that it is possible to reach `dest_j` from both `src1_j` and `src2_j` using edges in this subtree.

A **subtree** here is any connected subset of nodes and edges of the original tree forming a valid tree.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], queries = [[2,3,4],[0,2,5]]</span>

**Output:** <span class="example-io">[12,11]</span>

**Explanation:**

The blue edges represent one of the subtrees that yield the optimal answer.

![](images/tree1-4.jpg)

	- `answer[0]`: The total weight of the selected subtree that ensures a path from `src1 = 2` and `src2 = 3` to `dest = 4` is `3 + 5 + 4 = 12`.

	- `answer[1]`: The total weight of the selected subtree that ensures a path from `src1 = 0` and `src2 = 2` to `dest = 5` is `2 + 3 + 6 = 11`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">edges = [[1,0,8],[0,2,7]], queries = [[0,1,2]]</span>

**Output:** <span class="example-io">[15]</span>

**Explanation:**

![](images/tree1-5.jpg)

	- `answer[0]`: The total weight of the selected subtree that ensures a path from `src1 = 0` and `src2 = 1` to `dest = 2` is `8 + 7 = 15`.

</div>

**Constraints:**

	- `3 <= n <= 10^5`

	- `edges.length == n - 1`

	- `edges[i].length == 3`

	- `0 <= u_i, v_i < n`

	- `1 <= w_i <= 10^4`

	- `1 <= queries.length <= 10^5`

	- `queries[j].length == 3`

	- `0 <= src1_j, src2_j, dest_j < n`

	- `src1_j`, `src2_j`, and `dest_j` are pairwise distinct.

	- The input is generated such that `edges` represents a valid tree.
