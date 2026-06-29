# Suffix Arrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREFPRO5 |
| Difficulty Rating | 1200 |
| Difficulty Band | Prefix Sum Problems |
| Path | Data Structures and Algorithms |
| Lesson | Prefix and Suffix Sum |
| Official Link | [PREFPRO5](https://www.codechef.com/practice/course/prefix-sums/PREFIXSUMS/problems/PREFPRO5) |

---

## Problem Statement

A suffix array is similar to prefix array. The only difference is that a suffix array works from right to left, while a prefix array works from left to right.

Suffix array of [1, 2, 3, 4, 5] -> [15, 14, 12, 9, 5]

We generally use prefix/suffix arrays to store the sum, but we can also use them to store some other operations like multiplication, GCD, OR, XOR, etc.

Some algorithms required us to use both prefix and suffix operations of different types together.

### Problem
- First line contains an integer $N$, the length of an array.
- Second line contains $N$ elements A1, A2, A3, . . . A$N$
- Find the maximum GCD that can be obtained by removing one element from the array.

---

## Input Format

- The first line of input will contain a single integer $N$, denoting the length of an array.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of vertices and edges of the graph, respectively.
    - The next $M$ lines describe the edges. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting an edge between $u_i$ and $v_i$.

---

## Output Format

For each test case, output on a new line the number of good subgraphs of $G$, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq N \leq 100000$
- $1 \leq Ai \leq 100000$

---

## Examples

**Example 1**

**Input**

```text
4
4 3 2 6
```

**Output**

```text
2
```
