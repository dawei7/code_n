# Chef and squares

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHSQR |
| Difficulty Rating | 1576 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [CHSQR](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/CHSQR) |

---

## Problem Statement

Chef has finished his freshman year in college. As a present, his parents gave him a new problem to solve:

Chef has to fill a **K x K** square grid of integers in a certain way. Let us say that such a grid is *valid* if:

- Each cell contains an integer from **1** and **K** (inclusive).

- No integer appears twice in the same row or the same column.

Let **F(K)** be maximum possible distance between the center of the square and the closest cell that contains **1**, among all possible squares with the side length **K**.

Here, we use the following notions:

-  The distance between cell **(x, y)** and **(i, j)** is equal to **|x-i|+|y-j|**.

-  The center of a **K x K** square is cell **((K+1)/2, (K+1)/2)** for odd **K**.

### Input

The first line of input contains a single integer **T** denoting the number of test cases.

Each test case consists of a single line containing a single odd integer **K**.

### Output
For each test case, print **K** lines each consisting of **K** space separated integers giving some square grid where the distance from the center of the grid to the nearest **1** is exactly **F(K)**. If there's more than 1 possible answer output any of them.

### Constraints

- **Ki** is odd.

**Subtask **#1** (10 points) ** :

-  **1** ≤ **T** ≤ **50**

-  **1** ≤ **Ki**≤ **5**

**Subtask **#1** (90 points) ** :

-  **1** ≤ **T** ≤ **10**

-  **1** ≤ **Ki** < **400**

---

## Examples

**Example 1**

**Input**

```text
2
1
3
```

**Output**

```text
1
3 2 1
1 3 2
2 1 3
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHSQR)

[Contest](http://www.codechef.com/NOV16/problems/CHSQR)

# DIFFICULTY:

Simple

# PREREQUISITES:

Basic programming skills

# PROBLEM:

Given an odd integer **K**, you are required to find a **K** * **K** matrix such that each cell has a value between 1 and **K** and no two cells on the same row or column have the same value, among all the ways you should choose the one in which the distance between the center cell and closest cell containing value 1 is maximum possible.

# EXPLANATION:

## prove that **F(K)** = (**K**-1)/2:

First, it’s easy to see that **F(K)** can’t be bigger than (**K**-1)/2 because let’s consider the row which contains the center cell, in this row we should choose exactly one cell to have a value 1, if we choose leftmost or rightmost cell then the distance from the center cell would be (**K**-1)/2 so  **F(K)** can’t be bigger than (**K**-1)/2.

now let’s prove that we can always find a matrix that satisfy **F(K)**=(**K**-1)/2, let’s fill the central row with values like this: 1 2 3 4 … **K**, and for each row below the central row we make it equal to the left shift of the row above it, and for each row above the central row we make it equal to the right shift of the row below it. in this way all cells which have value 1 will have at least (**K**-1)/2 distance from the center cell, and no two cells on the same row/column will have same value.

## example filling the matrix

let’s try an example of how to create the matrix with **K**=5

first of all, let’s fill the central matrix as we described below (1 2 3 4 5) so we have the matrix like this so far:

``* * * * *
* * * * *
1 2 3 4 5
* * * * *
* * * * *
``

after that, let’s fill the 4th row, it should be equal to the left shift of the central row so it’s (2 3 4 5 1), for the 5th row it’s again left shift of 4-th row so it’s (3 4 5 1 2) so the matrix so far is like this:

``* * * * *
* * * * *
1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
``

now for the rows above the central row, let’s start with 2nd row, it is right shift of central row so it’s (5 1 2 3 4) the 1st row is right shift of 2nd row so it’s (4 5 1 2 3)

so we have the final matrix like this:

``4 5 1 2 3
5 1 2 3 4
1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
``

## implementation details

We can follow the details step by step to obtain the matrix. however, if you write down the matrix for few sizes you will notices an interesting pattern, if we first decrease all values by 1 so that we deal with 0-based numbers we will notice the upper-left cell have value (**K**+1)/2, if the index of the row or the column is increased by 1 then the value will be increased by 1 (modulo **K**) so we can figure out an immediate formula for each cell based on the indices of its row and column, which is simply **mat[i][j]=((K+1)/2 + i + j) % K + 1**, note we added 1 in the end in order to return to 1-base.

so we can use 2 nested loops and then write the formula inside them

`
int main(){
	cin>>K;
	for(int i=0;i < K;i++){
		for(int j=0; j< K;j++){
			cout<< ((K+1)/2 + i + j) % K + 1<< " ";
		}
		cout<< endl;
	}
}`

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/NOV16/Setter/CHSQR.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/NOV16/Tester/CHSQR.cpp).

</details>
