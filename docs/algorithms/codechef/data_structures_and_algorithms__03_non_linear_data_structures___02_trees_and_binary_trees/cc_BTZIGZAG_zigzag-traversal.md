# ZigZag Traversal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTZIGZAG |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [BTZIGZAG](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/BTZIGZAG) |

---

## Problem Statement

Given a binary tree, print the zigzag level order traversal of its nodes. (i.e., from left to right, then right to left for the next level and alternate between).

For example, the zigzag traversal of the following binary tree is: \
1 \
3 2 \
4 5

![BTZIGZAG](https://cdn.codechef.com/images/learning/graphs-trees/leve-order-traversal.png)

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on the L separate lines, $N$ space separated integers - its nodes in the zigzag level order traversal of the given tree, where L is total no. of levels in the given tree.

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
1
3 2
4 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Binary Trees, Level order traversal, Queue.

**Problem:** Given a binary tree, print the zigzag level order traversal of its nodes.

(i.e., from left to right, then right to left for the next level and alternate between).

**Solution Approach:**

Solution to this problem is almost the same as that of level order traversal with a minor tweak. We keep a queue data structure to visit nodes at each level one by one. One more boolean variable, let’s name it leftToRight, is needed to keep track of ordering while printing/storing nodes at each level. If leftToRight is set to true, the algorithm store/print nodes at current

level from left to right, else, right to left.

**Time Complexity:** O(N), as we need to visit each node once.

**Space Complexity:** O(N), as we need to store each node in the queue so that later its children can be visited in a zigzag manner.

</details>
