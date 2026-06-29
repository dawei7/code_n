# Minimum Depth of Binary Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTMINDEPTH |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [BTMINDEPTH](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/BTMINDEPTH) |

---

## Problem Statement

Given a binary tree, print its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

For example, the minimum depth of the following binary tree is: 2

![BTMINDEPTH](https://cdn.codechef.com/images/learning/graphs-trees/leve-order-traversal.png)

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on the single line - the minimum depth of the given binary tree.

---

## Constraints

- $1 \leq N \leq 10000$
- $1 \leq p_i, c_i \leq 100000$
- $R_i$ = `L` or `R`
- All $p_i$'s and $c_i$'s are distinct.

---

## Examples

**Example 1**

**Input**

```text
5
1 2 L
1 3 R
3 4 L
3 5 R
```

**Output**

```text
2
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Binary trees, binary tree traversal.

**Problem:** Given a binary tree, print its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Solution Approach:**

Basically we need node count from root to lowest hanging leaf. How to get that?

Just traverse down the tree in a similar to postorder manner and whenever we encounter a leaf return 1. While coming up at the root from left and right subtrees, take 1 + the minimum depth found from both the left and right subtrees. That’s it.

**Time complexity:** O(N), as we need to visit each node at most twice.

**Space complexity:** O(1), as no extra containers/variables are required.

</details>
