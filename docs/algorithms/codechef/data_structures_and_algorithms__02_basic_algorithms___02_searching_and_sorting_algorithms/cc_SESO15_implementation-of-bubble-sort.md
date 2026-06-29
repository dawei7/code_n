# Implementation of Bubble Sort

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO15 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SESO15](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH4/problems/SESO15) |

---

## Problem Statement

Sorting the array [6,5,3,1] using bubble sort.

### Initial List
- [6,5,3,1]
### First Pass:
- Compare 6 and 5, swap -> [5,6,3,1]
- Compare 6 and 3, swap -> [5,3,6,1]
- Compare 6 and 1, swap -> [5,3,1,**6**]

### Second Pass
- Compare 5 and 3, swap -> [3,5,1,**6**]
- Compare 5 and 1, swap -> [3,1,**5**,**6**]

### Third Pass
- Compare 3 and 1, swap -> [**1**,**3**,**5**,**6**]

### The list is now sorted.
- [1,3,6,5]

## Task
- Given a program to sort using bubble sort.
- Analyze the code for bubble sort and **submit**.

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
6 5 3 1 8 7 2 4
```

**Output**

```text
1 2 3 4 5 6 7 8
```
