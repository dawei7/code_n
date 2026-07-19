## General
**Grow a minimum spanning tree with Prim's rule**

Treat every point as a vertex of the complete graph whose edge weights are Manhattan distances. Maintain `best_distance[i]`, the cheapest edge currently known from the growing tree to point `i`. Start with one point at distance zero.

At each step, select the unvisited point with the smallest `best_distance`, add that cost to the answer, and mark the point as part of the tree. Then compute its distance to every unvisited point and lower those points' best distances when this new edge is cheaper.

**Why each selected edge is safe**

Before a point is added, the visited and unvisited vertices form a cut. The selected `best_distance` is the lightest edge crossing that cut. By the minimum-spanning-tree cut property, some optimal spanning tree contains that edge, so adding it never prevents an optimal result.

Each iteration adds one new vertex and one connecting edge except for the zero-cost starting vertex. After $N$ iterations, all vertices are connected with $N-1$ edges and the accumulated cost is minimum.

## Complexity detail
Selecting the next point scans up to $N$ distances, and updating distances scans up to $N$ points. Repeating for all $N$ vertices gives $O(N^2)$ time.

The visited flags and best-distance array use $O(N)$ auxiliary space.

## Alternatives and edge cases
- **Kruskal's algorithm:** materialize all $O(N^2)$ edges, sort them, and join components. It is correct but uses $O(N^2)$ space and $O(N^2\log N)$ time.
- **Repeated full cut scan:** search every visited-to-unvisited edge from scratch at each step. It implements Prim correctly but takes $O(N^3)$ time.
- **Heap-based Prim:** push candidate edges into a priority queue. On the dense complete graph it can retain quadratic edges and adds logarithmic overhead.
- **Single point:** no edge is required, so the cost is zero.
- **Two points:** the answer is their Manhattan distance.
- **Collinear points:** connecting neighboring coordinates in order often realizes the optimum.
- **Negative coordinates:** absolute differences handle them without special cases.
- **Large coordinates:** the total may exceed individual coordinate bounds, so fixed-width implementations need adequate integer range.
- **Several equal edge weights:** any safe minimum crossing edge may be chosen.
