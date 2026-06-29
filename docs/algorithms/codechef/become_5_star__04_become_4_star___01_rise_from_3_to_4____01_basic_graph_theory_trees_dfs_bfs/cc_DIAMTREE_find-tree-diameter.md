# Find Tree Diameter

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIAMTREE |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [DIAMTREE](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/DIAMTREE) |

---

## Problem Statement

You're given a tree with $N$ vertices numbered from $1$ to $N$. A tree is defined as a connected, undirected graph with $N$ vertices and $N-1$ edges. The distance between two vertices in a tree is equal to the number of edges on the unique simple path between them.

The diameter of a tree is the maximum distance between two nodes. Your task is to determine the diameter of the tree.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$.
- Each of the following $N−1$ lines contains two space-separated integers $u$ and $v$ denoting an edge between nodes $u$ and $v$.

### Output
For each test case, output in a single line the answer to the problem - the diameter of the tree.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq u, v \leq N$

---

## Examples

**Example 1**

**Input**

```text
2
6
1 2
1 3
2 4
2 5
3 6
5
1 2
1 3
3 4
3 5
```

**Output**

```text
4
3
```

**Explanation**

**Example case 1:** The structure of the given tree is shown below.

- The diameter corresponds to the path $4?2?1?3?6$ or $5?2?1?3?6$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Find Tree Diameter](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/DIAMTREE)

### [](#problem-statement-1)Problem Statement

You’re given a tree with N vertices numbered from 1 to N. A tree is defined as a connected, undirected graph with N vertices and N-1 edges. The distance between two vertices in a tree is equal to the number of edges on the unique simple path between them.

The diameter of a tree is the maximum distance between two nodes. Your task is to determine the diameter of the tree.

### [](#approach-2)Approach

The code uses a **“two-pass BFS”** to find the tree’s diameter. First, we run BFS from an arbitrary node (node 1) to find the farthest node, called a leaf. Then, we run BFS again from this leaf to find the farthest node from it. The distance between these two nodes is the tree’s diameter. This method is efficient as BFS runs twice,  each taking O(N) time

### [](#time-complexity-3)Time Complexity

The time complexity is O(N), as we perform two BFS operations.

### [](#space-complexity-4)Space Complexity

The space complexity is O(N), due to the adjacency list and queue used for BFS.

</details>
