# Triplet LCA

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LCAN3 |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [LCAN3](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/LCAN3) |

---

## Problem Statement

You are given a binary tree and three nodes A, B and C. Find the lowest common ancestor of the three nodes.

- A binary tree is a tree data structure in which every node has at most 2 children nodes.
- Lowest common ancestor of node A, B and C  is defined as the lowest node in the tree such that subtree rooted at that node contains all the nodes A,B and C.
- A subtree of a tree T is a tree S consisting of a node in T and all of its descendants in T.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each testcase contains single integer $N$ - number of nodes in Tree
- Next n lines each contains 2 space separated integers $parent_i$ and $node_i$ denoting value of parent and node in the given tree.
  - Note that node with value 1 is the root node and its parent will be given as -1
- Last line of each testcase contains $node_a$, $node_b$ and $node_c$ denoting node values for Node A, B and C.

Following things are guaranteed :
- $node_a$, $node_b$ and $node_c$ are distinct and will be present in the tree.
- Resulting tree is a binary tree.

**Note:**

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
int  tripletLCA(Node* root,  int a, int b, int c){...}

```
$\ $

---

## Output Format

Using the functions you have completed, values returned will be checked for the correctness.
- For each testcase a single integer $LCA$ - least common ancestor will be outputted.

---

## Constraints

- $1 \leq T \leq 1000$
- $4 \leq N \leq 10^5$
- $1 \leq parent_i \leq N$ and $parent_j = -1$ iff $node_j = 1$
- $1 \leq node_i \leq N, node_i = node_j$ iff $i = j$
- $1 \leq node_a, node_b, node_c \leq N$

Sum of $N$ over all test cases will not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
2
7
1 2
2 3
3 6
3 7
2 4
4 5
-1 1
6 4 5
5
1 2
-1 1
2 3
2 4
1 5
2 3 4
```

**Output**

```text
2
2
```

**Explanation**

**Testcase 1** :

![](https://s3.amazonaws.com/codechef_shared/download/Images/Aman/testcase1.jpeg =300x300)

From the tree we can see that LCA of 6 4 5 is 2

**Testcase 2** :

![](https://s3.amazonaws.com/codechef_shared/download/Images/Aman/testcase2.jpeg =300x300)

From the tree we can see that LCA of 2 3 4 is 2

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
1 2
2 3
3 6
3 7
2 4
4 5
-1 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
6 4 5
5
1 2
-1 1
2 3
2 4
1 5
2 3 4
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Trees, LCA.

**Problem :-** Given a binary tree and three nodes A, B and C. Find the lowest common ancestor of the three nodes.

*Note:*

- A binary tree is a tree data structure in which every node has at most 2 children nodes.

- Lowest common ancestor of node A, B and C is defined as the lowest node in the tree such that subtree rooted at that node contains all the nodes A,B and C.

- A subtree of a tree T is a tree S consisting of a node in T and all of its descendants in T.

**Solution Approach:** The provided solution employs a recursive approach to find the LCA of a pair of nodes and then uses this result to find the LCA with the third node. The key function here is *findLCA()*, which recursively searches for the LCA of a set of nodes in the binary tree.

Let’s break-down the *findLCA()* function:

- The function takes the root of the binary tree and a set of nodes.

- It checks if the current node’s data is in the set. If yes, it returns the current node.

- It then recursively searches for the LCA in the left and right subtrees.

- If both left and right LCA are found, it means the current root is the LCA.

- It returns the non-null LCA (either left or right).

**Time Complexity :-** The time complexity of this solution is O(N), where N is the number of nodes in the binary tree. Each node is visited once during the traversal.

**Space Complexity :-** The space complexity is O(H), where H is the height of the binary tree. This space is used for the recursive call stack during the traversal. The additional space for the unordered set is O(1) since it has a constant number of elements (three nodes).

</details>
