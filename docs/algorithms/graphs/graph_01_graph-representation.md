# Graph Representations

| | |
|---|---|
| **ID** | `graph_01` |
| **Category** | graphs |
| **Complexity (required)** | Varies based on representation |
| **Difficulty** | 2/10 |
| **Interview relevance** | 10/10 |
| **GeeksForGeeks Equivalent** | [Graph and its representations](https://www.geeksforgeeks.org/graph-and-its-representations/) |

## Problem statement

Before any Graph algorithm (BFS, DFS, Dijkstra) can be executed, the Graph data structure must first be constructed in memory from a given list of edges.
Given V vertices and an array of E edges where `edges[i] = [u, v]` (meaning there is a connection between vertex `u` and vertex `v`), build the foundational graph representation.

**Input:** Number of vertices `V`, and a 2D integer array `edges`.
**Output:** A data structure representing the graph.

## When to use it

- The mandatory first 5 lines of code in 100% of graph interview questions.
- You must choose between an Adjacency Matrix and an Adjacency List based on the graph's density (dense vs. sparse).

## Approach

**1. The Adjacency Matrix:**
A 2D array of size V x V where `matrix[u][v] = 1` if there is an edge from `u` to `v`, and `0` otherwise.
- **Pros:** Checking if an edge exists between `u` and `v` takes absolute $O(1)$ time. Removing an edge takes $O(1)$ time.
- **Cons:** It takes $O(V^2)$ memory space regardless of how many edges actually exist. Iterating over the neighbors of `u` takes $O(V)$ time, even if `u` only has 1 neighbor!
- **When to use:** ONLY when the graph is incredibly dense (almost every vertex is connected to every other vertex, E ~= V^2), or when V is very small (e.g., V \le 1000).

**2. The Adjacency List:**
An array of lists (or a HashMap mapping a vertex to a list of its neighbors). `adj[u] = [v1, v2, v3]`.
- **Pros:** It only takes $O(V + E)$ memory space. Iterating over the neighbors of `u` only takes time proportional to the actual number of neighbors `u` has! This makes BFS/DFS traverse in strictly $O(V + E)$ time rather than $O(V^2)$.
- **Cons:** Checking if an edge exists between `u` and `v` takes $O(\text{degree}(u)$) time, as you have to scan the list of neighbors.
- **When to use:** The default choice for 99% of interviews. Most real-world graphs (social networks, maps) are extremely sparse (E \ll V^2).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_01: Graph Representation.

Build an adjacency list from a list of edges. The graph is
undirected, so each edge (u, v) adds v to u's list and u to v's.
The input may contain duplicate edges; using a per-node set
deduplicates them in O(1) each. O(n) where n is the number of
edges.
"""


def solve(num_nodes, edges):
    graph = {i: set() for i in range(num_nodes)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    return {node: sorted(neighbors) for node, neighbors in graph.items()}
```

</details>

## Walk-through

`V = 4`, `edges = [[0, 1], [0, 2], [1, 2], [2, 3]]`. (Undirected).

**Adjacency Matrix:**
Initially a 4 x 4 grid of `0`s.
1. `[0, 1]`: `matrix[0][1] = 1`, `matrix[1][0] = 1`.
2. `[0, 2]`: `matrix[0][2] = 1`, `matrix[2][0] = 1`.
3. `[1, 2]`: `matrix[1][2] = 1`, `matrix[2][1] = 1`.
4. `[2, 3]`: `matrix[2][3] = 1`, `matrix[3][2] = 1`.
```text
[
  [0, 1, 1, 0],
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 0, 1, 0]
]
```

**Adjacency List:**
1. `[0, 1]`: `adj[0] = [1]`, `adj[1] = [0]`.
2. `[0, 2]`: `adj[0] = [1, 2]`, `adj[2] = [0]`.
3. `[1, 2]`: `adj[1] = [0, 2]`, `adj[2] = [0, 1]`.
4. `[2, 3]`: `adj[2] = [0, 1, 3]`, `adj[3] = [2]`.
```text
{
  0: [1, 2],
  1: [0, 2],
  2: [0, 1, 3],
  3: [2]
}
```

## Complexity

| | Time | Space |
|---|---|---|
| **Adj Matrix** | $O(V^2)$ Init + $O(E)$ Add | $O(V^2)$ |
| **Adj List** | $O(E)$ | $O(V + E)$ |

Initializing an Adjacency Matrix takes $O(V^2)$ because you must physically allocate and zero out a 2D array. Adding the edges takes $O(E)$. Total time is $O(V^2 + E)$. Space is strictly $O(V^2)$.
Initializing an Adjacency List via a HashMap takes $O(1)$ initially. Adding the edges takes $O(E)$. Total time is $O(E)$. Space is $O(V + E)$ to store the keys and lists.

## Variants & optimizations

- **Edge Weights:** If edges have weights `(u, v, weight)`, in a Matrix you store `matrix[u][v] = weight` (and initialize empty spaces to `infinity` instead of `0`). In an Adjacency List, you append a tuple: `adj[u].append((v, weight))`.
- **Set vs List:** If the graph has duplicate edges (multigraph), `adj[u].append(v)` will add `v` twice! If you need to enforce simple graphs, use `adj = defaultdict(set)` and `adj[u].add(v)`. Checking edge existence becomes $O(1)$ instead of $O(\text{degree}(u)$), but iteration becomes slightly slower due to set overhead.

## Real-world applications

- **Routing Tables:** Modern internet routers use highly optimized Adjacency Lists (representing the network topology) to run Shortest Path algorithms like OSPF.

## Related algorithms in cOde(n)

- **[graph_02 - Breadth-First Search](graph_02_bfs.md)** — The foundational algorithm that traverses the Adjacency List.
- **[graph_03 - Depth-First Search](graph_03_dfs.md)** — The recursive alternative traversing the exact same Adjacency List.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
