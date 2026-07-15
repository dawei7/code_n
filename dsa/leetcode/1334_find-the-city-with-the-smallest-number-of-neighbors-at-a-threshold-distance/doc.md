# Find the City With the Smallest Number of Neighbors at a Threshold Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1334 |
| Difficulty | Medium |
| Topics | Dynamic Programming, Graph Theory, Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) |

## Problem Description
### Goal
There are $n$ cities numbered from 0 through $n-1$. The array `edges` describes an undirected weighted graph: each record `[from, to, weight]` connects two different cities in both directions with the given positive distance. Every unordered city pair appears at most once.

For each city, count how many other cities can be reached by a path whose total distance is at most `distanceThreshold`. Return the city with the smallest such count. If several cities share that minimum, return the one with the greatest numeric index.

### Function Contract
**Inputs**

- `n`: the number of cities, where $2\le n\le100$.
- `edges`: between 1 and $n(n-1)/2$ distinct undirected edges `[from, to, weight]`, with $0\le\texttt{from}<\texttt{to}<n$ and $1\le\texttt{weight}\le10^4$.
- `distance_threshold`: the inclusive maximum path distance, between 1 and $10^4$.

**Return value**

The greatest-indexed city among those having the fewest other cities reachable within the threshold.

### Examples
**Example 1**

- Input: `n = 4`, `edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]`, `distance_threshold = 4`
- Output: `3`

**Example 2**

- Input: `n = 5`, `edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]`, `distance_threshold = 2`
- Output: `0`

**Example 3**

- Input: `n = 3`, `edges = [[0,1,5],[1,2,5],[0,2,20]]`, `distance_threshold = 10`
- Output: `2`
- Explanation: Every city can reach both others, so the greatest index wins the tie.

### Required Complexity
- **Time:** $O(n^3)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Build shortest paths through successively allowed intermediates**

Create an $n\times n$ distance matrix initialized to infinity, put zero on its diagonal, and copy each undirected edge weight into both symmetric entries. Floyd-Warshall then considers every city `k` as a possible intermediate. For each ordered pair `(i, j)`, replace its distance when traveling from `i` through `k` to `j` is shorter.

After processing `k`, every matrix entry is the shortest path whose intermediate cities come only from 0 through `k`. The update compares the best path that avoids `k` with one formed from two already-optimal subpaths meeting at `k`; induction over the allowed intermediates therefore yields all-pairs shortest distances.

Count, for each row, entries no greater than `distance_threshold`, excluding the zero-distance entry for the city itself. Scan city indices in ascending order and replace the answer whenever the new count is less than or equal to the best count. Allowing equality deliberately retains the greatest index required by the tie rule.

#### Complexity detail

The three Floyd-Warshall loops examine $n^3$ city triples, and the final counts take $O(n^2)$ time, for $O(n^3)$ total. The distance matrix uses $O(n^2)$ space.

#### Alternatives and edge cases

- **Dijkstra from every city:** Positive edge weights permit $n$ heap-based shortest-path runs, which can be preferable for sparse graphs but requires a more involved adjacency-list implementation.
- **Bellman-Ford from every city:** This also computes the required distances but ignores the positive-weight advantage and can take $O(n^2m)$ time for $m$ edges.
- **Disconnected graph:** Infinite matrix entries are never counted as reachable.
- **Inclusive threshold:** A shortest path exactly equal to `distance_threshold` qualifies.
- **Indirect path:** A route through intermediate cities may be shorter than a direct edge.
- **Tie:** Updating on an equal neighbor count ensures the greatest city index is returned.

</details>
