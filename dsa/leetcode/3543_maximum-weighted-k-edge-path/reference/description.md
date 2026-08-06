## Description

You are given an integer `n` and a **Directed Acyclic Graph (DAG)** with `n` nodes labeled from 0 to `n - 1`. This is represented by a 2D array `edges`, where `edges[i] = [u_i, v_i, w_i]` indicates a directed edge from node `u_i` to `v_i` with weight `w_i`.

You are also given two integers, `k` and `t`.

Your task is to determine the **maximum** possible sum of edge weights for any path in the graph such that:

<ul>
	<li>The path contains **exactly** `k` edges.</li>
	<li>The total sum of edge weights in the path is **strictly** less than `t`.</li>
</ul>

Return the **maximum** possible sum of weights for such a path. If no such path exists, return `-1`.
