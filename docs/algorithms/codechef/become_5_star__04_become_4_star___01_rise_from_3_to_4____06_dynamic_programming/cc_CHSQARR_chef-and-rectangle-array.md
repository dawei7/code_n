# Chef and Rectangle Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHSQARR |
| Difficulty Rating | 2088 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [CHSQARR](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/CHSQARR) |

---

## Problem Statement

Chef has a two-dimensional matrix **A** of dimensions **N** × **M**, (**N** rows and **M** columns).

He calls the matrix **A** beautiful if there exist an **a**×**b** submatrix, such that all of its elements are equal. In one minute Chef can increase one element of the matrix **A** by 1. Now he asks you to find out minimum time he will need to make the matrix **A** beautiful?

Please note that sub-matrix of a matrix is a **continuous** rectangular block of the matrix. It can be denoted by two pair of indices **(x1, y1)** and **(x2, y2)** where **x1 ≤ x2**, **y1 ≤ y2**. The content of the submatrix will be all the cells **(i, j)** such that **x1 ≤ i ≤ x2** and **y1 ≤ j ≤ y2**.

### Input

- There is a single test case.

- The first line contains two space-separated integers **N**, **M** denoting the number of rows and columns in the matrix **A**, respectively

- Each of the next **N** lines, contains **M** space-separated integers denoting the **i**-th row of the array

- Next line contains one integer **Q** - amount of questions

- Each of next **Q** lines contains two space-separated integers **a** and **b** denoting sizes of submatrix sought.

- All questions are independent and do not influence each other. It means when you answer question, you don't need to change the array

### Output

- For each question, output a single line containing the minimum time that Chef needs to make an matrix **A** beautiful (for parameters **a** and **b** from question)

### Constraints

- **1** ≤ **Q** ≤ **50**

- **1** ≤ **N**, **M**, **Ai, j** ≤ **1000**

- **1** ≤ **a** ≤ **N**

- **1** ≤ **b** ≤ **M**

### Subtasks
**Subtask #1 (13 pts)**

- **1** ≤ **N**, **M** ≤ **50**

- TL = 1s

**Subtask #2 (35 pts)**

- **1** ≤ **N**, **M** ≤ **200**

- TL = 2s

**Subtask #3 (52 pts)**

- Original constraints

- TL = 4s

---

## Examples

**Example 1**

**Input**

```text
3 4
1 8 3 4
5 2 3 1
3 6 2 2
4
1 1
2 2
2 3
3 2
```

**Output**

```text
0
4
15
9
```

**Explanation**

**Question #1:**
Chef can choose any 1 × 1 submatrix and it will take his 0 minutes to make it beautiful.

**Question #2:**
The best variant is submatrix
`
3 1
2 2
`

**Question #3:**
The next submatrix Chef can make equal in 15 minutes
`
5 2 3
3 6 2
`

**Question #4:**
`
3 4
3 1
2 2
`

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/JUNE16/problems/CHSQARR)

[Practice](http://www.codechef.com/problems/CHSQARR)

**Author:** [Vasya Antoniuk](http://www.codechef.com/users/dpraveen)

**Testers:** [Istvan Nagy](http://www.codechef.com/users/iscsi)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

medium

### PREREQUISITES:

partial sums, dequeue, dynamic programming

### PROBLEM:

You are given 2-D matrix A[n][m]. The matrix will be called good if there exists a sub-matrix (continuous rectangular block of matrix) of dimensions a \times b whose all of its elements are equal. In a single operation, you can increase any element of the matrix by 1. Find out minimum number of operations required to make the matrix good.

### QUICK EXPLANATION:

For finding sum of a sub-matrix, you can use partial sums.

For finding maximum element in a sub-matrix, your can use doubly ended queue or deque.

### EXPLANATION:

Let us consider some a \times b dimension sub-matrix. Let x be the largest element in the sub-matrix. Let S be the total sum of elements in the sub-matrix. For making all the elements equal in minimum number of operations, we should aim to make all the elements equal to x. So, the minimum number of operations required will be x * n * m - S.

So, we have to find the sum and maximum element in all the possible sub-matrices of dimension a \times b.

For finding sum of all sub-matrices of sizes a \times b, we can use maintain partial sum sub-matrix. For that, we maintain another array, sum[n][m], where sum[i][j] will denote the sum of elements of the sub-matrix with left top end coordinate being (1, 1) and right bottom coordinate being (i, j). After computing sum matrix, we can find the sum of any sub-matrix.

Now let us learn about how to find maximum element in all sub-matrices of sizes a \times b.

Let maxCol[i][j] be the maximum element of the sub-matrix in the column starting at (i, j - b + 1) and ending at (i, j) (i.e. of column of length b).

Assume that we have computed maxCol array efficiently, let us find how we can use this to calculate maximum of a \times b sub-matrix.

Let max[i][j] denote the maximum value of sub-matrix of A ending at (i, j) (bottom right point), and of dimensions a \times b. Note that max[i][j] is maximum of maxCol[i - a + 1][j], maxCol[i - a + 2][j], \dots, maxCol[i][j].

Note that for calculating max[i][j + 1] from max[i][j], we have to add a new element maxCol[i][j + 1] and remove the element maxCol[i - a + 1][j].

That means, that we have to maintain maximum of a constant size subarray of an array, i.e. at each step, maintain maximum with inserting and deleting one element at each step. Note that we can compute maxCol in similar way.

This can be done either maintaining a multi-set (balanced binary search tree) of K elements, in which insertion/deletion and finding maximum can be done in \mathcal{O}(log(n)) time. Sadly this method is slower for passing largest subtask.

You can find a \mathcal{O}(n) solution for it by using doubly ended queue (aka deque). Please see this [link](http://www.geeksforgeeks.org/maximum-of-all-subarrays-of-size-k/) for its very detailed explanation.

### Time Complexity:

\mathcal{O}(n m) for finding both maxCol and max matrices.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter](http://www.codechef.com/download/Solutions/JUNE16/Setter/CHSQARR.cpp)

[Tester](http://www.codechef.com/download/Solutions/JUNE16/Tester/CHSQARR.cpp)

</details>
