# Min Cost to Connect All Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1584 |
| Difficulty | Medium |
| Topics | Array, Union-Find, Graph Theory, Minimum Spanning Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/min-cost-to-connect-all-points/) |

## Problem Description
### Goal

Given distinct points on a two-dimensional plane, connecting points $i$ and $j$ costs their Manhattan distance:

$$
\lvert x_i-x_j\rvert+\lvert y_i-y_j\rvert.
$$

Choose connections so that every point is reachable from every other point and there is exactly one simple path between each pair. Thus, the chosen connections form a spanning tree over the points.

Return the minimum possible sum of connection costs. Any pair of points may be connected directly; only the total tree cost is returned.

### Function Contract
**Inputs**

- `points`: An array of $N$ distinct coordinate pairs `[x, y]`, where $1 \le N \le 1000$ and $-10^6 \le x,y \le 10^6$.

**Return value**

Return the minimum total Manhattan-distance cost of a tree connecting every point.

### Examples
**Example 1**

- Input: `points = [[0,0],[2,2],[3,10],[5,2],[7,0]]`
- Output: `20`

**Example 2**

- Input: `points = [[3,12],[-2,5],[-4,1]]`
- Output: `18`

**Example 3**

- Input: `points = [[0,0]]`
- Output: `0`

### Required Complexity

- **Time:** $O(N^2)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Grow a minimum spanning tree with Prim's rule**

Treat every point as a vertex of the complete graph whose edge weights are Manhattan distances. Maintain `best_distance[i]`, the cheapest edge currently known from the growing tree to point `i`. Start with one point at distance zero.

At each step, select the unvisited point with the smallest `best_distance`, add that cost to the answer, and mark the point as part of the tree. Then compute its distance to every unvisited point and lower those points' best distances when this new edge is cheaper.

**Why each selected edge is safe**

Before a point is added, the visited and unvisited vertices form a cut. The selected `best_distance` is the lightest edge crossing that cut. By the minimum-spanning-tree cut property, some optimal spanning tree contains that edge, so adding it never prevents an optimal result.

Each iteration adds one new vertex and one connecting edge except for the zero-cost starting vertex. After $N$ iterations, all vertices are connected with $N-1$ edges and the accumulated cost is minimum.

#### Complexity detail

Selecting the next point scans up to $N$ distances, and updating distances scans up to $N$ points. Repeating for all $N$ vertices gives $O(N^2)$ time.

The visited flags and best-distance array use $O(N)$ auxiliary space.

#### Alternatives and edge cases

- **Kruskal's algorithm:** materialize all $O(N^2)$ edges, sort them, and join components. It is correct but uses $O(N^2)$ space and $O(N^2\log N)$ time.
- **Repeated full cut scan:** search every visited-to-unvisited edge from scratch at each step. It implements Prim correctly but takes $O(N^3)$ time.
- **Heap-based Prim:** push candidate edges into a priority queue. On the dense complete graph it can retain quadratic edges and adds logarithmic overhead.
- **Single point:** no edge is required, so the cost is zero.
- **Two points:** the answer is their Manhattan distance.
- **Collinear points:** connecting neighboring coordinates in order often realizes the optimum.
- **Negative coordinates:** absolute differences handle them without special cases.
- **Large coordinates:** the total may exceed individual coordinate bounds, so fixed-width implementations need adequate integer range.
- **Several equal edge weights:** any safe minimum crossing edge may be chosen.

</details>
