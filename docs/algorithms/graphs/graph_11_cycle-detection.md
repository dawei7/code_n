# Cycle Detection (Directed and Undirected)

| | |
|---|---|
| **ID** | `graph_11` |
| **Category** | graphs |
| **Complexity (required)** | $O(V + E)$ Time, $O(V)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Course Schedule](https://leetcode.com/problems/course-schedule/) |

## Problem statement

Given a graph represented as an adjacency list. Determine if the graph contains at least one cycle.
The implementation differs fundamentally depending on whether the graph is **Directed** or **Undirected**.

**Input:** Number of vertices `V` and an adjacency list `adj`.
**Output:** A boolean. `True` if a cycle exists, `False` otherwise.

## When to use it

- To validate dependency trees (checking if a curriculum is impossible to finish).
- To check if a graph is a valid Tree (a Tree is a connected undirected graph with exactly 0 cycles).

## Approach 1: Undirected Graphs

In an undirected graph, an edge A - B goes both ways. If you traverse A \rightarrow B, the neighbor list of B will contain A. If you naively go back to A, you might falsely claim "Cycle!".
**The Rule:** A cycle in an undirected graph only exists if you reach an ALREADY VISITED node that is **NOT YOUR IMMEDIATE PARENT**.

1. Run DFS. Pass along the `curr` node and its `parent`.
2. When evaluating a `neighbor` of `curr`:
   - If `neighbor == parent`: Ignore it (it's the edge we just walked across).
   - If `neighbor` is in `visited`: We found a cycle!
   - If `neighbor` is not in `visited`: Mark visited and recurse `dfs(neighbor, parent=curr)`.

## Approach 2: Directed Graphs (The 3-Color Method)

In a directed graph, the "parent" rule doesn't work. The graph A \rightarrow B, A \rightarrow C, B \rightarrow C is perfectly valid (a diamond shape, not a cycle). However, C will be visited twice! If we just use a single `visited` set, we would falsely claim a cycle when the second path reaches C.
**The Rule:** A cycle in a directed graph only exists if you reach a node that is **CURRENTLY IN YOUR ACTIVE RECURSION STACK**.

We use a `state` array for every vertex with 3 colors:
- `0` (White): Unvisited.
- `1` (Gray): Currently visiting (it is in the active DFS call stack).
- `2` (Black): Completely finished (all its children have been explored).

1. Run DFS.
2. Mark `state[curr] = 1`.
3. For each `neighbor`:
   - If `state[neighbor] == 1`: We looped back to a node in our active stack! **CYCLE DETECTED!**
   - If `state[neighbor] == 0`: Recurse `dfs(neighbor)`.
4. After checking all neighbors, mark `state[curr] = 2` and return.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_11: Cycle Detection (Undirected).

Iterative DFS with parent tracking. A back-edge to a non-parent
visited node is a cycle.
"""


def solve(num_nodes, edges):
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * num_nodes
    for start in range(num_nodes):
        if visited[start]:
            continue
        stack = [(start, -1)]
        visited[start] = True
        while stack:
            u, parent = stack.pop()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append((v, u))
                elif v != parent:
                    return True
    return False
```

</details>

## Walk-through (Directed)

`adj = {0: [1], 1: [2], 2: [0]}`.
`state = [0, 0, 0]`.

1. Loop starts at `i=0`. `state[0] == 0`. Call `dfs(0)`.
2. `dfs(0)`: `state[0] = 1`.
   - Neighbor `1`. `state[1] == 0`. Call `dfs(1)`.
3. `dfs(1)`: `state[1] = 1`.
   - Neighbor `2`. `state[2] == 0`. Call `dfs(2)`.
4. `dfs(2)`: `state[2] = 1`.
   - Neighbor `0`. `state[0] == 1`!
   - `1 == 1`! Cycle detected! Return `True`.
5. Returns bubble all the way up. Output is `True`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V + E)$ | $O(V)$ |
| **Average** | $O(V + E)$ | $O(V)$ |
| **Worst** | $O(V + E)$ | $O(V)$ |

Since we use a DFS that never re-visits completely processed nodes (either via the `visited` set or `state == 2`), every vertex is processed once and every edge is traversed once. Time complexity is strictly $O(V + E)$.
Space complexity is $O(V)$ for the state array/visited set, and $O(V)$ for the recursion call stack in the worst-case (a linear chain).

## Variants & optimizations

- **Kahn's Algorithm (Directed):** Instead of using DFS, you can run Kahn's Topological Sort (`graph_07`). If Kahn's terminates but hasn't appended exactly V elements to the output array, a cycle definitely exists! (This avoids recursion stack limits).
- **Union-Find (Undirected):** You can use a Disjoint Set (`graph_09`). Iterate over all edges. If `find(u) == find(v)`, you just found an edge that connects two nodes already in the same component! That's a cycle! (This is how Kruskal's works).

## Real-world applications

- **Deadlock Detection:** In OS kernel design, a "Wait-For" graph maps which processes are waiting for locks held by other processes. If a cycle is detected, the system is in a Deadlock and one process must be killed.
- **Spreadsheet Circular References:** Excel detects if Cell A = Cell B + 1, and Cell B = Cell A + 1 using directed cycle detection.

## Related algorithms in cOde(n)

- **[graph_03 - Depth-First Search](graph_03_dfs.md)** — The foundation of the traversal.
- **[graph_07 - Topological Sort](graph_07_topological-sort.md)** — Kahn's algorithm, the queue-based alternative for directed graphs.
- **[graph_09 - Union-Find](graph_09_union-find.md)** — The subset-merging alternative for undirected graphs.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
