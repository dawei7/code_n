# Identical Binary Trees

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | IDENTTREES |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [IDENTTREES](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/IDENTTREES) |

---

## Problem Statement

Given two undirected binary trees T1 and T2, check if they are the identical or not.

Two binary trees are considered identical if they are structurally same, and the nodes have the same value.

For example, the following two binary trees are identical:

![IdenticalTrees](https://cdn.codechef.com/images/learning/graphs-trees/identical-trees.png)

---

## Input Format

- The first line of the input contains two space separated integers $N$ and $M$ — the number of nodes in the two binary trees.
- Next $N - 1$ lines contain three space separated characters $p1_i, c1_i, R_i$, describing the first tree with edge informations - $p1_i$ is an integer denoting the parent node of the $i$th edge, $c1_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c1_i$ is left child of $p1_i$, else `R`.
- Similarly, next $M - 1$ lines contain three space separated characters $p2_i, c2_i, R_i$, describing the second tree with edge informations - $p2_i$ is an integer denoting the parent node of the $i$th edge, $c2_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c2_i$ is left child of $p2_i$, else `R`.

---

## Output Format

Output on the single line, `YES` if the two trees are identical else `NO` otherwise.

---

## Constraints

- $1 \leq N, M \leq 10000$
- $1 \leq p1_i, p2_i, c1_i, c2_i \leq 100000$
- $R_i$ = `L` or `R`
- All $p_i$'s and $c_i$'s are distinct.

---

## Examples

**Example 1**

**Input**

```text
5 5
1 2 L
1 3 R
3 4 L
3 5 R
1 2 L
1 3 R
3 4 L
3 5 R
```

**Output**

```text
YES
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Binary tree, BT traversal. .

**Problem:** Given two undirected binary trees **T1** and **T2**, check if they are the identical or not.

Two binary trees are considered identical if they are structurally the same, and the nodes have the same value.

**Solution Approach:** The problem can be solved using a recursive approach to check if two binary trees are identical. The primary idea is to compare the nodes of both trees at each level, ensuring that they have the same structure and values.

*Algorithm:*

-

- Implement a recursive function *isSameTree()* that checks if two nodes are identical.

- If both nodes are NULL, they are identical (base case).

- If only one of the nodes is NULL, they are not identical.

- If both nodes have values equal and their left and right subtrees are also identical, return true.

- Otherwise, return false.

-

- In the main function *isIdenticalTrees()*, call *isSameTree()* with the roots of the two trees.

-

- Print “YES” if the trees are identical and “NO” otherwise.

</details>
