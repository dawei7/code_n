# Paths with given sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTPATHSUM |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [BTPATHSUM](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/BTPATHSUM) |

---

## Problem Statement

Given a binary tree and an integer **`target`**, retrieve all root-to-leaf paths where the sum of the node values along the path equals the given integer **`target`**. Print each such path on separate lines.

A root-to-leaf path signifies a path that initiates from the root and concludes at any leaf node. A leaf node is characterized as a node without any children.

For eg., in the given tree there is only one path with sum equals to 8 (1 - 3 - 4).

![BTPATHSUM](https://cdn.codechef.com/images/learning/graphs-trees/leve-order-traversal.png)

---

## Input Format

- The first line of the input contains two space separated integer $N$ and $target$ — the number of nodes in the binary tree and the desired path sum value.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on the $K$(if there are $K$ paths) separate lines, space separated integers - the nodes in paths whose sum is equal to $target$.

---

## Constraints

- $1 \leq N \leq 10000$
- $1 \leq target \leq 1000000000$
- $1 \leq p_i, c_i \leq 100000$
- $R_i$ = `L` or `R`
- All $p_i$'s and $c_i$'s are distinct.

---

## Examples

**Example 1**

**Input**

```text
5 8
1 2 L
1 3 R
3 4 L
3 5 R
```

**Output**

```text
1 3 4
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Trees, Tree traversal.

**Problem :-** Given a binary tree and an integer target, retrieve all root-to-leaf paths

where the sum of the node values along the path equals the given integer target.

Print each such path on separate lines.

A root-to-leaf path signifies a path that initiates from the root and concludes

at any leaf node. A leaf node is characterized as a node without any children.

**Solution Approach :-**

This can be solved by preorder traversal of the given tree. While going down the tree from root,

We keep track of each node and their sum and whenever we reach a leaf node, we check if the running path sum is equal to the target integer or not, if it’s equal, then we add this path to the result vector.

**Time complexity:** O(N), as we need to visit each nodes at least once.

**Space complexity:** O(N), as we need to store each node a couple of times while traversing the tree down.

</details>
