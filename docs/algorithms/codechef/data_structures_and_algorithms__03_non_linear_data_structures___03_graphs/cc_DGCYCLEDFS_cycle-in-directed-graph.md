# Cycle in Directed Graph

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DGCYCLEDFS |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Connectivity and Cycles in Graphs |
| Official Link | [DGCYCLEDFS](https://www.codechef.com/learn/course/graphs/GRAPHCYCLE/problems/DGCYCLEDFS) |

---

## Problem Statement

### Video Explanation

The cycle detection algorithm for directed and undirected graphs using DFS is different because in a directed graph, two different paths to the same vertex don't make a cycle, while in an undirected graph, they do. In short, we cannot say that directed graph is having a cycle, if we get to a node which is already marked visited.

Take a look at the following directed graph:

![digraph](https://cdn.codechef.com/images/learning/graphs-trees/directed-graph2.png)

This graph doesn't have a cycle in it. However if we use cycle detection algorithm of undirected graph, the `visited` array will first mark the node `4` visited while traversing it through upper path and once the dfs traces back and visits the same node via lower path, it finds the node `4` already visited and hence detects a cycle.

However the following algorithm which uses node coloring scheme instead of marking them visited, solves the above problem. Let's take a look at the algorithm and understand how:

We run a series of DFS in the graph. Initially all vertices are colored white (0). From each unvisited (white) vertex, start the DFS, mark it gray (1) while entering and mark it black (2) on exit. If DFS moves to a gray vertex, then we have found a cycle .

Let's take a look at a more detailed and elaborate explanation of the algorithm:

**Key Idea:**
The algorithm uses a coloring scheme to mark the state of each node during the DFS traversal. Three possible colors are used:

_White (0)_: Unvisited node. \
_Gray (1):_ Node is currently in the process of being visited. \
_Black (2):_ Node has been visited and processed.

**DFS Traversal:**

For each unvisited node in the graph, initiate a DFS traversal.
During the DFS, mark the current node as gray (color[node] = 1) when starting the exploration.
Recursively visit each neighbor of the current node.
If a neighbor is already marked as gray, a cycle is detected.
If the DFS traversal completes without finding a cycle, mark the current node as black (color[node] = 2).

**Cycle Detection:**

A cycle is detected when a node currently being visited (gray) is encountered during the DFS traversal. This indicates that there is a back edge in the graph, forming a cycle.

Here's a pseudocode for finding cycle in a directed graph using Depth-First Search (DFS):

**Pseudocode:**

```plaintext
Procedure DFS(node):
    if color[node] == 1 then
        return true  // Cycle detected
    end if

    if color[node] == 0 then
        color[node] = 1
        for each neighbor in adj[node] do
            if DFS(neighbor) then
                return true  // Cycle detected
            end if
        end for
    end if

    color[node] = 2
    return false

Procedure findCycle(n):
    Create an array color of size n and initialize all elements to 0  // 0 represents unvisited

    has_cycle = false

    for v from 1 to n do
        if color[v] == 0 and DFS(v) then
            has_cycle = true
            break
        end if
    end for

    if has_cycle then
        Output "YES"
    else
        Output "NO"
    end if

```

### Task
- Implement the given algorithm to check if given directed graph contains any cycle.

---

## Input Format

- The first line consists of two space separated integers, `N` and `M`, representing the number of nodes and edges.
- Nodes are numbered from `1` to `N`.
- The subsequent `M` lines describe the edges in , each containing two integers, `u` and `v`, describing the directed edge from node `u` to node `v`.
- Each edge links two distinct nodes, and at most one edge exists between any two nodes.

---

## Output Format

- Output `YES` if there is cycle in graph, else `NO`.

---

## Constraints

- $1 \leq N \leq 200000$
- $1 \leq M \leq N(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.

---

## Examples

**Example 1**

**Input**

```text
5 6
1 2
2 3
3 1
3 5
2 4
4 5
```

**Output**

```text
YES
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Graphs, DFS

**Problem:**  Implement the algorithm to check if a given directed graph contains any cycle.

**Solution Approach:** As mentioned on the problem statement page, we run a series of DFS to find the cycle in a directed graph.

*Key Idea:* The algorithm uses a coloring scheme to mark the state of each node during the DFS traversal. Three possible colors are used:

White (0): Unvisited node.

Gray (1): Node is currently in the process of being visited.

Black (2): Node has been visited and processed.

*DFS Traversal:*

For each unvisited node in the graph, initiate a DFS traversal. During the DFS, mark the current node as gray (color[node] = 1) when starting the exploration. Recursively visit each neighbor of the current node. If a neighbor is already marked as gray, a cycle is detected. If the DFS traversal completes without finding a cycle, mark the current node as black (color[node] = 2).

*Cycle Detection:*

A cycle is detected when a node currently being visited (gray) is encountered during the DFS traversal. This indicates that there is a back edge in the graph, forming a cycle.

**Time complexity:**  O(N + M) as we need to explore all nodes using DFS.

**Space complexity:**  O(N) as we need to store the colors of the nodes in an array.

</details>
