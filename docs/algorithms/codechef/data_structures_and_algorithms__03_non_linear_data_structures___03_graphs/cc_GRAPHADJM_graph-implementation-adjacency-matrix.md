# Graph Implementation - Adjacency Matrix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GRAPHADJM |
| Difficulty Rating | 932 |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Graphs |
| Official Link | [GRAPHADJM](https://www.codechef.com/learn/course/graphs/GRAPHREP/problems/GRAPHADJM) |

---

## Problem Statement

In this section, we will check out how to implement the adjacency matrix we discussed.

img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

The code given on the right forms the adjacency matrix for the graph given above. Notice how the edges are taken as input and run the code to see the matrix.

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the number of nodes and the edges in the graph.
- Then the next $M$ lines contains two numbers $u_i$ and $v_i$ denoting the i-th edge of the Graph.

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
4 5
1 2
2 3
3 4
1 4
1 3
```

**Output**

```text
0 1 1 1 
1 0 1 0 
1 1 0 1 
1 0 1 0
```
