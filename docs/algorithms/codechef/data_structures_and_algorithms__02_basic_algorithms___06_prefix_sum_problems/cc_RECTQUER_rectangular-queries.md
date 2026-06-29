# Rectangular Queries

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECTQUER |
| Difficulty Rating | 1778 |
| Difficulty Band | Prefix Sum Problems |
| Path | Data Structures and Algorithms |
| Lesson | Prefix and Suffix Sum |
| Official Link | [RECTQUER](https://www.codechef.com/practice/course/prefix-sums/PREFIXSUMS/problems/RECTQUER) |

---

## Problem Statement

You are given a square matrix $A$ of size $N \times N$ (having $N$ rows and $N$ columns). **The values in the matrix are integers restricted to a small range, specifically $1 \le A_{i, j} \le 10$.**
Your task is to answer exactly $Q$ queries, where each query defines a rectangular submatrix.
The submatrix is specified by its upper-left corner $(X_1, Y_1)$ and its lower-right corner $(X_2, Y_2)$. For each query, you need to count the number of distinct elements present within this submatrix. That is, count the number of unique values of $A_{i, j}$ such that $X_1 \le i \le X_2$ and $Y_1 \le j \le Y_2$.

---

## Function Declaration

### Function Name
$countDistinctInSubmatrix$ – This function processes the matrix and returns the answers for all the given queries.

### Parameters

$N$ : An integer representing the number of rows and columns in the square matrix.
$A$ : A 2D array/vector of integers representing the matrix elements (1-indexed).
$Q$ : An integer representing the number of queries.
$queries$ : A 2D array/list of size $Q \times 4$, where each row contains four integers representing $X_1$, $Y_1$, $X_2$, and $Y_2$.

### Return Value

Returns an array/vector of exactly **$Q$ integers**, containing the count of distinct elements for each query in the same order they are given.

---

### Constraints:
* $1 \le N \le 300$
* $1 \le Q \le 10^5$
* $1 \le A_{i, j} \le 10$
* $1 \le X_1 \le X_2 \le N$
* $1 \le Y_1 \le Y_2 \le N$

*The input and output formats provided below are only for testing with custom inputs. You only need to return the expected array of integers. Printing is handled automatically by the platform.*

## Input Format
* The first line contains a single integer $N$.
* The next $N$ lines contain $N$ space-separated integers each, describing the matrix $A$. The rows are indexed $1$ to $N$ from top to bottom, and columns are indexed $1$ to $N$ from left to right.
* The next line contains a single integer $Q$, the number of queries.
* The next $Q$ lines each contain four space-separated integers representing $X_1$, $Y_1$, $X_2$, and $Y_2$.

## Output Format
* Output $Q$ integers, each on a separate line, representing the answers to the respective queries.

---

## Examples

**Example 1**

**Input**

```text
3
1 2 3
3 2 1
5 6 3
3
1 1 2 3
2 2 2 2
1 1 3 3
```

**Output**

```text
3
1
5
```

**Explanation**

There are 3 queries.
#### Query 1: `(1, 1, 2, 3)`
The selected submatrix is:
1 2 3
3 2 1
The distinct elements are `{1, 2, 3}`.
Hence, the answer is `3`.

#### Query 2: `(2, 2, 2, 2)`
The selected submatrix contains only the element:2
The distinct elements are `{2}`.
Hence, the answer is `1`.
#### Query 3: `(1, 1, 3, 3)`
The selected submatrix is the entire matrix:
1 2 3
3 2 1
5 6 3
The distinct elements are `{1, 2, 3, 5, 6}`.
Hence, the answer is `5`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/RECTQUER)

[Contest](http://www.codechef.com/DEC13/problems/RECTQUER)

**Author:** [Roman Rubanenko](http://www.codechef.com/users/Rubanenko)

**Tester:** [Gerald Agapov](http://www.codechef.com/users/gerald)

**Editorialist:** [Jingbo Shang](http://www.codechef.com/users/jingbo_adm)

### DIFFICULTY:

Easy

### PREREQUISITES:

Prefix sum

### PROBLEM:

Given a N*N matrix of at most 10 different numbers, answer Q queries about how many distinct numbers are there in a given sub matrix.

### EXPLANATION:

It is worth noting that there are at most 10 different numbers. Assume they are 1, 2, 3, … , 10.

To answer the number of distinct numbers, we can divide this problem to 10 separate problems:

``for d = 1 to 10:
    Is there any d in the sub matrix?
``

Let’s focus on a given number d. Then the matrix can be treated as binary, i.e. whether the entry equals d. Do the prefix sum for the binary matrix:

``S[i][j] = S[i-1][j] + S[i][j-1] – S[i-1][j-1] + Matrix[i][j]
``

With this O(N^2) preprocess, we can answer the problem “Is there any d in the sub matrix?” in O(1) time. That is,

``# of number d in (x1,y1)-(x2,y2) = S[x2][y2]–S[x2][y1-1]–S[x1-1][y2]+S[x1-1][y1-1]
``

Also, you can see the following figure for visualization. Denote the sum of red region as R, similar to Y(ellow), G(ray), B(lue).

Then we can have

``S[x2][y2] = R + B + G + Y
S[x2][y1-1] = G + B
S[x1-1][y2] = G + Y;
S[x1-1][y1-1] = G
Our goal is R.
``

Using this technique, it is easy to solve this problem in O(N^2 + Q * D). D is the different numbers in the matrix.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Solutions to be uploaded soon.

Author’s solution can be found here.

Tester’s solution can be found here.

</details>
