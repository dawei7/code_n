# LCA of two nodes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TREELCA |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [TREELCA](https://www.codechef.com/learn/course/trees/TREESPRO/problems/TREELCA) |

---

## Problem Statement

Given an undirected connected tree with **N** nodes, numbered from **1** to **N**, rooted at node **1**, and two nodes $u$ and $v$, find the lowest common ancestor (LCA) of it. (**Note:** The lowest common ancestor of two nodes $u$ and $v$ is the lowest node that has both $u$ and $v$ as its descendants)

For example, in the following tree, the LCA of nodes $3$ and $7$ is node $1$. Also the LCA of nodes $4$ and $7$ is $4$.

![Kth Nodes](https://cdn.codechef.com/images/learning/graphs-trees/sample-tree.png)

---

## Input Format

- The first line of the input contains three space separated integers $N$, $u$ and $v$ — the number of nodes, and two given nodes.
- The next $N - 1$ lines describe the edges. The $i$-th of these $N - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

- Output on the single line, the LCA of nodes $u$ and $v$.

---

## Constraints

- $1 \leq N \leq 100000$
- $1 \leq u_i, v_i \leq N$
- $1 \leq u, v \leq N$

---

## Examples

**Example 1**

**Input**

```text
7 3 7
1 2
1 4
2 5
2 3
2 6
4 7
```

**Output**

```text
1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** DFS, Binary Lifting

**Problem :-** Given an undirected connected tree with N nodes, numbered from 1 to N, rooted at node 1, and two nodes u and v, find the lowest common ancestor (LCA) of it. (Note: The lowest common ancestor of two nodes u and v is the lowest node that has both u and v as its descendants)

**Solution Approach:** This problem can be solved using depth first search along with the concept of binary lifting (a simple dynamic programming technique).

Let’s understand a few basic concepts first:

Let’s consider a general tree **T**. For each query like lca(u, v), we want to find the lowest common ancestor of nodes u and v. This means finding out a node w that exists on both the path from u to the root of the tree and the path from v to the root of the tree. If there are several possible w nodes, we choose the one that is farthest from the top of the tree. In simple terms, w is the lowest shared ancestor of both u and v. If u is already an ancestor of v, then u is the lowest common ancestor.

The binary lifting algorithm described here needs O(NlogN) for preprocessing the tree, and then O(logN) for each LCA query.

### [](#detailed-explanation-1)Detailed Explanation:

-

Ancestor Calculation:

- During the preprocessing step, the algorithm calculates ancestors using dynamic programming.

- For each node i,ancestor[i][j] is set to be the j-th ancestor of i if j-th ancestor exists.

- This is done iteratively, starting from i =1 to N, j =0 up to log⁡2(N).

-

Jumping Up the Tree:

- When comparing depths, if u is deeper, it iteratively jumps u to higher ancestors.

- The key insight is that the binary representation of the jump length helps efficiently traverse the tree. For example, jumping by 2^j is the same as using the j-th bit in the binary representation of the jump length.

- By using powers of 2, the algorithm efficiently moves u up the tree until it reaches the same depth as v.

-

Finding the Common Ancestor:

- Once u and v are at the same depth, the algorithm starts jumping them up simultaneously.

- At each step, if ancestor[u][j] is not equal to ancestor[v][j], it means u and v are not at their common ancestor yet.

- Jumping u and v to ancestor[u][j] and ancestor[v][j] respectively ensures they both get closer to their common ancestor.

### [](#why-it-works-2)Why It Works:

- Binary Lifting leverages the binary representation of numbers to efficiently move up the tree by powers of 2.

- By comparing the binary representations of the jump lengths, the algorithm ensures that both nodes u and v move towards their common ancestor.

- The common ancestor found using this method is the lowest common ancestor, as it is the farthest node from the root that both u and v share.

**Time Complexity:** O(NlogN), as for each node the we need to find the at most LogN ancestors during the preprocessing step.

**Space Complexity:** O(NLogN) as we need to store the LogN ancestors details for each of the N nodes.

</details>
