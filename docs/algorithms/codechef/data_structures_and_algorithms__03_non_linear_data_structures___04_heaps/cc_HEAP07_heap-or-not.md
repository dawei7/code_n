# Heap or not

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HEAP07 |
| Difficulty Band | Heaps |
| Path | Data Structures and Algorithms |
| Lesson | Learn Heaps |
| Official Link | [HEAP07](https://www.codechef.com/learn/course/heaps/LIHP01/problems/HEAP07) |

---

## Problem Statement

Given an array check if it represents a min-heap or not.
Print "Yes" if it represents a min-heap. Otherwise, print "No".

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
2
7
10 15 30 40 50 100 40
3
15 10 18
```

**Output**

```text
Yes
No
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
10 15 30 40 50 100 40
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
3
15 10 18
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Heap or not](https://www.codechef.com/learn/course/heaps/LIHP01/problems/HEAP07)

### [](#problem-statement-1)Problem Statement -

Given an array check if it represents a `min-heap` or not. Print `Yes` if it represents a `min-heap`. Otherwise, print `No`.

### [](#approach-2)Approach:

The key idea of the solution is to verify if each node in the binary tree satisfies the **Max-Heap property** by comparing it with its left and right children. Here’s how the program works:

-

**Input Parsing**:

-

The program reads the number of test cases `t`.

-

For each test case, the size of the array `n` and the array elements are read.

-

**Logic for Checking Max-Heap**:

-

For each node at index `i`, the **left child** is located at index `2*i + 1` and the **right child** is located at index `2*i + 2`.

-

We check if the parent node (`arr[i]`) is greater than or equal to both of its children (if they exist).

-

If at any point a parent node is smaller than one of its children, the array does not satisfy the Max-Heap property, and we set `isHeap` to `false`.

-

**Result**:

- After checking all nodes, the program prints `Yes` if the array is a Max-Heap, otherwise it prints `No`.

### [](#time-complexity-3)Time Complexity:

- **O(n)**: We traverse each node and its children only once in a single loop.

### [](#space-complexity-4)Space Complexity:

- **O(n)**: We store the array of size `n` for each test case.

</details>
