# Boundary of the Binary Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTBOUNDARY |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [BTBOUNDARY](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/BTBOUNDARY) |

---

## Problem Statement

Given a binary tree, print the boundary nodes of it in an **Anti-Clockwise** direction, starting from the root. The boundary encompasses:

1. Left boundary (nodes on the left, excluding leaf nodes).
2. Leaves (comprising solely the leaf nodes).
3. Right boundary (nodes on the right, excluding leaf nodes).

For eg., in the above tree: \
**root:** 1 \
**left boundary nodes:** 2 \
**leaf nodes:** 6 8 4 5 \
**right boundary nodes:** 3 \
Hence the output should be: 1 2 6 8 4 5 3

![BTBOUNDARY](https://cdn.codechef.com/images/learning/graphs-trees/bt-boundary.png)

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Print on the single line, $K$ (if there are $K$ nodes in the tree's boundary) space separated nodes values - the boundary nodes of the given binary tree in an **Anti-Clockwise** direction

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
8
1 2 L
1 3 R
3 4 L
3 5 R
2 6 L
2 7 R
7 8 R
```

**Output**

```text
1 2 6 8 4 5 3
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Binary tree, BT traversal. .

**Problem:** Given a binary tree, print the boundary nodes of it in an Anti-Clockwise direction, starting from the root.

The boundary encompasses:

- Left boundary (nodes on the left, excluding leaf nodes).

- Leaves (comprising solely the leaf nodes).

- Right boundary (nodes on the right, excluding leaf nodes).

**Solution Approach:** We can use a four-step process to print the boundary nodes of the binary tree in an Anti-Clockwise direction:

- Print the Root:

- Print the value of the root node.

- Print the Left Boundary (Top-Down):

- Recursively print the left boundary nodes in a top-down manner.

- Print each node before calling itself for the left subtree.

- Avoid printing leaf nodes to prevent duplicates in the output.

- Print the Leaves:

- Recursively print the leaf nodes in both the left and right subtrees.

- Avoid printing duplicate leaf nodes.

- Print the Right Boundary (Bottom-Up):

- Recursively print the right boundary nodes in a bottom-up manner.

- Print each node after calling itself for the right subtree.

- Avoid printing leaf nodes to prevent duplicates in the output.

Take a look at the code to understand how we’re avoiding the duplication.

**Time Complexity:** O(N), as we need to visit each node once.

**Space Complexity:** O(1), as we don’t need any extra space.

</details>
