# Optimization Using Prefix Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREFPRO2 |
| Difficulty Band | Prefix Sum Problems |
| Path | Data Structures and Algorithms |
| Lesson | Prefix and Suffix Sum |
| Official Link | [PREFPRO2](https://www.codechef.com/practice/course/prefix-sums/PREFIXSUMS/problems/PREFPRO2) |

---

## Problem Statement

Given an array of length $n$, we need to perform $m$ query over the array.

In each query you need to find the sum of the element in the range $a$ to $b$.

### Without using prefix sum

- For each query we need to iterate over the length of array, which will take $O(n)$ time.
- Total m query will make the time complexity $O(n*m)$

### Using prefix sum
- Create an prefix sum array in $O(n)$ time.
- For each query we can find the sum of a range in $O(1)$ time, using $prefix[b] - prefix[a-1]$ as the sum of range from $a$ to $b$
- Total $m$ query will make the time complexity $m * O(1) + O(n)$ => $O(m) + O(n)$

We can see above clearly how prefix sum help us to optimize the time complexity of our code.

### Task
Use the optimized algorithm to solve the problem.

---

## Input Format

- First line contains an integer $N$, the length of the array.
- Second line contains $N$ elements a1, a2, a3 . . . . ar$N$.
- Third line gives an integer $K$, the number of queries.
- Next $K$ line contains queries with integer a$i$ and b$i$.

---

## Output Format

For each test case, output on a new line the number of good subgraphs of $G$, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq N \leq 100000$
- $1 \leq arr_i \leq 100000$
- $1 \leq K \leq 100000$
- $1 \leq a_i, b_i \leq N$

---

## Examples

**Example 1**

**Input**

```text
5
1 2 3 4 5 
5
1 2
2 3
2 4
4 4
1 5
```

**Output**

```text
3
5
9
4
15
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [ Optimization Using Prefix Array](https://www.codechef.com/practice/course/prefix-sums/PREFIXSUMS/problems/PREFPRO2?tab=statement)

### [](#problem-statement-1)Problem Statement

Given an array of length `n`, we need to perform `m` query over the array.

In each query you need to find the sum of the element in the range `a` to `b`.

### [](#approach-2)Approach

The prefix sum technique preprocesses the array so that each element at index **i** in the **prefix_sum** array represents the sum of elements from the start to index **i**. For a query with range **a** to **b**, the sum is calculated as `prefix_sum[b] - prefix_sum[a-1]`, with special handling when **a = 0**.

### [](#time-complexity-3)Time Complexity:

The time complexity is O(n  \times m) because for each query, we might have to sum `n` elements in the worst case.

### [](#space-complexity-4)Space Complexity:

The space complexity is O(n) due to the storage of the array `v1`.

</details>
