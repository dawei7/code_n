## Description

You are given a **directed** weighted graph with `n` nodes labeled from 0 to `n - 1`.

The graph is represented by a 2D integer array `edges`, where `edges[i] = [u_i, v_i, t_i]` indicates a directed edge from node `u_i` to node `v_i` that takes `t_i` seconds to traverse.

You are also given an integer `power` representing the initial available power, and an integer array `cost` of length `n`, where `cost[u]` represents the power required to forward the signal from node `u` through **any** one of its outgoing edges.

You are given two integers `source` and `target`.

The signal starts at `source` at time 0 with `power` units of power and follows these rules:

<ul>
	<li>The signal may traverse a directed edge from node `u` only if the remaining power is **at least** `cost[u]`.</li>
	<li>No power is consumed when the signal arrives at a node, unless it later leaves that node by traversing another edge.</li>
	<li>When the signal is forwarded from node `u`, the remaining power is **decreased** by `cost[u]` units.</li>
	<li>Traversing an edge `edges[i] = [u_i, v_i, t_i]` **increases** the total time by `t_i` seconds.</li>
</ul>

Return an integer array `answer` of size 2, where:

<ul>
	<li>`answer[0]` is the **minimum** time required for the signal to reach node `target`.</li>
	<li>`answer[1]` is the **maximum** remaining power among all paths that achieve `answer[0]`.</li>
</ul>

If the signal cannot reach `target`, return `[-1, -1]`.
