## Description

There is a **directed weighted** graph that consists of `n` nodes numbered from `0` to `n - 1`. The edges of the graph are initially represented by the given array `edges` where `edges[i] = [from_i, to_i, edgeCost_i]` meaning that there is an edge from `from_i` to `to_i` with the cost `edgeCost_i`.

Implement the `Graph` class:

<ul>
	<li>`Graph(int n, int[][] edges)` initializes the object with `n` nodes and the given edges.</li>
	<li>`addEdge(int[] edge)` adds an edge to the list of edges where `edge = [from, to, edgeCost]`. It is guaranteed that there is no edge between the two nodes before adding this one.</li>
	<li>`int shortestPath(int node1, int node2)` returns the **minimum** cost of a path from `node1` to `node2`. If no path exists, return `-1`. The cost of a path is the sum of the costs of the edges in the path.</li>
</ul>
