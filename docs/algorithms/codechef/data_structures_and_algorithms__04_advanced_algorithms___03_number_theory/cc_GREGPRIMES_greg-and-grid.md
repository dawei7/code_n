# Greg and Grid

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GREGPRIMES |
| Difficulty Rating | 1519 |
| Difficulty Band | Number theory |
| Path | Data Structures and Algorithms |
| Lesson | Sieve of Eratosthenes |
| Official Link | [GREGPRIMES](https://www.codechef.com/learn/course/number-theory/LINTDSA09/problems/GREGPRIMES) |

---

## Problem Statement

Recently, Greg got a grid with $n$ rows and $m$ columns. Rows are indexed from $1$ to $n$ and columns are indexed from $1$ to $m$. The cell $ ( i , j )$ is the cell of intersection of row $i$ and column $j$. Each cell has a number written on it. The number written on cell  $( i , j )$  is equal to  $(i+j)$.

Now, Greg wants to select some cells from the grid, such that for every pair of  selected cells ,the numbers on the cells are co-prime.  Determine the maximum number of cells that Greg can select.

---

## Input Format

- A single line containing the integers $n$ and $m$ denoting number of rows and number of columns respectively.

---

## Output Format

- Output a single line containing the answer.

---

## Constraints

- $1 \leq n,m \leq 10^{6}$

---

## Examples

**Example 1**

**Input**

```text
3 4
```

**Output**

```text
4
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Greg and Grid in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA09/problems/GREGPRIMES)

### [](#problem-statement-1)Problem Statement:

Recently, Greg got a grid with n rows and m columns. Rows are indexed from 1 to n and columns are indexed from 1 to m. The cell (i,j) is the cell of intersection of row i and column j. Each cell has a number written on it. The number written on cell (i,j) is equal to (i+j).

Now, Greg wants to select some cells from the grid, such that for every pair of selected cells, the numbers on the cells are co-prime. Determine the maximum number of cells that Greg can select.

### [](#approach-2)Approach:

- The function **SieveOfEratosthenes(int num)** computes the number of prime numbers less than or equal to num. This is useful because the maximum set of co-prime numbers that can be formed will be prime numbers.

- We will call the function for (n+m) as the maximum number that can be formed is n+m and count for total number of prime numbers.

- See for reference:- [Sieve of Eratosthenes in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA08/problems/SIEV00)

### [](#complexity-3)Complexity:

- **Time Complexity:** `O((n+m) log log (n+m))` for sieve of eratothenes.

- **Space Complexity:** `O(n)` to store prime array

</details>
