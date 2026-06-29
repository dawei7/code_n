# Mirror Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MIRRORTREE |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [MIRRORTREE](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/MIRRORTREE) |

---

## Problem Statement

Given a binary tree, check whether it is a structural mirror of itself (i.e., structurally symmetric around its center).

For example, the following binary tree is structurally symmetric:

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on the single line, `YES` if the given binary tree is structurally symmetric to itself, `NO` otherwise.

---

## Constraints

- $1 \leq N \leq 10000$
- $1 \leq p_i, c_i \leq 100000$
- $R_i$ = `L` or `R`
- All $p_i$'s and $c_i$'s are distinct.( No same pairs are given twice)

---

## Examples

**Example 1**

**Input**

```text
7
1 2 L
1 3 R
3 4 L
3 5 R
2 6 R
2 7 L
```

**Output**

```text
YES
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Binary tree, BT traversal.

**Problem:** Given a binary tree, check whether it is a structural mirror of itself (i.e., structurally symmetric around its center).

**Solution Approach:** Similar to Identical trees problem, this one can also be solved using a recursive approach to check if a binary tree is a structural mirror of itself. Two nodes are considered symmetric if their subtrees are symmetric. The algorithm recursively compares corresponding nodes in the left and right subtrees.

*Algorithm:*

-

- Implement a recursive function *isMirror()* that checks if two nodes are symmetric.

- If both nodes are NULL, they are symmetric (base case).

- If only one of the nodes is NULL, they are not symmetric.

- If both nodes are non-NULL, check if their left and right subtrees are symmetric recursively.

- If the values are equal and both subtrees are symmetric, return true; otherwise, return false.

-

- In the main function *isMirrorTree()*, call *isMirror()* with the root of the binary tree.

-

- Print “YES” if the tree is a structural mirror and “NO” otherwise.

**Time Complexity:** O(N), as we need to traverse each node at least once.

**Space Complexity:** O(1), as we don’t need any extra space.

</details>
