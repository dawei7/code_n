# Distinct colors in subtrees

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TREECOLOR |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [TREECOLOR](https://www.codechef.com/learn/course/trees/TREESPRO/problems/TREECOLOR) |

---

## Problem Statement

Given an undirected connected tree with $N$ coloured nodes (colours denoted with integers $1$ to $N$), numbered from $1$ to $N$, and rooted at node $1$. Your task is to determine, for each node, the number of distinct colours present in its subtree.

For example, a subtree rooted at a specific node might contain several nodes with duplicate colors. You must count only the unique colors present in that entire subtree (including the root of that subtree).

![Subtree Colors](https://cdn.codechef.com/images/learning/graphs-trees/colored-tree.png)

---

## Function Declaration

### Function Name
$distinctColorsInSubtrees$ – This function computes the number of distinct colors in the subtree of every node in the given tree.

### Parameters

* $N$ : An integer representing the total number of nodes in the tree.
* $C$ : A list/array of integers of length $N$, where $C[i]$ represents the color of the $(i+1)^{th}$ node (assuming 0-indexed arrays for colors and 1-indexed nodes).
* $edges$ : A 2D list/array of size $(N-1) \times 2$ representing the undirected edges of the tree, where each pair $(u, v)$ indicates an edge between node $u$ and node $v$.

### Return Value

Returns a list/array of integers of length $N$: The $i^{th}$ element in the returned array should represent the total number of distinct colors in the subtree rooted at node $i+1$.

---

### Constraints:
* $1 \leq N \leq 10^5$
* $1 \leq C[i] \leq N$ for each $0 \leq i < N$
* $1 \leq u, v \leq N$
* The given edges are guaranteed to form a valid connected tree.
* The sum of $N$ over all test cases won't exceed $5 \cdot 10^5$.

**The input and output formats provided below are only for testing with custom inputs. You only need to return the value. Printing is handled automatically**

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes.
- The second line contains $N$ space separated integers $C_i$ - the colour of ith node.
- The next $N - 1$ lines describe the edges. The $i$-th of these $N - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

- Output on the single line, $N$ space separated integers, the no. of distinct coloured nodes in the subtree of node $i$ ($1 \leq i \leq N$).

---

## Constraints

- $1 \leq N \leq 100000$
- $1 \leq u_i, v_i \leq N$
- $1 \leq C_i \leq N$

---

## Examples

**Example 1**

**Input**

```text
7
1 2 3 4 3 4 5
1 2
1 7
1 5
2 4
2 3
5 6
```

**Output**

```text
5 3 1 1 2 1 1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** DFS

**Problem :-** Given an undirected connected tree with N coloured nodes (colors denoted with integers 1 to N), numbered from 1 to N, and rooted at node 1, determine for each node the number of distinct colors in the subtree of the node.

**Solution Approach:**

The solution uses Depth-First Search (DFS) to efficiently traverse the tree and maintain a set of distinct colors for each node.

Let’s take a look at the the approach, step by step:

- DFS Traversal:

- Start a DFS traversal from the root node (node 1).

- During the traversal, maintain a set of distinct colors for each node, representing the colors in its subtree.

- Set Operations:

- As the DFS progresses from parent to child nodes, update the set of distinct colors for each node.

- Combine the sets of distinct colors from child nodes with the set of the current node. The main concept is to swap the large and small set and merge the small set to large set always, thus reducing the time complexity by a huge margin.

**Time Complexity:** O(NlogN + E) = O(NlogN), where N is the number of nodes and E is the no. of edges in the tree. The extra logN factor comes from the set insertion and merging.

**Space Complexity:** O(N), as the algorithm uses a set and few arrays to store the colors and results.

</details>
