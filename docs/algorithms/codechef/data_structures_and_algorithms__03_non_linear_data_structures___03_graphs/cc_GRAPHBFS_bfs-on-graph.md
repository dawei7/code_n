# BFS on Graph

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GRAPHBFS |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Graphs |
| Official Link | [GRAPHBFS](https://www.codechef.com/learn/course/graphs/GRAPHTRAVERS/problems/GRAPHBFS) |

---

## Problem Statement

Now, let's take a deeper look at BFS.

Breadth-First Search (BFS) is a graph traversal algorithm that systematically explores a graph by visiting all the nodes at the current depth before moving on to nodes at the next depth. It starts from a source node and explores its neighbors first, before moving on to the next level of neighbors.

**Algorithm Steps:**
1. Start from a source node.
2. Enqueue the source node into a queue and mark it as visited.
3. While the queue is not empty:
   - Dequeue a node from the queue and process it (print or do other operations).
   - Enqueue all unvisited neighbors of the dequeued node into the queue and mark them as visited.
4. Repeat until the queue is empty.

### Video Explanation

### Task
-  Test the given code in editor with different graph's inputs. Also submit the code.

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the number of nodes and edges in the graph.
- The next $M$ lines describe the edges. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

For each test case, output on a new line the number of good subgraphs of $G$, modulo $10^9 + 7$.

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
BFS traversal: 1 2 4 3
```
