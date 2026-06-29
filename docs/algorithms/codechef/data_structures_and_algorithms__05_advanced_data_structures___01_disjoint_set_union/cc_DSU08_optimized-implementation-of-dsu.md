# Optimized Implementation of DSU

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSU08 |
| Difficulty Band | Disjoint Set Union |
| Path | Data Structures and Algorithms |
| Lesson | DSU |
| Official Link | [DSU08](https://www.codechef.com/learn/course/dsu/LDSU01/problems/DSU08) |

---

## Problem Statement

Fill in the blanks to implement the optimizations in the previous lessons in the code editor.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of vertices and edges of the graph, respectively.
    - The next $M$ lines describe the edges. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting an edge between $u_i$ and $v_i$.

---

## Output Format

For each test case, output on a new line the number of good subgraphs of $G$, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
5 7
union 1 0
union 2 1
find 0
find 1
find 2
find 3
find 4
```

**Output**

```text
2
2
2
3
4
```
