# Depth First Search

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSADFS |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [DSADFS](https://www.codechef.com/learn/course/trees/TREES/problems/DSADFS) |

---

## Problem Statement

Depth-First Search (DFS) is a tree traversal algorithm that explores as far as possible along each branch before backtracking. It starts at the root and systematically explores the tree by going as deep as possible along each branch before backtracking.

Here's a more detailed explanation of DFS:

1. **Start at the Source**: Begin the traversal from the root node.

2. **Visit and Print**: Visit the source node and print it.

3. **Explore Children**: Move to an unvisited child of the node and repeat steps 2 and 3.

4. **Backtrack**: If all children of this node are visited, backtrack to a neighboring unvisited node.

5. **Continue Until All Nodes Are Visited**: Repeat steps 3 - 4 until all vertices have been visited.

DFS is often implemented using a recursive approach or a stack data structure.

### Video Explanation

![Tree DFS](https://cdn.codechef.com/images/learning/graphs-trees/dfs-gif.gif)

Check this pseudo code for DFS:
```cpp
void dfs(int node){
    // print node or do anything with it...
    for(int child: tree[node]){ // tree is stored as adjacency list
        dfs(child);
    }
}
```

### Task
- Given a tree with $N$ vertices and $N - 1$ edges, rooted at node number $1$.
- Output the nodes while traversing the tree in DFS order.

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of vertices.
- The next $N - 1$ lines describe the edges. The $i$-th of these $N - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

Output $N$ integers on the same line - the vertices of the given tree in DFS order if we start traversing from the root node 1.

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
1 5
1 9
2 3
3 4
5 6
6 7
5 8
9 10
```

**Output**

```text
1 2 3 4 5 6 7 8 9 10
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:-**  Trees or Graph

**Problem :-** Given a tree with N vertices and N−1 edges, rooted at node number 1. Output the nodes while traversing the tree in DFS order.

**Solution Approach:-** In a tree data structure, the absence of cycles is a fundamental property. This concept is leveraged in the approach described here. During the Depth-First Search (DFS) function call, we maintain awareness of both the parent node and the current node. The objective is to navigate down the depth until all children of the current node are visited and then backtrack to its parent. The crucial principle is to avoid reaching the parent node prematurely, especially when some children of the current node are yet to be explored.

Tree traversal shares similarities with graph traversal, as it is a form of graph traversal. Depth-First Search traversal on a graph closely resembles its counterpart on a tree. The primary distinction lies in the fact that a tree is a specialized type of connected graph without cycles.

Conversely, in DFS traversal on a general graph, additional memory is required to keep track of visited nodes to prevent revisiting them. Unlike trees, graphs can have cycles, and they may not necessarily be connected. Therefore, the tracking of visited nodes becomes essential in graph traversal to handle these variations.

**Time Complexity:** O(N+E) - Each node and each edge are visited once during BFS traversal, where N is the number of vertices, and E is the number of edges. E = N - 1 in case of trees. Hence, the ultimate time complexity is O(N).

**Space Complexity:**  O(1) - as no extra space is needed.

</details>
