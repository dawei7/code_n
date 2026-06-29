# Number of Rectangles

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NUMREC |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 1 |
| Official Link | [NUMREC](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/NUMREC) |

---

## Problem Statement

You are given a rectangular grid with $N$ rows and $M$ columns. A number $A_{i,j}$ is written in the cell belonging to the $i^{th}$ row and the $j^{th}$ column.
- $A_{i,j} = 1$, for all $1 \leq i \leq N$ and $1 \leq j \leq M$, except for $i = N$ and $j = M$.
- $A_{N, M} = 0$.

Find the number of sub-rectangular grids which contain only $1$s.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, two integers $N, M$.

---

## Output Format

For each testcase, print the number of sub-rectangular grids containing only $1$s.

---

## Constraints

- $1 \leq T \leq 50$
- $2 \leq N, M \leq 10^4$

---

## Examples

**Example 1**

**Input**

```text
2
2 2
4 5
```

**Output**

```text
5
130
```

**Explanation**

**Test case-1:** Consider the following rectangles :

- Rectangle made up of cell $(1,1)$.
- Rectangle made up of cell $(1,2)$.
- Rectangle made up of cell $(2,1)$.
- Rectangle made up of cells $(1,1)$ and $(1,2)$.
- Rectangle made up of cells $(1,1)$ and $(2,1)$.

Total $5$ sub-rectangles of given grid are made up of only $1$s.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
4 5
```

**Output for this case**

```text
130
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will solve the problem of counting sub-rectangular grids that contain only 1’s in an $N\times M$ grid, where every cell is $1$ except the cell at the bottom‐right corner $(N, M)$ which is $0$. We will explore two different approaches to solve this problem.

---

## Approach 1: Direct Mathematical Combinatorics (Total Minus Invalid)

### Explanation

1. **Total Rectangles:**
   In a grid of size $N\times M$, the total number of subrectangles can be computed by choosing two boundaries from the rows and two from the columns. This leads to:
   $$ Total = \frac{N(N+1)}{2} \times \frac{M(M+1)}{2} $$

2. **Rectangles including the cell $(N, M)$:**
   Any rectangle that includes the cell $(N, M)$ is invalid. A rectangle includes $(N, M)$ if its top-left corner is chosen from any of the cells in the first $N$ rows and first $M$ columns. Therefore, the number of rectangles containing $(N, M)$ is:
   $$ Invalid = N \times M $$

3. **Valid Rectangles:**
   Subtract the invalid rectangles from the total:
   $$ Answer = Total - Invalid $$

### Code Implementation

Below is the implementation of Approach 1 in both **C++** and **Python**.

#### C++ Code
```cpp
#include
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        long long N, M;
        cin >> N >> M;
        // Total subrectangles in an N x M grid
        long long totalRectangles = (N * (N + 1) / 2) * (M * (M + 1) / 2);
        // Rectangles that include the cell (N, M)
        long long invalidRectangles = N * M;
        // Result is the difference
        cout << totalRectangles - invalidRectangles << endl;
    }
    return 0;
}
```

#### Python Code
```python
def count_subrectangles(n, m):
    # Total subrectangles in an n x m grid
    total = (n * (n + 1) // 2) * (m * (m + 1) // 2)
    # Rectangles that include the cell (n, m)
    invalid = n * m
    return total - invalid

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(count_subrectangles(n, m))
```

---

## Approach 2: Inclusion-Exclusion of Regions

### Explanation

Another perspective is to count rectangles that are *certain* not to contain the $0$ in the bottom-right corner by dividing the grid into safe regions:

1. **Region A (Excluding the Last Column):**
   The grid consisting of all rows and columns $1$ to $M-1$ is guaranteed not to have the cell $(N, M)$. The number of rectangles in this region is:
   $$ A = \frac{N(N+1)}{2} \times \frac{(M-1)M}{2} $$

2. **Region B (Excluding the Last Row):**
   Similarly, the grid consisting of rows $1$ to $N-1$ and all columns is safe:
   $$ B = \frac{(N-1)N}{2} \times \frac{M(M+1)}{2} $$

3. **Intersection (Excluding Both Last Row and Column):**
   Rectangles within the grid from rows $1$ to $N-1$ and columns $1$ to $M-1$ are counted twice, so we subtract them once:
   $$ I = \frac{(N-1)N}{2} \times \frac{(M-1)M}{2} $$

4. **Valid Rectangles:**
   Apply the inclusion-exclusion principle:
   $$ Answer = A + B - I $$

### Code Implementation

Below is the implementation of Approach 2 in both **C++** and **Python**.

#### C++ Code
```cpp
#include
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        long long N, M;
        cin >> N >> M;
        long long regionA = (N * (N + 1) / 2) * ((M - 1) * M / 2);
        long long regionB = ((N - 1) * N / 2) * (M * (M + 1) / 2);
        long long intersection = ((N - 1) * N / 2) * ((M - 1) * M / 2);
        cout << regionA + regionB - intersection << endl;
    }
    return 0;
}
```

#### Python Code
```python
def count_subrectangles(n, m):
    regionA = (n * (n + 1) // 2) * (((m - 1) * m) // 2)
    regionB = (((n - 1) * n) // 2) * (m * (m + 1) // 2)
    intersection = (((n - 1) * n) // 2) * (((m - 1) * m) // 2)
    return regionA + regionB - intersection

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(count_subrectangles(n, m))
```

---

## Summary

- **Approach 1** uses a direct mathematical formula to compute the total number of subrectangles and subtracts the count of those including the cell $(N, M)$. This approach is optimal and straightforward.
- **Approach 2** divides the grid into regions that are guaranteed to exclude the forbidden cell using the inclusion-exclusion principle.

Each approach deepens your understanding of combinatorial counting and reinforces the importance of optimal algorithm design when facing constraints.

</details>
