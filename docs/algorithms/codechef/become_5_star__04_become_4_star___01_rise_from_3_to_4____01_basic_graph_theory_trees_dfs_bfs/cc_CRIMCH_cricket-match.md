# Cricket Match

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CRIMCH |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [CRIMCH](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/CRIMCH) |

---

## Problem Statement

There are $N$ people numbered from $1$ to $N$ and they want to play a cricket match between them by forming two teams that may not be of the same size. There are $M$ pairs of peoples and for each pair of peoples, they can not be in the same team. Now Chef wants to know if there is any way to split them into two teams such that Chef can organize the cricket match between two teams. If possible then print `"YES"` (without quotes), otherwise print `"NO"` (without quotes).

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- Each of the following $M$ lines follows. Each line has two space-separated numbers $u$ and $v$.

### Output
For each test case, output in a single line the answer to the problem.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N \leq 2000$
- $1 \leq M \leq 10000$
- $1 \leq u < v \leq N$

---

## Examples

**Example 1**

**Input**

```text
2
3 3
1 2
1 3
2 3
4 2
1 4
2 3
```

**Output**

```text
NO
YES
```

**Explanation**

**Example case 1:** It's impossible to divide them into two teams.

**Example case 2:** Both the teams will look like $[1, 2]$ and $[3, 4]$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Cricket Match](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/CRIMCH)

### [](#problem-statement-1)Problem Statement -

There are N people numbered from 1 to N and they want to play a cricket match between them by forming two teams that may not be of the same size. There are M pairs of peoples and for each pair of peoples, they can not be in the same team. Now Chef wants to know if there is any way to split them into two teams such that Chef can organize the cricket match between two teams. If possible then print `"YES"` (without quotes), otherwise print `"NO"` (without quotes).

### [](#approach-2)Approach -

The problem can be visualized as graph where each person is a node, and each restricted pair forms an edge. The task is to split the nodes into two groups, which requires checking if the graph is *bipartite*. In a bipartite graph, nodes can be divided into two sets where no two nodes within the same set are adjacent. To verify this, we can use *DFS* (or *BFS*), assigning each node a level or “depth” during traversal. We start with an unvisited node, assigning it an initial level (0), and assign alternating levels (0 and 1) to adjacent nodes.

If we find two adjacent nodes with the same level, the graph contains an odd-length cycle, meaning it’s non-bipartite, so we output `"NO"`. This indicates we can’t separate the nodes into two groups. If no such condition occurs in any graph component, we output `"YES"`.

### [](#time-complexity-3)Time Complexity

O(N + M), where N is the number of nodes and M is the number of edges.

### [](#space-complexity-4)Space Complexity

O(N + M), for storing the graph and levels of nodes.

</details>
