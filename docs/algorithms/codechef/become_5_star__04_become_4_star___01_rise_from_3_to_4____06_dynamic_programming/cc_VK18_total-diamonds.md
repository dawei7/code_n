# Total Diamonds

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VK18 |
| Difficulty Rating | 1786 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [VK18](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/VK18) |

---

## Problem Statement

Chef is so good at programming that he won almost all competitions. With all the prizes, Chef bought a new house. The house looks like a grid of size **N** (1-indexed) which consists of **N** × **N** rooms containing diamonds. For each room, the room number is equal to the sum of the row number and the column number.

The number of diamonds present in each room is equal to the absolute difference between the sum of even digits and sum of odd digits in its room number. For example, if the room number is 3216, then the number of diamonds present in that room will be |(2+6)-(3+1)| = 4.

You are given the number **N**. You have to print the total number of diamonds present in Chef's house.

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The only line of each test case contains a single integer **N**.

### Output

For each test case, print the answer on a separate line.

### Constraints

- 1 ≤ **T** ≤ 105

- 1 ≤ **N** ≤ 106

### Subtasks

**Subtask #1 (15 points):**

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 1000

**Subtask #2 (15 points):**

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 106

**Subtask #3 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
1
2
3
```

**Output**

```text
2
12
36
```

**Explanation**

**Example case 3:** There are 9 rooms. Room (1,1) has number 2, room (1,2) has number 3, etc. For each room, the number of diamonds in it is equal to the room number, so the total number of diamonds present is (2+3+4+3+4+5+4+5+6) = 36.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
12
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
36
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/VK18)

[Contest](http://www.codechef.com/DEC17/problems/VK18)

**Author:** [Hruday Pabbisetty](http://www.codechef.com/users/hruday968)

**Tester:** [Mugurel Ionut Andreica](http://www.codechef.com/users/mugurelionut)

**Editorialist:** [Kirill Gulin](http://www.codechef.com/users/kefaa)

### PROBLEM

For each cell (i,j) of the N \times N grid define its value as the absolute difference between the sum of even digits and sum of odd digits in decimal representation of i+j. You are to find the total sum of cell values in the grid.

# QUICK EXPLANATION:

Precalculate answers for each N from 1 to 10^6 in ascending order for answering a query in O(1) time. For doing this find how the answer for matrix of order N - 1 differs from the answer for the matrix of order N.

# EXPLANATION:

Denote f(x) as the total number of diamonds in room with number x. It can be easily calculated in O(L) time by splitting x into digits, L is the length of x in decimal representation. Precalculate these values for each N from 1 to 2 \cdot 10^6 at the beginning. It requires O(NL) time.

## Subtask 1 solution.

Iterate over all rooms (i,j) (1 \leq i,j \leq N) in O(N^2) time and add f(i+j) to the answer.

Total time complexity: O(TN^2).

## Subtask 2 solution.

Notice there are O(N) different values of i+j in the N \times N grid. Indeed, if 1 \leq i \leq N and 1 \leq j \leq N then 2 \leq i + j \leq 2N and each x = i+j in range [2; 2N] can be reached. Moreover, any x occurs exactly min(x -1, 2N-x+1) times in the grid. To understand this write out room numbers as a grid and notice that the same x occurs only in diagonals parallel to the secondary diagonal of the grid. Here are room numbers of the 5\times5 grid:

\begin{matrix}
2&  3 & 4 & 5 & 6 \\
3&  4 & 5 & 6 & 7 \\
4&  5 & 6 & 7 & 8 \\
5&  6 & 7 & 8 & 9 \\
6 & 7 & 8 & 9 & 10
\end{matrix}

It’s easy to see the written above is true. So iterate through each x in range [2; 2N] and add f(x) \cdot min(x-1,2N-x-1) to the answer.

Total time complexity: O(TN).

## Subtask 3 solution.

Let’s find out how the answer for (N-1) \times (N-1) grid is different from the N \times N grid. Actually, N \times N grid fully contains the whole (N-1)\times(N-1) grid with one more row at the bottom and one more column at the right (the right-bottom cell exists in both this row and this column). Write out two grids of sizes N-1 and N for some N as above for a better understanding.

Go through each N from 1 to 10^6 in ascending order. Suppose now that for some N answers for each grid with less size has been already processed. A part of the current grid of size (N-1)\times(N-1) with left bottom cell is just the answer for the grid of size N-1. The last column cells have coordinates of the form (i,N) for each 1 \leq i \leq N. So the last column increases the answer for the current grid by f(1 + N) + f(2 + N) + … + f(N + N). Similarly, the last row cells have coordinates of the form (N, i) for each 1 \leq i \leq N and this row increases the answer by f(N + 1) + f(2 + N) + … + f(N + N). The right-bottom cell (N, N) is counted twice so the answer should be decreased by f(N + N). Easy to see the sums above are the same, so eventually the last row and column increase the answer by 2 \cdot (f(N+1)+f(N+2)+…+f(2N)) – f(2N). Still we need to find f(N+1) + f(N+2) + … + f(2N) fast since the naive summation has O(N) complexity.

We can use the fact that such sum can be easily recalculated for N+1 if we know it for N. Let’s just find the difference between them. Substituting N+1 instead of N in the sum above gives the sum f(N+2) + f(N+3) + … + f(2N) + f(2N+1) + f(2N+2). The difference is (f(N+2) + f(N+3) + … + f(2N) + f(2N+1) + f(2N+2)) – (f(N+1) + f(N+2) + … + f(2N)) = f(2N+1)+f(2N+2)-f(N+1). So we can maintain some variable S denoting f(N+1) + f(N+2) + … f(2N) for each N. Initially for N = 1 S = f(1 + 1) = 2. Then, for some N the answer for the appropriate grid is the answer for the grid of size N-1 increased by 2\cdot S - f(2N). For the next step S should be increased by f(2N+1)+f(2N+2)-f(N+1).

Total time complexity for precalculating the answers for each possible grid size is O(N) obviously, where N = 10^6. Answering a query takes O(1) time since all the answers are precalculated, hence the total time for queries is O(T).

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/DEC17/Setter/VK18.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/DEC17/Tester/VK18.cpp).

</details>
