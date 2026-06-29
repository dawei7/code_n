# Find Pairs Divisible Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO09 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Searching |
| Official Link | [SESO09](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH2/problems/SESO09) |

---

## Problem Statement

Write a program to find and print all pairs of integers from a list of **n** pairs where the sum of each pair is divisible by **k**.

The order of pairs in the output should be the same as the order in which they are provided in the input.
### Input Format

- The first line contains two integers **n** and **k**, where **n** is the number of pairs and **k** is the divisor.
- The next **n** lines each contain two integers, representing the pairs.

### Output Format
- Print each pair on a new line whose sum is divisible by **k**. Each pair should be printed in the format **(a, b)**.

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
3 5
1 4
2 5
6 4
```

**Output**

```text
(1, 4)
(6, 4)
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH2/problems/SESO09)

### [](#problem-explanation-1)Problem Explanation

The task is to find all pairs of integers from a list of `n` pairs where the sum of the elements in each pair is divisible by a given integer `k`. The order of pairs in the output should match the order in which they were provided in the input.

### [](#approach-2)Approach

To find and print all pairs of integers from a list where the sum of each pair is divisible by a given integer `k`, we first read the number of pairs `n` and the integer `k`, then store the pairs in a vector. We iterate through each pair, calculate the sum of the two integers, and check if the sum is divisible by `k`. If it is, we print the pair, ensuring that the output order matches the input order. This approach efficiently processes each pair in O(n) time.

### [](#complexity-analysis-3)Complexity Analysis

-

**Time Complexity**: The time complexity is O(n), where `n` is the number of pairs. This is because the program iterates through each pair once to check if the sum is divisible by `k`.

-

**Space Complexity**: The space complexity is O(n) due to the storage of the pairs in a vector, or if O(1) if we don’t consider the input storage space.

</details>
