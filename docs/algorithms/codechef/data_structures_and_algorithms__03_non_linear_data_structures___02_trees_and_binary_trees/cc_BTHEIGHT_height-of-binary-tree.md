# Height of Binary Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTHEIGHT |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [BTHEIGHT](https://www.codechef.com/learn/course/trees/BINARYTREES/problems/BTHEIGHT) |

---

## Problem Statement

Given a connected binary tree with **N** nodes, find the height of it. (**Note:** The height of a binary tree is the number of edges between the tree's root and its furthest leaf.)

For example, the following binary tree has height `2`:

![Height Balanced Tree](https://cdn.codechef.com/images/learning/graphs-trees/bt-height.png)

Hint: While traversing the Tree, you will have to store the height of children and use that to calculate the height of parent.

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on the single line, the height of the given binary tree.

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

**Prerequisites:** Binary Trees, Binary Trees Traversal Techniques.

**Problem:** Given a connected binary tree with N nodes, find the height of it.

(Note: The height of a binary tree is the number of edges between the tree’s root and its furthest leaf.)

**Solution Approach:**

We know that the height of a binary tree is the number of edges between the tree’s root and its furthest leaf.

Similarly, the depth of a binary tree is the number of nodes between the tree’s root and its furthest leaf.

So basically, height of the tree = max(0, depth of the tree - 1);

We can traverse the tree  down in a postorder manner and keep track of depth of the root,

Once we get the depth, return the height using the above equation.

It will become more clear once we take a look at the solution.

**Time Complexity:** O(N), as we need to traverse each node at least once.

**Space Complexity:** O(N) if we consider recursion space, as tree can be a linear chain in worst case.

</details>
