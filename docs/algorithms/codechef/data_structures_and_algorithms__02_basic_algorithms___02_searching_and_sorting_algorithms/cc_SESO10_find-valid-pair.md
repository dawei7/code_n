# Find Valid Pair

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO10 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Searching |
| Official Link | [SESO10](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH2/problems/SESO10) |

---

## Problem Statement

Write a program that reads an integer **n** followed by **n pairs** of integers. Given two additional integers **left** and **right**, the program should print all pairs whose sum and product fall within the inclusive range **[left, right]**.

### Input Format
- The first line contains an integer n, representing the number of pairs.
- The next n lines each contain two integers, representing a pair of elements.
- The next line contains two integers left and right, defining the inclusive range for the sum and product of the pairs.
### Output Format
- Print each pair of integers **(a, b)** on a new line if both the **sum** and the **product** of **a** and **b** are within the range **[left, right]**.

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
3
1 2
2 3
4 5
3 15
```

**Output**

```text
2 3
```

**Explanation**

Evaluating each pair:

Pair (1, 2):

Sum: 1 + 2 = 3 (within range)

Product: 1 * 2 = 2 (not within range)

Pair (2, 3):

Sum: 2 + 3 = 5 (within range)

Product: 2 * 3 = 6 (within range)

Output: 2 3

Pair (4, 5):

Sum: 4 + 5 = 9 (within range)

Product: 4 * 5 = 20 (not within range)

**Example 2**

**Input**

```text
4
1 1
2 2
3 3
4 4
2 10
```

**Output**

```text
2 2
3 3
```

**Explanation**

Evaluating each pair:

Pair (1, 1):

Sum: 1 + 1 = 2 (within range)

Product: 1 * 1 = 1 (not within range)

Pair (2, 2):

Sum: 2 + 2 = 4 (within range)

Product: 2 * 2 = 4 (within range)

Pair (3, 3):

Sum: 3 + 3 = 6 (within range)

Product: 3 * 3 = 9 (within range)

Pair (4, 4):

Sum: 4 + 4 = 8 (within range)

Product: 4 * 4 = 16 (not within range)

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH2/problems/SESO10)

#### [](#problem-statement-1)Problem Statement

You are given an integer `n` followed by `n` pairs of integers. Additionally, two integers `left` and `right` are provided, representing an inclusive range `[left, right]`. The task is to print all pairs where both the sum and the product of the integers in each pair fall within the given range `[left, right]`.

#### [](#approach-2)Approach

To solve this problem, we first need to read and store the `n` pairs of integers. Then, for each pair, we calculate the sum and the product of the two integers. We check if both the sum and the product fall within the inclusive range `[left, right]`. If they do, we print the pair.

#### [](#complexity-analysis-3)Complexity Analysis

-

**Time Complexity**: The time complexity is O(n), where `n` is the number of pairs. This is because we iterate through the list of pairs once, performing constant-time operations (addition, multiplication, and comparisons) for each pair.

-

**Space Complexity**: The space complexity is O(n) due to the storage of the pairs in a vector. The additional space used by the program for storing variables is negligible (O(1)).

</details>
