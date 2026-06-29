# Sum of deepest leaves

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTDLSUM |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [BTDLSUM](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/BTDLSUM) |

---

## Problem Statement

Given a binary tree, find the sum of leaves at deepest level.

For example, in the following tree, leaves $4$ and $5$ are the the deepest level and their sum is $9$.

![BTDLSUM](https://cdn.codechef.com/images/learning/graphs-trees/leve-order-traversal.png)

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on the single line, the sum of leaves at the deepest level.

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
9
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Binary trees, Binary tree traversal.

**Problem:** Given a binary tree, find the sum of leaves at deepest level.

**Solution Approach:** A simple preorder traversal can be used to solve this problem. This idea is to visit the tree downwards while keeping track of level, *maxlevel* and *sum_at_deepest_level*. Whenever we find a level deeper than current *maxlevel*, we update the *sum_at_deepest_level* with node value at this level otherwise if the current level is equal to *maxlevel*, we add the current node’s value to *sum_at_deepest_level*.

Finally, *sum_at_deepest_level* will have a sum of nodes’ values which are at the deepest level.

**Time Complexity:** O(N) as we need to explore each node at least once.

**Space complexity:** O(1), as we don’t need any significant extra space.

</details>
