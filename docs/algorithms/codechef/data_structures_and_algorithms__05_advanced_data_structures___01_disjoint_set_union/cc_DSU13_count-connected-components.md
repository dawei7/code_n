# Count Connected Components

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSU13 |
| Difficulty Band | Disjoint Set Union |
| Path | Data Structures and Algorithms |
| Lesson | DSU |
| Official Link | [DSU13](https://www.codechef.com/learn/course/dsu/LDSU02/problems/DSU13) |

---

## Problem Statement

Notice in the previous MCQ since each connected components have one leader, there will be as many connected components as there are leaders.
You are given $N$ nodes and $M$ connections. Output the total number of connected components.

---

## Input Format

- The first line of input contains two integers $N$ and $M$, denoting the number of nodes and the number of connections.
- Next M lines contain two integers a and b denoting that a is a connected to b.

---

## Output Format

For each test case, output the number of total connected components.

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
10 5
0 1
1 2
2 3
3 4
4 5
```

**Output**

```text
5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Count Connected Components](https://www.codechef.com/learn/course/dsu/LDSU02/problems/DSU13)

### [](#problem-statement-1)Problem Statement:

You are given **N nodes** and **M connections**. The task is to determine the total number of connected components in the graph formed by these nodes and connections. Each connected component has a unique leader, and thus the number of leaders will be equal to the number of connected components.

### [](#approach-2)Approach:

This solution employs the **Disjoint Set Union (DSU)**, or **Union-Find**, to efficiently manage connected components.

-

**Initialization**: Two arrays are used:

-

`parent[]`: Tracks the parent of each node, initialized so each node is its own parent.

-

`setSize[]`: Stores the size of each component, initialized to `1`.

-

**Finding Leaders**: The function `dsuFind(int a)` finds the leader of the component containing node `a`. If `a` is its own parent, it is the leader; otherwise, it recursively finds the leader with path compression.

-

**Union of Components**: The function `dsuUnion(int a, int b)` connects two nodes by merging their components. It attaches the smaller component to the larger to maintain balance.

-

**Counting Connected Components**: After processing connections, the program counts unique leaders by checking how many nodes are their own parents.

### [](#time-complexity-3)Time Complexity:

-

**Union and Find Operations**: Amortized **O(α(N))**, where `α` is the inverse Ackermann function, making these operations nearly constant.

-

**Counting Leaders**: **O(N)**, for a single pass through the nodes.

### [](#space-complexity-4)Space Complexity:

- **O(N)** for the `parent` and `setSize` arrays that store node information.

</details>
