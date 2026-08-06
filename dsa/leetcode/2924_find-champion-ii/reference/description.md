## Description

There are `n` teams numbered from `0` to `n - 1` in a tournament; each team is also a node in a **DAG**.

You are given the integer `n` and a **0-indexed** 2D integer array `edges` of length `<font face="monospace">m</font>` representing the **DAG**, where `edges[i] = [u_i, v_i]` indicates that there is a directed edge from team `u_i` to team `v_i` in the graph.

A directed edge from `a` to `b` in the graph means that team `a` is **stronger** than team `b` and team `b` is **weaker** than team `a`.

Team `a` will be the **champion** of the tournament if there is no team `b` that is **stronger** than team `a`.

Return *the team that will be the **champion** of the tournament if there is a **unique** champion, otherwise, return *`-1`*.*

**Notes**

<ul>
	<li>A **cycle** is a series of nodes `a_1, a_2, ..., a_n, a_n+1` such that node `a_1` is the same node as node `a_n+1`, the nodes `a_1, a_2, ..., a_n` are distinct, and there is a directed edge from the node `a_i` to node `a_i+1` for every `i` in the range `[1, n]`.</li>
	<li>A **DAG** is a directed graph that does not have any **cycle**.</li>
</ul>
