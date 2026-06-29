# DFS on Graph

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GRAPHDFS |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Graphs |
| Official Link | [GRAPHDFS](https://www.codechef.com/learn/course/graphs/GRAPHTRAVERS/problems/GRAPHDFS) |

---

## Problem Statement

Now, let's take a deeper look at the DFS.

Depth-First Search (DFS) is a graph traversal algorithm that explores a graph by going as deep as possible along each branch before backtracking. It starts from a source node, explores as far as possible along each branch, and then backtracks.

**Algorithm Steps:**
1. Start from a source node.
2. Visit the current node. Mark it visited using a boolean array/vector.
3. Recursively explore each unvisited neighbor.
4. If a node has no unvisited neighbors, backtrack to the previous node

### Video Explanation

### Task
- Test the given code in editor with different graph's inputs. Also submit the code.

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the number of nodes and edges in the graph.
- The next $M$ lines describe the edges. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
4 5
1 2
2 3
3 4
1 4
1 3
```

**Output**

```text
DFS traversal: 1 2 3 4
```
