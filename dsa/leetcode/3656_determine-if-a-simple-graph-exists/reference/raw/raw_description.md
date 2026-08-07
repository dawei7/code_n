## Description

You are given an integer array `degrees`, where `degrees[i]` represents the desired degree of the `i^th` vertex.

Your task is to determine if there exists an **undirected simple** graph with **exactly** these vertex degrees.

A **simple** graph has no self-loops or parallel edges between the same pair of vertices.

Return `true` if such a graph exists, otherwise return `false`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">degrees = [3,1,2,2]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

![](images/screenshot-2025-08-13-at-24347-am.png)

​​​​​​​

One possible undirected simple graph is:

	- Edges: `(0, 1), (0, 2), (0, 3), (2, 3)`

	- Degrees: `deg(0) = 3`, `deg(1) = 1`, `deg(2) = 2`, `deg(3) = 2`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">degrees = [1,3,3,1]</span>

**Output:** <span class="example-io">false</span>

**Explanation:**​​​​​​​

	- `degrees[1] = 3` and `degrees[2] = 3` means they must be connected to all other vertices.

	- This requires `degrees[0]` and `degrees[3]` to be at least 2, but both are equal to 1, which contradicts the requirement.

	- Thus, the answer is `false`.

</div>

**Constraints:**

	- `1 <= n == degrees.length <= 10^​​​​​​​5`

	- `0 <= degrees[i] <= n - 1`
