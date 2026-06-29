# Matrix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATRIX2 |
| Difficulty Rating | 2209 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [MATRIX2](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/MATRIX2) |

---

## Problem Statement

You are given a matrix **A** that consists of **N** rows and **M** columns. Every number in the matrix is either zero or one. Calculate the number of such triples (**i**, **j**, **h**) where for all the pairs (**x**, **y**), where both **x** and **y** belong to [**1**; **h**] if **y >= x**, **A[i+x-1][j+y-1]** equals to one. Of course, the square (**i**, **j**, **i+h-1**, **j+h-1**) should be inside of this matrix. In other words, we're asking you to calculate the amount of square submatrices of a given matrix which have ones on and above their main diagonal.

### Input

The first line of the input consists of two integers - **N** and **M**.

The following **N** lines describe the matrix. Each line consists of **M** characters that are either zero or one.

### Output

Output should consist of a single integer - the answer to the problem.

### Example
`**Input:**
2 3
011
111

**Output:**
6
`

### Scoring
Subtask 1 (9 points): 1 <= **N,M** <= 2000, All the numbers in the matrix are equal to one.

Subtask 2 (12 points): 1 <= **N,M** <= 10.

Subtask 3 (34 points): 1 <= **N,M** <= 30.

Subtask 4 (17 points): 1 <= **N,M** <= 150.

Subtask 5 (28 points): 1 <= **N,M** <= 2000.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/MATRIX2)

[Contest](http://www.codechef.com/LTIME03/problems/MATRIX2)

# Difficulty:

Simple

# Pre-requisites:

DP

# Problem:

Calculate the amount of square submatrices of a given matrix which have ones on and above their **main diagonal**.

# Explanation:

## Sub task 1:

Even regardless the fact that the constraints are large, all the numbers are equal to one. Therefore, we just have to calculate the amount of square submatrices of the given matrix. To do that, we can brute force the size of the submatrix - let’s call this number **s** and add the product **(N-s+1) * (M-s+1)** - naturally, it’s the amount of possible **top left corners** for the submatrix of the size **s**, to the answer.

## Sub tasks 2, 3:

Even **O(N^5)** solution will do here. We can do a brute force for a **top left corner** and **the size of a submatrix**. It is already **O(N^3)**. Then, we just check the submatrix in **O(N^2)** time. Thus, we have obtained **O(N^5)** solution.

## Sub tasks 2, 3, 4:

There is also an **O(N^4)** solution. Again, let’s do a brute force for a **top left corner** and **the size of the submatrix**. And now we have to check whether the submatrix is good in any way with the complexity **O(N)**. Let’s notice that a good submatrix **C[][]** should contain ones in the **i**-th column at the positions [**1**; **i**] (we consider that the matrix is **1**-indexed). As it is a consecutive range of cells, we can use the standard approach to calculate the amount of ones in the rectangle. Generally, there will be **O(N)** such rectangles to check, so we have obtained the **O(N^4)** solution.

## All the sub tasks:

The model solution has **O(N^2)** complexity.

Observation: if the triple (**X**, **Y**, **s**) where (**X**, **Y**) describes the **top right cell** and **s** describes the **size of the submatrix** denotes a good square, then the triple (**X**, **Y**, **s-1**) also denotes a good square. Of course, now we consider the case when **s>1**. So, for every cell (**X**, **Y**) let’s calculate **F[X][Y]** - the maximal possible **s** where (**X**, **Y**, **s**) still denotes a good square. The answer to the problem, therefore, is the sum of all possible **F[X][Y]**.

How to calculate **F[][]** efficiently? Let’s denote the amount of the consecutive cells with ones right under the cell (**X**, **Y**) by **G[X][Y]**. Then, **F[X][Y]** equals to **min(F[X][Y-1]+1, G[X][Y])**. This can be explained. If we have a good matrix of the size **N**, it is impossible to obtain a good matrix of the size bigger than **N+1** by adding only a single column to it. It becomes obvious if we look at the figure that is formed by the cells that are on or above the main diagonal of the matrix. So, upper limit for the **F[X][Y]** is **F[X][Y-1]+1**. But it is not always possible to increase the size of the new matrix, because the last column of any good square submatrix should consist only of ones. So, if we don’t have enough ones below (**X**, **Y**), we just say that **F[X][Y]** equals to **G[X][Y]** - just the maximal possible submatrix that could end here. It is OK to consider it **G[X][Y]**, because in this case **G[X][Y] <= F[X][Y]** and as we mentioned earlier, if the triple (**X**, **Y**, **s**) where (**X**, **Y**) describes the **top right cell** and **s** describes the **size of the submatrix** denotes a good square, then the triple (**X**, **Y**, **s-1**) also denotes a good square.

# Setter’s solution:

Solution to sub tasks 2 and 3 can be found [here](http://www.codechef.com/download/Solutions/LTIME03/Setter/MATRIX2_GROUPS23.cpp).

Solution to sub tasks 2, 3 and 4 can be found [here](http://www.codechef.com/download/Solutions/LTIME03/Setter/MATRIX2_GROUPS234.cpp).

Solution to all the subtasks can be found [here](http://www.codechef.com/download/Solutions/LTIME03/Setter/MATRIX2_FULL.cpp).

# Tester’s solution:

Can be found [here](http://www.codechef.com/download/Solutions/LTIME03/Tester/MATRIX2.pas)

</details>
