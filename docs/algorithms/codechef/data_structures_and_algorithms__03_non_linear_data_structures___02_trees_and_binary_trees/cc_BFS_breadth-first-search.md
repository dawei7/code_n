# Breadth First Search

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BFS |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [BFS](https://www.codechef.com/learn/course/trees/TREES/problems/BFS) |

---

## Problem Statement

In BFS algorithm, we focus on traversing the tree "breadth-wise", i.e, the traversal begins at the root as usual, but instead of traversing a single branch till full depth, we traverse the nodes of all branches according to level. The nodes in the next level are traversed only after all the nodes at the current level/depth have been traversed.

BFS is commonly implemented using a queue data structure, and it's often used for problems where the goal is to find the shortest path or to visit all nodes at a given depth in the tree.

1. **Start by selecting root** as the starting point of the traversal.
2. **Create a queue** and add the starting node to it.
3. **While the queue is not empty**, repeat the following steps:
   - Remove a node from the queue and process it (e.g., print its value).
   - Mark the node as visited and remove it from the queue
   - Retrieve all adjacent nodes of the node being processed. For each of these nodes, if it has not been visited yet, add it to the queue.
4. Continue the process until the queue is empty.

BFS guarantees that it visits all vertices at the current level before moving on to the next level, ensuring that it explores the tree in a breadth-first fashion. This property is useful in various applications, such as finding the shortest path.

### Video Explanation

See the BFS traversal of the following tree:

![Tree BFS](https://cdn.codechef.com/images/learning/graphs-trees/tree-bfs-gif.gif)

### Task
- Given a tree with $N$ vertices and $N - 1$ edges, rooted at node number $1$.
- Output the nodes while traversing the tree in BFS order.

---

## Input Format

- The first line of the input contains single integer $N$ — the number of vertices.
- The next $N - 1$ lines describe the edges. The $i$-th of these $N - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

Output $N$ integers on the same line - the vertices of the given tree in BFS order.

---

## Constraints

- $1 \leq N \leq 100000$
- $1 \leq u_i, v_i \leq N$

---

## Examples

**Example 1**

**Input**

```text
10
1 2
1 3
1 4
2 5
5 9
3 6
3 7
6 10
4 8
```

**Output**

```text
1 2 3 4 5 6 7 8 9 10
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Trees or Graph

**Problem :-** Given a tree with N vertices and N − 1 edges, rooted at node number 1. Output the nodes while traversing the tree in BFS order.

**Solution Approach :-**

The problem involves performing a Breadth-First Search (BFS) traversal of a tree rooted at node 1. Here’s the solution approach:

- Initialize Data Structures:

- Create a queue to store nodes during BFS traversal.

- Create a boolean array to keep track of visited nodes to avoid revisiting.

- BFS Traversal:

- Start with the root node (node 1) and enqueue it.

- While the queue is not empty:

- Dequeue a node, output its value, and mark it as visited.

- Enqueue all unvisited children of the dequeued node.

- Continue this process until the queue is empty.

- Output:

- The output sequence represents the BFS order of nodes in the tree.

**Time Complexity:** O(N+E) - Each node and each edge are visited once during BFS traversal, where N is the number of vertices, and E is the number of edges. E = N - 1 in case of trees. So, ultimately, the time complexity is O(N)

**Space Complexity:** O(N) - The space required for the queue and the boolean array for visited nodes.

</details>
