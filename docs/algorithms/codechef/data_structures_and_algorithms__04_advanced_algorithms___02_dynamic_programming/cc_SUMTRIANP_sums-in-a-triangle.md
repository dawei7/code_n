# Sums in a Triangle

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUMTRIANP |
| Difficulty Rating | 869 |
| Difficulty Band | Dynamic programming |
| Path | Data Structures and Algorithms |
| Lesson | Different types of dynamic programming problems |
| Official Link | [SUMTRIANP](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA09/problems/SUMTRIANP) |

---

## Problem Statement

Given an integer $N$, let us consider a triangle of numbers of $N$ lines in which a number $a_{11}$ appears in the first line, two numbers $a_{21}$ and $a_{22}$ appear in the second line, three numbers $a_{31}$, $a_{32}$ and $a_{33}$ appear in the third line, etc. In general, $i$ numbers $a_{i1}, a_{i2} \dots a_{ii}$ appear in the $i^{th}$ line for all $1 \leq i \leq N$. Develop a program that will compute the largest of the sums of numbers that appear on the paths starting from the top towards the base, so that:
- on each path the next number is located on the row below, more precisely either directly below or below and one place to the right.

**Warning:** large Input/Output data, be careful with certain languages**

---

## Input Format

- The first line of the input contains an integer $T$, the number of test cases.
- Then T test cases follow. Each test case starts with an integer $N$, the number of rows. Then $N$ lines follow where in $i^{th}$ line contains $i$ integers $a_{i1}, a_{i2} \dots a_{ii}$.

---

## Output Format

For each test case print the maximum path sum in a separate line.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \lt 100$
- $0 \leq a_{ij} \lt 100$

---

## Examples

**Example 1**

**Input**

```text
2
3
1
2 1
1 2 3
4
1
1 2
4 1 2
2 3 1 1
```

**Output**

```text
5
9
```

**Explanation**

**Test case 1:**

There are a total of $4$ paths
- $(1,1) \rightarrow (2, 1) \rightarrow (3, 1)$ with sum equal to $4$.
- $(1,1) \rightarrow (2, 1) \rightarrow (3, 2)$ with sum equal to $5$.
- $(1,1) \rightarrow (2, 2) \rightarrow (3, 2)$ with sum equal to $4$.
- $(1,1) \rightarrow (2, 2) \rightarrow (3, 3)$ with sum equal to $5$.

Therefore, the maximum sum over all paths is equal to $5$.

**Test case 2:**

There are a total of $8$ paths
- $(1,1) \rightarrow (2, 1) \rightarrow (3, 1) \rightarrow (4, 1)$ with sum equal to $8$.
- $(1,1) \rightarrow (2, 1) \rightarrow (3, 1) \rightarrow (4, 2)$ with sum equal to $9$.
- $(1,1) \rightarrow (2, 1) \rightarrow (3, 2) \rightarrow (4, 2)$ with sum equal to $7$.
- $(1,1) \rightarrow (2, 1) \rightarrow (3, 2) \rightarrow (4, 3)$ with sum equal to $4$.
- $(1,1) \rightarrow (2, 2) \rightarrow (3, 2) \rightarrow (4, 2)$ with sum equal to $7$.
- $(1,1) \rightarrow (2, 2) \rightarrow (3, 2) \rightarrow (4, 3)$ with sum equal to $5$.
- $(1,1) \rightarrow (2, 2) \rightarrow (3, 3) \rightarrow (4, 3)$ with sum equal to $6$.
- $(1,1) \rightarrow (2, 2) \rightarrow (3, 3) \rightarrow (4, 4)$ with sum equal to $6$.

Therefore, the maximum sum over all paths is equal to $9$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Sums in a Triangle](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA09/problems/SUMTRIANP)

### [](#problem-statement-1)Problem Statement:

Given an integer `N`, we have a triangle of numbers where the first line contains one number, the second line contains two numbers, the third line contains three numbers, and so on, up to `N` lines. The goal is to compute the largest sum of numbers along paths starting from the top of the triangle to the base.

### [](#approach-2)Approach:

The key idea of this solution is to use dynamic programming to find the maximum path sum from the top of the triangle to the base. We maintain a 2D array, **DP**, where **DP[i][j]** represents the maximum sum that can be obtained when reaching the element in the `i-th` row and `j-th` column.

Here’s how the approach works:

-

**Filling the Triangle**: For each number in the triangle represented by `A[i][j]`:

-

If it’s the first number in a row (i.e., j=1), the maximum sum to reach this number is simply the number itself plus the sum from directly above it:

`DP[i][j]=A[i][j]+DP[i−1][j]`.

-

For all other numbers in that row, we calculate the maximum sum possible by taking the maximum of the two possible paths leading to it:

`DP[i][j]=A[i][j]+max⁡(DP[i−1][j−1],DP[i−1][j])`

This way, for each number in the current row, we consider the best path that could have led there.

-

**Finding the Maximum Path Sum**: Once we have filled in the **DP** table, the answer will be the maximum value in the last row of **DP**. This gives the largest sum of all possible paths from the top to the base of the triangle.

### [](#time-complexity-3)Time Complexity:

- The time complexity of the solution is `O(N^2)` because we need to fill in a triangle of size `N`.

### [](#space-complexity-4)Space Complexity:

- The space complexity is also `O(N^2)` due to the storage required for the **DP** array.

</details>
