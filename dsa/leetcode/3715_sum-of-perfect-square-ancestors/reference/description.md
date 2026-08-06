## Description

You are given an integer `n` and an undirected tree rooted at node 0 with `n` nodes numbered from 0 to `n - 1`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates an undirected edge between nodes `u_i` and `v_i`.

You are also given an integer array `nums`, where `nums[i]` is the positive integer assigned to node `i`.

Define a value `t_i` as the number of **ancestors** of node `i` such that the product `nums[i] * nums[ancestor]` is a **<span data-keyword="perfect-square">perfect square</span>**.

Return the sum of all `t_i` values for all nodes `i` in range `[1, n - 1]`.

**Note**:

<ul>
	<li>In a rooted tree, the **ancestors** of node `i` are all nodes on the path from node `i` to the root node 0, **excluding** `i` itself.</li>
</ul>
