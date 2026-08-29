## General

**Turn a cycle into an edge plus an alternate path**

Take any undirected edge $(u,v)$. If a cycle contains this edge, removing just that edge leaves a path from $u$ to $v$ through the rest of the cycle. Conversely, if $u$ and $v$ remain connected after their direct edge is removed, that alternate path together with edge $(u,v)$ forms a cycle.

This gives a precise way to measure the shortest cycle containing a chosen edge:

$$
1+\text{the shortest distance from }u\text{ to }v
\text{ when edge }(u,v)\text{ is unavailable}.
$$

The added one counts the removed edge itself. The exact solution evaluates this quantity for every input edge and keeps the minimum.

**Build an undirected adjacency structure**

The dictionary `g` maps each vertex to a set of its neighbors. For every input pair `u, v`, the code adds `v` to `g[u]` and `u` to `g[v]`. Both insertions are necessary because the graph is bi-directional.

Sets make the adjacency representation insensitive to repeated insertion, although the contract already guarantees that no edge is repeated. Vertices with no incident edge simply have no stored neighbors, which is harmless because no cycle can use such a vertex.

**One breadth-first search per edge**

The helper `bfs(u, v)` temporarily treats edge $(u,v)$ as deleted without modifying `g`. It creates a distance array filled with infinity, sets `dist[u] = 0`, and explores outward from $u$ using a FIFO queue.

When examining adjacency step $(i,j)$, the condition

`(i, j) != (u, v) and (j, i) != (u, v)`

rejects both orientations of the selected undirected edge. This two-sided check is essential: the adjacency structure stores the edge in both directions, so skipping only $u\to v$ would still leave $v\to u$ available.

An undiscovered neighbor receives distance `dist[i] + 1` and enters the queue. Because breadth-first search visits an unweighted graph layer by layer, the first assigned distance to every vertex is its shortest number of allowed edges from $u$.

After exploration, the helper returns `dist[v] + 1`. A finite result is the length of the shortest cycle that uses the removed edge. If $v$ is unreachable, `dist[v]` remains infinity, and adding one leaves it infinite.

**Why examining every edge finds the global shortest cycle**

Let $C$ be a globally shortest cycle, and choose any edge $(u,v)$ on it. Removing that edge from $C$ leaves a $u$-to-$v$ path of length $|C|-1$. Therefore, the breadth-first search performed for $(u,v)$ finds an alternate path of length at most $|C|-1$, producing a cycle candidate of length at most $|C|$.

Every finite candidate produced by the algorithm is also a genuine cycle: its breadth-first-search path does not use $(u,v)$, and adding that edge closes the path. Since $C$ was globally shortest, no genuine candidate can have length below $|C|$. The candidate for the chosen edge is consequently exactly $|C|$, and taking the minimum over all edges returns the correct answer.

This proof also explains why it is enough to remove one edge at a time. There is no need to guess all vertices of a cycle; every cycle exposes itself as an alternate route between the endpoints of each of its edges.

**What happens in an acyclic component**

In a tree, deleting any edge separates its endpoints into different components. The corresponding breadth-first search cannot reach `v`, so it returns infinity. The same holds for every bridge, even when that bridge belongs to a larger graph containing cycles elsewhere.

The outer expression computes the minimum helper result across all edges. If every result is infinite, the graph has no cycle and the final conditional returns `-1`. Otherwise, it returns the smallest finite cycle length.

**A concrete trace**

For triangle edges `[0,1]`, `[1,2]`, and `[2,0]`, consider removing $(0,1)$. Breadth-first search travels $0\to2\to1$, a distance of two. Adding the removed edge gives length three.

For a square, removing one side leaves a three-edge route around the other sides, producing length four. If the graph contains both a triangle and a square, searches for triangle edges produce three while searches for square edges may produce four; the outer minimum correctly selects three.

**Relationship to the manifest summary**

The stored implementation runs a breadth-first search for each edge and obtains a cycle by deleting that edge. This differs in mechanics from the common parent-aware method that starts BFS from each vertex and recognizes non-tree edges, but both rely on shortest unweighted paths. The explanation here follows the exact solution file so that every line and complexity claim can be traced to the code that actually runs.

## Complexity detail

Let $n$ be the number of vertices and $m$ the number of edges. Building the adjacency sets takes expected $O(m)$ time and $O(n+m)$ space when the distance array is included.

There are $m$ calls to `bfs`. Each call allocates and initializes an $n$-entry distance array, and in the worst case scans every vertex and both stored directions of every edge. One call therefore costs $O(n+m)$ time, and the exact total is

$$
O\bigl(m(n+m)\bigr).
$$

The manifest records $O(n(n+m))$, which describes the alternative “BFS from every vertex” formulation, not the per-edge loop in this exact source. For the implementation shown here, $m$ is the multiplier that accurately counts searches.

At any moment, the graph occupies $O(n+m)$ space, while `dist` and the queue use $O(n)$ additional space. Searches run sequentially, so their arrays do not accumulate. Total auxiliary space is $O(n+m)$.

## Alternatives and edge cases

- **BFS from every vertex:** Track distances and parents, and use an already-visited neighbor that is not the parent to form a cycle. This can achieve $O(n(n+m))$ time and matches the manifest summary, but its cycle-length formula and parent handling require care.
- **Floyd–Warshall:** All-pairs dynamic programming can be adapted to cycle detection in $O(n^3)$ time and $O(n^2)$ space, which is unnecessary for this sparse constraint range.
- **Depth-first search alone:** DFS detects whether a cycle exists, but ordinary DFS depth does not guarantee the shortest cycle length.
- **Disconnected graph:** Each search naturally remains within its component; the minimum can come from any component.
- **Tree or forest:** Removing every edge disconnects its endpoints, so all candidates remain infinite and the result is `-1`.
- **Bridge next to a cycle:** Searches for bridge edges fail, while edges on the cyclic part still produce finite candidates.
- **Triangle:** Three is the smallest possible cycle because self-loops and repeated parallel edges are forbidden.
- **Multiple shortest cycles:** The outer minimum needs only their common length and does not need to reconstruct a particular cycle.
- **Undirected deletion:** Both ordered forms of the selected edge must be skipped during BFS.
- **Infinity arithmetic:** In Python, `inf + 1` is still `inf`, so unreachable endpoints flow safely into the final minimum and conditional.
