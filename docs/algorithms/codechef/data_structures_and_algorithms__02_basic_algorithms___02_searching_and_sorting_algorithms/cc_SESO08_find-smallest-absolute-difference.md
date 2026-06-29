# Find Smallest Absolute Difference

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO08 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Searching |
| Official Link | [SESO08](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH2/problems/SESO08) |

---

## Problem Statement

Write a program to find the element in an array with the **smallest absolute difference** from a given integer **k**. If there are multiple elements with the same minimum difference, print the smallest of these elements.

### Input Format
- The first line contains two integers **n** and **k**, where **n** is the number of elements in the array and **k** is the integer against which to compare.
- The second line contains $n$  integers separated by spaces, representing the elements of the array.

### Output Format
- Print the element in the array with the smallest difference from k. If multiple elements have the same minimum difference, print the smallest of these elements.

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
5 10
1 5 9 12 14
```

**Output**

```text
9
```

**Example 2**

**Input**

```text
6 7
3 8 6 5 10 15
```

**Output**

```text
6
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH2/problems/SESO08)

### [](#problem-explanation-1)Problem Explanation

The task is to find the element in an array that has the smallest absolute difference from a given integer `k`. If there are multiple elements with the same minimum difference, the program should return the smallest of these elements.

### [](#approach-2)Approach

To find the element in an array with the smallest absolute difference from a given integer `k`, we iterate through the array while keeping track of the minimum absolute difference (`min_diff`) and the corresponding element (`result`). For each element in the array, we calculate its absolute difference from `k`. If this difference is smaller than `min_diff`, or if the difference is equal but the element is smaller than the current `result`, we update `min_diff` and `result` accordingly. After traversing the entire array, `result` will hold the element with the smallest absolute difference from `k`, ensuring that if multiple elements have the same difference, the smallest one is returned. This approach efficiently finds the desired element with a time complexity of O(n).

### [](#complexity-analysis-3)Complexity Analysis

-

**Time Complexity**: The time complexity of this solution is O(n), where `n` is the number of elements in the array. This is because the array is traversed only once.

-

**Space Complexity**: The space complexity is O(1), as the algorithm uses only a few extra variables (`min_diff` and `result`), regardless of the input size.

</details>
