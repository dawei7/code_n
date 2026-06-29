# Kth ancestor of the node

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KTHANCESTOR |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [KTHANCESTOR](https://www.codechef.com/learn/course/trees/TREESPRO/problems/KTHANCESTOR) |

---

## Problem Statement

Given an undirected connected tree with **n** nodes, numbered from **1** to **n**, and rooted at node **1**, and two positive integer $k$ and $v$, find the **$k^{th}$** ancestor (Ancestor at $k$ level up. Parent of a node is also an ancestor 1 level up) of the node $v$.

For example, in the following tree, the 2nd ancestor of node $7$ is node $1$.

![Kth Nodes](https://cdn.codechef.com/images/learning/graphs-trees/sample-tree.png)

## **Function Declaration**

### **Function Name**

$kthAncestor$ – Finds the $k^{th}$ ancestor of a given node in a tree.

### **Parameters**

* $n$ : An integer representing the number of nodes in the tree.
* $edges$ : A list of $n - 1$ edges where each edge $[u, v]$ denotes an undirected edge between nodes $u$ and $v$.
* $v$ : The node whose $k^{th}$ ancestor needs to be found.
* $k$ : The ancestor level to be queried.

### **Return Value**

* Returns an **integer** — the $k^{th}$ ancestor of node $v$.
* Returns $-1$ if the $k^{th}$ ancestor does not exist.

## Constraints:
- $1 \leq n \leq 100000$
- $1 \leq u_i, v_i \leq n$
- $1 \leq v \leq n$
- $1 \leq k \leq depth(v)$

**The input and output formats provided below are only for testing with custom inputs. You only need to return the value. Printing is handled automatically**

---

## Input Format

- The first line of the input contains three space separated integers $n$, $k$ and $v$ — the number of nodes, level up from node $v$ where we need to find the ancestor and the node $v$.
- The next $n - 1$ lines describe the edges. The $i$-th of these $n - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

- Output on the single line, the Kth ancestor of node $v$.

---

## Examples

**Example 1**

**Input**

```text
7 2 7
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

**Prerequisites:-** DFS on Trees, Binary Lifting.

**Problem :-** Given an undirected connected tree with N nodes, numbered from 1 to N, and rooted at node 1, and two positive integers K and v, find the Kth ancestor (Ancestor at K level up. Parent of a node is also an ancestor 1 level up) of the node v.

**Solution Approach:-** The approach utilizes Binary Lifting for efficient preprocessing. The algorithm performs a Depth-First Search (DFS) to calculate the ancestors of each node and then iteratively computes the  2^{j} th ancestor based on the 2^{j-1} th ancestor using dynamic programming. For each query, the function kth ancestor efficiently jumps the given node x to its K-th ancestor by leveraging the binary representation of K. The algorithm iterates through the bits of K and performs Binary Lifting jumps accordingly. This approach ensures a logarithmic time complexity for each query, making it suitable for scenarios where multiple K-th ancestor queries need to be answered in a connected tree.

**Time Complexity:**

- Preprocessing:

- The preprocessing step, which includes the DFS to calculate ancestors and Binary Lifting, takes O(NlogN) time, where N is the number of nodes in the tree.

- Query (Finding K-th Ancestor):

- Each query to find the K-th ancestor takes O(logK) time, where K is the specified level of the ancestor.

**Space Complexity:**

- The space complexity is O(NlogN) due to the storage of ancestor information.

</details>
