# Naive DSU Implementation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSU05 |
| Difficulty Band | Disjoint Set Union |
| Path | Data Structures and Algorithms |
| Lesson | DSU |
| Official Link | [DSU05](https://www.codechef.com/learn/course/dsu/LDSU01/problems/DSU05) |

---

## Problem Statement

Implement the dsuFind and dsuUnion functions of DSU in the code editor.

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

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Naive DSU Implementation](https://www.codechef.com/learn/course/dsu/LDSU01/problems/DSU05)

### [](#problem-statement-1)Problem Statement -

Implement the dsuFind and dsuUnion functions of DSU in the code editor.

### [](#approach-2)Approach:

The key idea of this code is to utilize the **Disjoint Set Union (DSU)** or **Union-Find** data structure to efficiently handle a collection of disjoint (non-overlapping) sets. This structure supports two main operations:

#### [](#dsufindint-a-3)**`dsuFind(int a)`**:

-

If `parent[a]` equals `a`, it means that `a` is the leader of its set. Thus, the function returns `a`.

-

If `parent[a]` does not equal `a`, the function recursively calls itself with `parent[a]` until it finds the leader. This implements the **path compression** technique, making future queries faster by directly linking elements to their set leader.

#### [](#dsuunionint-a-int-b-4)**`dsuUnion(int a, int b)`**:

-

It first finds the leaders of both `a` and `b` by calling `dsuFind` on both.

-

If the leaders are different, it updates the parent of `leader_b` to be `leader_a`, effectively merging the two sets.

-

This operation ensures that all elements of one set now point to the leader of the other set.

### [](#time-complexity-5)Time Complexity:

-

**dsuFind**: **O(α(n))**, where `α` is the inverse Ackermann function. This function grows very slowly, so it is nearly constant time for practical purposes.

-

**dsuUnion**: **O(α(n))**, for the same reasons as above.

### [](#space-complexity-6)Space Complexity:

- **O(n)** for storing the parent array, where n is the number of elements.

</details>
