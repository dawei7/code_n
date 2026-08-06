## Description

There exists an **undirected** tree with `n` nodes numbered `0` to `n - 1`. You are given a **0-indexed** 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates that there is an edge between nodes `u_i` and `v_i` in the tree. You are also given a **positive** integer `k`, and a **0-indexed** array of **non-negative** integers `nums` of length `n`, where `nums[i]` represents the **value** of the node numbered `i`.

Alice wants the sum of values of tree nodes to be **maximum**, for which Alice can perform the following operation **any** number of times (**including zero**) on the tree:

<ul>
	<li>Choose any edge `[u, v]` connecting the nodes `u` and `v`, and update their values as follows:

	<ul>
		<li>`nums[u] = nums[u] XOR k`</li>
		<li>`nums[v] = nums[v] XOR k`</li>
	</ul>
	</li>
</ul>

Return *the **maximum** possible **sum** of the **values** Alice can achieve by performing the operation **any** number of times*.
