## Description

You are given an integer `n`, representing `n` nodes numbered from 0 to `n - 1` and a list of `edges`, where `edges[i] = [u_i, v_i, s_i, must_i]`:

<ul>
	<li>`u_i` and `v_i` indicates an undirected edge between nodes `u_i` and `v_i`.</li>
	<li>`s_i` is the strength of the edge.</li>
	<li>`must_i` is an integer (0 or 1). If `must_i == 1`, the edge **must** be included in the** ****spanning tree**. These edges **cannot** be **upgraded**.</li>
</ul>

You are also given an integer `k`, the **maximum** number of upgrades you can perform. Each upgrade **doubles** the strength of an edge, and each eligible edge (with `must_i == 0`) can be upgraded **at most** once.

The **stability** of a spanning tree is defined as the **minimum** strength score among all edges included in it.

Return the **maximum** possible stability of any valid spanning tree. If it is impossible to connect all nodes, return `-1`.

**Note**: A **spanning tree** of a graph with `n` nodes is a subset of the edges that connects all nodes together (i.e. the graph is **connected**) *without* forming any cycles, and uses **exactly** `n - 1` edges.
