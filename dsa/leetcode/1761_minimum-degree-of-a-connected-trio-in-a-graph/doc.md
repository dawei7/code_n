# Minimum Degree of a Connected Trio in a Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1761 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Graph Theory, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/) |

## Problem Description

### Goal

You are given an undirected graph with nodes numbered from $1$ through $n$. Each pair in `edges` joins two distinct nodes. A connected trio is a set of exactly three nodes in which every pair is directly connected, so the three nodes form a triangle.

The degree of a connected trio is the number of graph edges having exactly one endpoint inside that trio and the other endpoint outside it. Find the minimum degree among all connected trios. If the graph contains no connected trio, return `-1`.

### Function Contract

**Inputs**

- `n`: the number of graph nodes, with $2 \le n \le 400$.
- `edges`: distinct undirected edges `[u, v]` with $1 \le u,v \le n$ and $u \ne v$.

Let $m=\lvert\texttt{edges}\rvert$.

**Return value**

- Return the minimum number of edges leaving any three-node clique.
- Return `-1` when no three nodes are pairwise adjacent.

### Examples

**Example 1**

- Input: `n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]`
- Output: `3`
- Explanation: Nodes `1`, `2`, and `3` form a trio, with one edge from each trio node to an outside node.

**Example 2**

- Input: `n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]`
- Output: `0`
- Explanation: Nodes `1`, `3`, and `4` form a triangle with no edge leaving the trio.

**Example 3**

- Input: `n = 5, edges = [[1,2],[2,3],[3,4],[4,5]]`
- Output: `-1`
- Explanation: The path contains no set of three pairwise adjacent nodes.

### Required Complexity

- **Time:** $O(n^3)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Record adjacency and node degrees**

Build a symmetric Boolean adjacency matrix so any potential edge can be tested in constant time. While reading each undirected edge, increment the degree of both endpoints.

**Enumerate every node triple once**

Choose indices satisfying `first < second < third`. This ordering covers each three-node set exactly once. Skip a pair immediately when `first` and `second` are not adjacent; otherwise the third node completes a connected trio precisely when it is adjacent to both.

**Convert node degrees into trio degree**

For a triangle with nodes $a$, $b$, and $c$, the sum

$$
\deg(a)+\deg(b)+\deg(c)
$$

counts every edge leaving the trio once. It also counts each of the triangle's three internal edges twice, once at each endpoint. Subtracting six removes these internal contributions, so the trio degree is

$$
\deg(a)+\deg(b)+\deg(c)-6.
$$

**Track the minimum and detect absence**

Minimize this value across every discovered triangle. The ordered enumeration cannot omit a trio, and the degree formula counts exactly its boundary edges, so the smallest recorded value is the requested minimum. If no candidate was recorded, the graph has no connected trio and the answer is `-1`.

#### Complexity detail

Building degrees and adjacency takes $O(n^2+m)$ initialization and input time. The three ordered loops examine $O(n^3)$ triples with constant-time adjacency and degree work, so total time is $O(n^3)$. The adjacency matrix occupies $O(n^2)$ space, while degrees use $O(n)$.

#### Alternatives and edge cases

- **Adjacency-set intersections:** For each edge, intersect the endpoints' neighbor sets to find common third nodes. This can be faster on sparse graphs but has representation-dependent bounds.
- **Count boundary edges separately per trio:** Scanning all outside nodes after finding every triangle is correct but increases worst-case time to $O(n^4)$.
- **Enumerate arbitrary edge triples:** Testing whether three selected edges form a triangle can cost $O(m^3)$ and repeats unnecessary combinations.
- **No triangle:** Return `-1`, even if the graph contains many paths or cycles of length greater than three.
- **Isolated triangle:** Its degree is zero, the smallest possible answer.
- **Complete graph:** Every triple is connected, and each has degree $3(n-3)$.
- **Shared triangle edges:** Different trios may overlap; each ordered node triple must still be evaluated independently.
- **Duplicate edges:** The contract excludes them, so degrees can be incremented directly without deduplication.
- **Disconnected graph:** Components without triangles do not affect a trio found elsewhere.

</details>
