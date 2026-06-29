# Implementation - Adjacency Matrix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPP81 |
| Difficulty Rating | 932 |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [DSCPP81](https://www.codechef.com/learn/course/trees/TREES/problems/DSCPP81) |

---

## Problem Statement

In this section, we will check out how to implement the adjacency matrix we discussed.

img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

The code given on the right forms the adjacency matrix for the tree given above. Notice how the edges are taken as input and run the code to see the matrix.

---

## Input Format

- The first line of input will contain a single integer $N$, denoting the number of nodes in the Tree.
- Then the next N - 1 lines contains two numbers $u_i$ and $v_i$ denoting the i-th edge of the Tree.

---

## Output Format

Output the final adjacency matrix.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
6
0 1
0 2
1 3
1 4
2 5
```

**Output**

```text
0 1 1 0 0 0
0 0 0 1 1 0
0 0 0 0 0 1
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```
