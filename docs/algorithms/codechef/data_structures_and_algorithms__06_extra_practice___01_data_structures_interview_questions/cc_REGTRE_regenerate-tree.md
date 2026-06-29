# Regenerate Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REGTRE |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [REGTRE](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_07/problems/REGTRE) |

---

## Problem Statement

Regenerate binary tree with given inorder and post order traversal. You need to return the pointer to the root node of the tree generated.

A binary tree is a tree data structure in which every node has at most 2 children nodes.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each testcase contains single integer $N$ - number of nodes in Tree
- Second line contains n space-separated integers $In_1, In_2......In_i....In_N$ - In Order Traversal
- Third line contains n space separated integers $Post_1, Post_2......Post_i....Post_N$ - Post Order Traversal

All the values in In Order Traversal and Post Order Traversal are distinct.

**Note:**

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
Node* regeneratedTree(vector In, vector Post){...}

```

---

## Output Format

Using the functions you have completed, for each testcase pre order traversal of the tree will be compared for the correctness.
- For each testcase N space separated integers $Pre_1, Pre_2 ....... Pre_i ... Pre_N$ - Pre Order Traversal will be outputted.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq In_i \leq  N, In_i = In_j$ iff $i = j$
- $1 \leq Post_i \leq N, Post_i = Post_j$ iff $i = j$

Sum of $N$ over all test cases will not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
2
7
6 3 7 2 4 5 1
6 7 3 5 4 2 1
5
3 2 4 1 5
3 4 2 5 1
```

**Output**

```text
1 2 3 6 7 4 5
1 2 3 4 5
```

**Explanation**

**Testcase 1** : Following will be the regenerated tree
![](https://s3.amazonaws.com/codechef_shared/download/Images/Aman/REGTRE-2.jpeg =300x300)

**Testcase 2** : Following will be the regenerated tree
![](https://s3.amazonaws.com/codechef_shared/download/Images/Aman/REGTRE-1.jpeg =300x300)

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
6 3 7 2 4 5 1
6 7 3 5 4 2 1
```

**Output for this case**

```text
1 2 3 6 7 4 5
```



#### Test case 2

**Input for this case**

```text
5
3 2 4 1 5
3 4 2 5 1
```

**Output for this case**

```text
1 2 3 4 5
```


