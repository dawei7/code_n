# Sort three integer

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO12 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SESO12](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH3/problems/SESO12) |

---

## Problem Statement

You are tasked with sorting a 3-integer array manually, without using any built-in sorting functions or libraries. Implement a program that reads three integers from input and rearranges them in ascending order.

### Input Format:

- Three integers separated by spaces on a single line.

### Output Format:

- Print the three integers in ascending order, separated by spaces.

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
5 2 7
```

**Output**

```text
2 5 7
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH3/problems/SESO12)

#### [](#problem-statement-1)Problem Statement

You are given a task to sort three integers in ascending order without using any built-in sorting functions or libraries. The goal is to implement a program that reads three integers from the input and rearranges them such that they are sorted in non-decreasing order.

#### [](#approach-2)Approach

To manually sort three integers, we can use a series of conditional checks and swaps. First, compare the first two integers and swap them if the first is greater than the second, ensuring the smaller value is in the first position. Next, compare the first integer with the third, and swap if necessary to place the smallest value in the first position. Finally, compare the second and third integers, swapping if the second is greater than the third, which ensures the integers are sorted in ascending order. This approach efficiently sorts the three integers using a minimal number of comparisons and swaps.

#### [](#complexity-analysis-3)Complexity Analysis

- **Time Complexity**: The time complexity of this solution is O(1) because the number of operations is constant, regardless of the values of the integers.

- **Space Complexity**: The space complexity is O(1) as no additional space is used besides the input variables and a few temporary variables during swapping.

</details>
