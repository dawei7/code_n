# Strange Matrix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RRMATRIX |
| Difficulty Rating | 1922 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [RRMATRIX](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/RRMATRIX) |

---

## Problem Statement

Given two matrices **A** and **B**. Both have **N** rows and **M** columns. In the matrix **A**, numbers from **1** to **MN** have been written in row major order. Row major order numbers cells from left to right, and top to bottom. That is,

`
           1                  2                 3             ...     M
A  =    M+1             M+2            M+3        ...     2M
          2M+1           2M+2          2M+3       ...   3M
           .                   .                  .              ...      .
           .                   .                  .               ...      .
         (N-1)M+1    (N-1)M+2    (N-1)M+3   ...   NM
`

Similarly, in the matrix **B**, numbers from **1** to **MN** have been written in column major order. Column major order numbers cells from top to bottom and left to right.

You are to count number of pairs **(i,j)** such that **Ai,j=Bi,j**.

### Input
The input consists of multiple test cases. The first line of input contains a single integer **T**, the number of test cases. **T** test cases follow. Each test case is described by one line containing two space separated integers, **N** and **M**

### Output
Output **T** lines, ith line containing answer of the ith test case.

### Constraints
**
 1 ≤ T ≤ 105 1 ≤ N, M ≤ 109**

---

## Examples

**Example 1**

**Input**

```text
1
4 5
```

**Output**

```text
2
```

**Explanation**

For the first case two matrices look as follows:

**A**=

1 2 3 4 5

6 7 8 9 10

11 12 13 14 15

16 17 18 19 20
**B**=

1 5 9 13 17

2 6 10 14 18

3 7 11 15 19

4 8 12 16 20

**A1,1=B1,1**
**A4,5=B4,5**

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/RRMATRIX)

[Contest](http://www.codechef.com/COOK38/problems/RRMATRIX)

**Author**: [Roman Rubanenko](http://www.codechef.com/users/Rubanenko)

**Tester/Editorialist**: [Utkarsh Lath](http://www.codechef.com/users/utkarsh_lath)

# Difficulty:

Simple

# Pre-requisites:

High school maths

# Problem:

Given two matrices **A** and **B**, both of them having **N** rows and **M** columns. The cells of **A** are numbered in row major order, and cells of **B** are numbered in column major order. How many cells appears at the same location in both the orderings ?

# Explanation:

For **0 ? i < N, 0 ? j < M**, the (i,j)th entries are:

Ai, j = i * M + j + 1

Bi, j = j * N + i + 1

equating the two, we get

i * M + j + 1  = j * N + i + 1

? i * (M-1) = j * (N-1)

? i / j = (N-1) / (M-1) = p / q

? i = l * p, j = l * q  for 0 ? l ? min((N-1) / p, (M-1)/q)

where **p/q** is reduced form of **(N-1)/(M-1)**.

However, if **g** = gcd(**N-1**, **M-1**),

(**p**, **q**) = (**(N-1)/g**, **(M-1)/g**)

Therefore, (N-1) / p = (M-1) / q = g

and the cells which get same numbering are **(l * p, l * q)** for **0 ? l ? g**, which are **g+1** in number.

## Boundary cases

N = 1 or M = 1, in which case the answer is *max(**N, M**)*.

# Solutions:

[Setter’s solution](http://www.codechef.com/download/Solutions/COOK38/Setter/RRMATRIX.pas)

[Tester’s Solution](http://www.codechef.com/download/Solutions/COOK38/Tester/RRMATRIX.cpp)

</details>
