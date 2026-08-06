## Description

You are given a positive integer `n` representing the number of nodes in an **undirected** graph. The nodes are labeled from `1` to `n`.

You are also given a 2D integer array `edges`, where `edges[i] = [a_i, b_i]` indicates that there is a **bidirectional** edge between nodes `a_i` and `b_i`. **Notice** that the given graph may be disconnected.

Divide the nodes of the graph into `m` groups (**1-indexed**) such that:

<ul>
	<li>Each node in the graph belongs to exactly one group.</li>
	<li>For every pair of nodes in the graph that are connected by an edge `[a_i, b_i]`, if `a_i` belongs to the group with index `x`, and `b_i` belongs to the group with index `y`, then `|y - x| = 1`.</li>
</ul>

Return *the maximum number of groups (i.e., maximum *`m`*) into which you can divide the nodes*. Return `-1` *if it is impossible to group the nodes with the given conditions*.
