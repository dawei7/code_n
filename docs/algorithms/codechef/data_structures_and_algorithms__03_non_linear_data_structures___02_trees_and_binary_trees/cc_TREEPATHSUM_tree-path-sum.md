# Tree Path Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TREEPATHSUM |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [TREEPATHSUM](https://www.codechef.com/learn/course/trees/TREESPRO/problems/TREEPATHSUM) |

---

## Problem Statement

Given an undirected connected tree with $N$ nodes, numbered from $1$ to $N$, and rooted at node $1$, along with an integer $target\_sum$. \
Check if there exists a path from root to any leaf whose sum is equal to $target\_sum$. Path sum is the addition of the values of nodes which are in that particular path.

For example, if $target\_sum$ is 9, then in the following tree, there is a path $1 -> 2 -> 6$ whose sum is 9.

## Function Declaration

### Function Name

$solution$ – This function determines whether there exists a root-to-leaf path in the given tree such that the sum of node values along that path equals $target\_sum$.

### Parameters

* $n$: The number of nodes in the tree (nodes are numbered from 1 to n).
* $target\_sum$: The required sum of a valid root-to-leaf path.
* $adj$: An adjacency list representing the tree.

  * $adj[i]$ contains the list of nodes directly connected to node $i$.
  * The tree is undirected and rooted at node 1.

### Return Value

* Returns $true$ if there exists at least one path from the root (node 1) to any leaf such that the sum of node values in that path equals $target\_sum$.
* Returns $false$ otherwise.

## Constraints

- $1 \leq N \leq 100000$
- $1 \leq u_i, v_i \leq N$
- $1 \leq target\_sum \leq \frac{N(N+1)}{2}$

---

## Input Format

- The first line of the input contains two space separated integer $N$ and $target\_sum$ — the number of vertices and the target sum which needs to be checked.
- The next $N - 1$ lines describe the edges. The $i$-th of these $N - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

Output $YES$ if tree has root to leaf path sum equal to given $target\_sum$ or $NO$ otherwise.

---

## Examples

**Example 1**

**Input**

```text
7 9
1 2
1 4
2 5
2 3
2 6
4 7
```

**Output**

```text
YES
```

**Explanation**

Refer to the image provided above for explanations of this sample test.

**Example 2**

**Input**

```text
6 4
1 2
1 3
2 4
2 6
3 5
```

**Output**

```text
NO
```

**Explanation**

There is no path that can achieve this target sum.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** DFS

Problem :- Given an undirected connected tree with N nodes, numbered from 1 to N, and rooted at node 1, along with an integer targetSum, check if there exists a path from root to any leaf whose sum is equal to targetSum.

**Solution Approach:** This problem can be solved using simple dfs traversal of the given tree. As we start the dfs traversal from the root node, we keep track of current path sum, and as soon as we reach any leaf node (In a general tree, a node is considered a leaf node if it has no children, i.e., it is not a parent to any other nodes.), we check if the current path sum is equal to the given target sum or not. If the sum is equal to the given target sum then we update a boolean flag to true, which was initially set to false.

**Time Complexity:**

The DFS traversal visits each node and edge once, leading to a time complexity of O(N + E), where N is the number of nodes and E is the number of edges (= N - 1, in case of tree). Hence the overall time complexity is O(N).

**Space Complexity:**

The space complexity is O(N) for storing the adjacency list and recursion stack during DFS.

</details>
