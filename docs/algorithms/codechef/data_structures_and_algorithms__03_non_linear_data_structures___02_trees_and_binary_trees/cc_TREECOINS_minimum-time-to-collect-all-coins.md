# Minimum time to collect all coins

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TREECOINS |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [TREECOINS](https://www.codechef.com/learn/course/trees/TREESPRO/problems/TREECOINS) |

---

## Problem Statement

Given an undirected connected tree with **N** nodes, numbered from **1** to **N**, and rooted at node **1**. Some of the nodes has gold coins in it. It takes 1 minute to walk over one edge of the tree. Determine the minimum time in minutes you have to spend to collect all coins in the tree, starting at root node $1$ and coming back to it.

For example, in the following tree, it will take 8 minutes to collect the gold coins from node 3, 4 and 5.

![Minimum time](https://cdn.codechef.com/images/learning/graphs-trees/coins-in-tree.png)

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes.
- The second line contains $N$ space separated integers $C_i$ ($1$ if there is gold coin at node $i$, else $0$).
- The next $N - 1$ lines describe the edges. The $i$-th of these $N - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

- Output on the single line, the minimum time it will take to collect all gold coins if you start from root node $1$ and return back to it.

---

## Constraints

- $1 \leq N \leq 100000$
- $1 \leq u_i, v_i \leq N$
- $0 \leq C_i \leq 1$

---

## Examples

**Example 1**

**Input**

```text
7
0 0 1 1 1 0 0
1 2
1 3
2 4
2 5
3 6
3 7
```

**Output**

```text
8
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** DFS

**Problem :-** Given an undirected connected tree with N nodes, numbered from 1 to N, and rooted at node 1. Some of the nodes have gold coins in them. It takes 1 minute to walk over one edge of the tree. Determine the minimum time in minutes you have to spend to collect all coins in the tree, starting at root node 1 and coming back to it.

**Solution Approach:**

The solution uses a depth-first search to traverse the tree, keeping track of the time spent to collect all the coins.

Let’s break down the algorithm step by step:

*DFS Function:*

-

The DFS function recursively visits each node and has a boolean array indicating whether each vertex has a coin.

-

It initializes a variable ans to 0, representing the time spent at the current node.

-

Traversal of Children:

- The DFS function is called recursively on that child to get the coins from the children

-

Time Calculation:

- The result (res) from the recursive call represents the time spent at the child node and its subtree.

- If res is greater than 0 or the current child has a coin, it adds (res + 2) to ans. The additional 2 seconds account for 1 second to go to the child and 1 second to return.

-

Return Result:

- The function returns the total time spent (ans) at the current node and its subtree.

**Time Complexity:** O(N + E) = O(N), where N is the number of nodes and E is the no. of edges in the tree. This runtime is due to the dfs traversal.

**Space Complexity:** O(1), as the algorithm doesn’t use extra space.

</details>
