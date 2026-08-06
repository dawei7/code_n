## Description

You are given two integers, `n` and `threshold`, as well as a **directed** weighted graph of `n` nodes numbered from 0 to `n - 1`. The graph is represented by a **2D** integer array `edges`, where `edges[i] = [A_i, B_i, W_i]` indicates that there is an edge going from node `A_i` to node `B_i` with weight `W_i`.

You have to remove some edges from this graph (possibly **none**), so that it satisfies the following conditions:

<ul>
	<li>Node 0 must be reachable from all other nodes.</li>
	<li>The **maximum** edge weight in the resulting graph is **minimized**.</li>
	<li>Each node has **at most** `threshold` outgoing edges.</li>
</ul>

Return the **minimum** possible value of the **maximum** edge weight after removing the necessary edges. If it is impossible for all conditions to be satisfied, return -1.
