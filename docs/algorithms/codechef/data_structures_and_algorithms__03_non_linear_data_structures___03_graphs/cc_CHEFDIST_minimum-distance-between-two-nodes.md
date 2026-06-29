# Minimum Distance Between Two Nodes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFDIST |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Graphs |
| Official Link | [CHEFDIST](https://www.codechef.com/learn/course/graphs/GRAPHTRAVERS/problems/CHEFDIST) |

---

## Problem Statement

Given an undirected and unweighted graph and two nodes $x$ and $y$, find the length of the shortest path between the two nodes. If no path exists, return $-1$.

## **Function Declaration**

### **Function Name**

$getMinimumDistance$ – Finds the minimum number of edges required to travel from one node to another in an undirected graph.

### **Parameters**

* $n$ : An integer representing the number of nodes in the graph.

* $edges$ : A list/vector of pairs where each pair
  $(u, v)$ represents an undirected edge between nodes $u$ and $v$.

* $x$ : An integer representing the starting node.

* $y$ : An integer representing the destination node.

### **Return Value**

* Returns an **integer** —
  the minimum distance (minimum number of edges) between nodes $x$ and $y$.

* If there is no path between the two nodes, return $-1$.

## Constraints:
- $1 \leq n \leq 200000$ - number of nodes.
- $1 \leq m \leq 200000$ - number of edges.
- $1 \leq u_i, v_i, x, y \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq m$.
- x and y can never be same in the test cases.

**The input and output formats provided below are only for testing with custom inputs. You only need to return the value. Printing is handled by the driver code.**

---

## Input Format

- The first line consists of two space separated integers, $n$ and $m$, representing the number of nodes and edges.
- Nodes are numbered from $1$ to $n$.
- The subsequent $m$ lines describe the connections, each containing two integers, $u$ and $v$, describing the edges.
- Each edge links two distinct nodes, and at most one edge exists between any two nodes.
- The last line consists of two space separated integers, $x$ and $y$, the given two nodes.

---

## Output Format

- If there is a path between $x$ and $y$, print the shortest distance (i.e., the minimum no. of edges) between them.
- If no path exist, return $-1$.

---

## Examples

**Example 1**

**Input**

```text
5 6
1 2
2 3
1 3
3 5
2 4
4 5
2 5
```

**Output**

```text
2
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Graphs, BFS.

**Problem:** Given an undirected and unweighted graph, the task is to find the length of the shortest path between two specified nodes, x and y. If no path exists, return -1.

**Solution Approach:** We can use BFS to solve the problem. If the node x is in same connected component as node y, then the minimum distance can be found, if not then the answer would be -1. Breadth-First Search (BFS) efficiently explores the graph in a level-by-level manner starting from node x. The inherent nature of BFS makes it suitable for finding the shortest path in an unweighted graph, ensuring that the first occurrence node y is reached using the minimum number of edges.

**Key Points:**

- *Level-by-Level Exploration:*

- BFS traverses the graph level by level, starting from the source node (x) and moving outward.

- At each level, all vertices at the same distance from the source are explored before moving to the next level.

- *Shortest Path Guarantee:*

- In an unweighted graph, BFS guarantees that the first occurrence of a target node (y) is reached with the minimum number of edges.

- As BFS explores the graph level by level, the first time y is encountered, it will be through the shortest possible path.

In case y is not reachable from node x, the distance array shall still have initial infinite value at the end of bfs traversal indicating there is no path between them.

**Time complexity:** The time complexity is O(N + M), where N is the number of nodes, and M is the number of edges. Each node and edge is processed once during the BFS traversal.

**Space complexity:** O(N) as the space complexity of BFS is O(N), as we need to put atmost all the nodes in the queue during BFS traversal.

</details>
