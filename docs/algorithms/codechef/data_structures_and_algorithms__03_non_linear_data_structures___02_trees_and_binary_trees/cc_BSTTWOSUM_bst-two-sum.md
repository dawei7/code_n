# BST Two Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BSTTWOSUM |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [BSTTWOSUM](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/BSTTWOSUM) |

---

## Problem Statement

Given a binary search tree and an integer $S$, check if there exist two elements in the BST such that their sum is equal to $S$.

For eg., in the following BST, for given S = 8, there exists few pairs of nodes whose sum is 8:

![BSTTWOSUM](https://cdn.codechef.com/images/learning/graphs-trees/bst-search.png)

---

## Input Format

- The first line of the input contains two space separated integers $N$ and $S$ — the number of nodes in the binary search tree, and the target sum.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Print `YES`, if there exists at least one such pair of nodes, whose sum is equal to $S$, else `NO`.

---

## Constraints

- $1 \leq N \leq 10000$
- $1 \leq p_i, c_i \leq 100000$
- $R_i$ = `L` or `R`
- All $p_i$'s and $c_i$'s are distinct.
- $1 \leq S \leq 150000$

---

## Examples

**Example 1**

**Input**

```text
50 106
7 2 L
7 10 R
11 7 L
11 27 R
27 24 L
35 11 L
35 38 R
37 36 L
38 37 L
38 40 R
40 39 L
50 35 L
50 87 R
61 58 L
61 67 R
70 61 L
70 81 R
81 80 L
87 70 L
87 94 R
92 89 L
94 92 L
94 97 R
97 96 L
100 50 L
100 153 R
104 102 L
104 107 R
108 104 L
108 112 R
112 110 L
113 108 L
113 126 R
123 114 L
126 123 L
126 137 R
137 132 L
153 113 L
153 187 R
174 163 L
180 174 L
180 186 R
186 184 L
187 180 L
187 191 R
190 188 L
191 190 L
191 199 R
199 196 L
```

**Output**

```text
YES
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Search Trees, BT traversals, HashSet/unordered_set.

**Problem :-** Given a binary search tree and an integer S, check if there exist two elements in the BST such that their sum is equal to S.

**Solution Approach :-** We can use Depth-First Search (DFS) approach to traverse the given BST while maintaining a HashSet/unordered_set to store the visited nodes. It checks whether there exist two elements in the BST such that their sum is equal to the given integer S.

*Algorithm:*

-

- Implement a DFS function that traverses the BST and checks for the existence of a pair with a given sum using an unordered_set.

-

- In the DFS function:

- If the current node is null, return false.

- If the complement of the current node’s value (i.e., S - current node’s value) exists in the HashSet, return true.

- Otherwise, insert the current node’s value into the HashSet.

- Recursively call the DFS function on the left and right subtrees.

-

- Initialize an empty HashSet and call the DFS function with the root of the BST.

-

- If the DFS function returns true, print “YES”; otherwise, print “NO”.

**Time Complexity:** O(N), because in the worst case, the algorithm visits all the nodes in the given BST.

**Space complexity:** O(N), as extra space is needed (unordered_set) to keep track of nodes’ values.

</details>
