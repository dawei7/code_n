# Checking Existence of Edge Length Limited Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1697 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Union-Find, Graph Theory, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/) |

## Problem Description
### Goal

An undirected weighted graph has $n$ vertices labeled from 0 through $n-1$. Each entry `edgeList[i] = [u_i, v_i, distance_i]` connects its two different endpoints with the given distance. Multiple edges may connect the same pair of vertices.

For every query `[p_j, q_j, limit_j]`, decide whether some path connects `p_j` to `q_j` using only edges whose individual distances are strictly less than `limit_j`. The path may contain any number of edges, but one edge equal to the limit invalidates that candidate path. Return the boolean answers in the same order as the input queries.

### Function Contract
**Inputs**

- `n`: the number of graph vertices, with $2 \le n \le 10^5$
- `edgeList`: $E$ undirected triples `[u, v, distance]`, where $1 \le E \le 10^5$
- `queries`: $Q$ triples `[p, q, limit]`, where $1 \le Q \le 10^5$

Endpoints are valid vertex labels, each edge and query uses two different vertices, and every distance and limit lies between 1 and $10^9$.

**Return value**

A length-$Q$ boolean list whose entry at each index answers the corresponding input query.

### Examples
**Example 1**

- Input: `n = 3, edgeList = [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], queries = [[0, 1, 2], [0, 2, 5]]`
- Output: `[false, true]`

The weight-2 edge is not below the first limit. Under limit 5, weights 2 and 4 connect all three vertices.

**Example 2**

- Input: `n = 5, edgeList = [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], queries = [[0, 4, 14], [1, 4, 13]]`
- Output: `[true, false]`

**Example 3**

- Input: `n = 4, edgeList = [[0, 1, 3], [1, 2, 5], [2, 3, 7]], queries = [[0, 3, 8], [0, 2, 5], [1, 3, 8]]`
- Output: `[true, false, true]`

### Required Complexity

- **Time:** $O((E+Q)log(E+Q))$
- **Space:** $O(n+E+Q)$

<details>
<summary>Approach</summary>

#### General

**View each limit as a connectivity snapshot**

For a fixed limit, discard every edge whose distance is not strictly smaller. The query is then an ordinary connectivity question in the remaining undirected graph. As the limit increases, edges are only added; connected components merge and never split. This monotonicity allows all queries to share one incremental graph sweep.

Sort the edges by distance. Attach each query's original index and sort queries by limit. Maintain a disjoint-set union structure initially containing $n$ singleton components and an edge pointer. Before answering a query with limit `limit`, union every still-unprocessed edge satisfying `distance < limit`. Do not union an equal-distance edge yet.

At that moment, the disjoint-set components are exactly the connected components of the graph containing all and only edges below the current limit. The query is true precisely when `find(p) == find(q)`. Store that boolean at the query's original index so sorting does not reorder the returned answers.

**Keep component operations nearly constant**

Path compression shortens parent chains during `find`, and union by component size attaches the smaller tree beneath the larger. These rules give amortized $O(\alpha(n))$ time per operation. Each edge is unioned at most once across the entire sweep rather than reconsidered for each query.

The component invariant follows initially from the empty eligible graph. Adding the next eligible edge merges exactly the two components that this edge connects, preserving the invariant. Therefore every saved answer matches the strict-threshold graph for its query.

#### Complexity detail

Sorting the $E$ edges and $Q$ indexed queries takes $O(E\log E+Q\log Q)$ time. At most $E$ unions and $2Q$ query finds add $O((E+Q)\alpha(n))$, which is within $O((E+Q)\log(E+Q))$. Parents and sizes use $O(n)$ space, while sorted edge and indexed-query lists plus answers use $O(E+Q)$.

#### Alternatives and edge cases

- **Graph search per query:** filtering edges and running BFS or DFS independently is straightforward but can take $O(Q(n+E))$ time.
- **Minimum spanning forest:** the maximum edge on a minimax path can answer queries after additional tree preprocessing, but the offline threshold sweep is simpler for a static query batch.
- **Union equal-weight edges too early:** this changes the strict `< limit` rule into `<= limit` and produces incorrect boundary answers.
- **Parallel edges:** each edge is processed independently; a lighter parallel edge may connect endpoints under a limit that excludes the heavier one.
- **Disconnected graph:** vertices in distinct final components remain false for every limit.
- **Query order:** sorting is internal only; answers must be written back by original index.
- **Repeated limits:** all queries at one limit observe the same component snapshot, and no equal-weight edge is eligible for any of them.

</details>
