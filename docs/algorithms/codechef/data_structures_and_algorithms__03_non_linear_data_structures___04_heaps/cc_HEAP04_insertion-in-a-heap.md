# Insertion in a heap

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HEAP04 |
| Difficulty Band | Heaps |
| Path | Data Structures and Algorithms |
| Lesson | Learn Heaps |
| Official Link | [HEAP04](https://www.codechef.com/learn/course/heaps/LIHP01/problems/HEAP04) |

---

## Problem Statement

To insert an element in a heap:
- Insert it at the end of the heap
- Check if the element has less priority than it's parent or if it is the top-most element in the heap.
- If Yes, exit.
- If No, swap the element with the parent node and go back to step 2.

Check the insert function to see how to insert an element in the heap.

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
7
2 3 4 6 1 3 1
```

**Output**

```text
1 2 1 6 3 4 3
```
