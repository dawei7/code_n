## Description

Implement `DistanceLimitedPathsExist` for an undirected weighted graph with nodes labeled from $0$ through $n-1$. Each entry `[u, v, distance]` in `edgeList` adds an edge of that weight; parallel edges may occur, and the graph need not be connected.

After construction, `query(p, q, limit)` must report whether some path connects `p` and `q` using only edges whose individual weights are strictly less than `limit`. Queries arrive online and do not modify the graph.
