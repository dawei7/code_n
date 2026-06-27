# Subtree Inversion Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3544 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Tree, Depth-First Search |
| Official Link | [subtree-inversion-sum](https://leetcode.com/problems/subtree-inversion-sum/) |

## Problem Description & Examples
### Goal
Given a tree where each node contains a value, calculate the total number of inversions across all possible subtrees. An inversion in a subtree is defined as a pair of nodes $(u, v)$ within that subtree such that $u$ is an ancestor of $v$ (or vice versa) and their values satisfy a specific ordering condition (typically $val[u] > val[v]$). The goal is to return the sum of these inversion counts for every node considered as the root of a subtree.

### Function Contract
**Inputs**

- `n`: An integer representing the number of nodes in the tree.
- `edges`: A list of lists where each inner list `[u, v]` represents an undirected edge between nodes.
- `values`: A list of integers where `values[i]` is the value associated with node `i`.

**Return value**

- A list of integers where the $i$-th element is the total number of inversions found within the subtree rooted at node $i$.

### Examples
**Example 1**

- Input: `n = 3, edges = [[0, 1], [1, 2]], values = [1, 2, 3]`
- Output: `[0, 0, 0]`

**Example 2**

- Input: `n = 3, edges = [[0, 1], [0, 2]], values = [3, 2, 1]`
- Output: `[2, 0, 0]`

**Example 3**

- Input: `n = 4, edges = [[0, 1], [1, 2], [2, 3]], values = [4, 3, 2, 1]`
- Output: `[6, 3, 1, 0]`

---

## Underlying Base Algorithm(s)
The problem is solved using a combination of **Depth-First Search (DFS)** for tree traversal and a **Fenwick Tree (Binary Indexed Tree)** or **Merge Sort** approach to count inversions efficiently. Since we need to calculate inversions for every subtree, we perform a post-order traversal. As we backtrack from children to parents, we merge the inversion counts and use the Fenwick Tree to count pairs $(u, v)$ where $u$ is in the current subtree and $v$ is a new node being added, maintaining $O(N \log N)$ complexity.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N)$, where $N$ is the number of nodes. Each node is processed, and Fenwick Tree operations take logarithmic time.
- **Space Complexity**: $O(N)$, required for the adjacency list, the recursion stack, and the Fenwick Tree storage.
