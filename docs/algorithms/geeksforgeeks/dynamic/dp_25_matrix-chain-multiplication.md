# Matrix Chain Multiplication (Top-Down Memoization)

| | |
|---|---|
| **ID** | `dp_25` |
| **Category** | dynamic_programming |
| **Complexity (required)** | $O(n^3)$ |
| **Difficulty** | 7/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Burst Balloons (Conceptually Similar)](https://leetcode.com/problems/burst-balloons/) |

## Problem statement

*(This is the Top-Down recursive variation of `dp_13_matrix-chain-multiplication`)*.

Given a sequence of `n` matrices, find the minimum number of scalar multiplications needed to multiply them all together. The order of multiplication dictates the cost.

**Input:** An array `p[]` where matrix A_i has dimensions `p[i-1] x p[i]`.
**Output:** An integer representing the minimum cost.

## When to use it

- The Bottom-Up approach (`dp_13`) requires complex looping over chain lengths `L`. Many engineers find the Top-Down recursive approach significantly more intuitive to write during a whiteboard interview.
- It perfectly demonstrates **Memoization**.

## Approach

We define a recursive function `solve(i, j)` that returns the minimum cost to multiply the sub-chain from matrix A_i to matrix A_j.

**Base Case:**
If `i == j`, there is only one matrix! The cost to multiply a single matrix is `0`.

**Recursive Step:**
If `i < j`, we try placing a parenthesis at every possible split point `k` (where i \le k < j).
The cost for a specific `k` is:
`cost = solve(i, k) + solve(k + 1, j) + p[i-1] * p[k] * p[j]`

We take the minimum of all these costs.
To prevent exponential $O(2^n)$ time complexity (re-calculating the same `solve(i, j)` multiple times), we store the results in a 2D cache table `memo[i][j]`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_25: Matrix Chain Multiplication.

m[i][j] = min over k of m[i][k] + m[k+1][j] +
dims[i][0] * dims[k][1] * dims[j][1].
"""


def solve(dims, n):
    if n <= 1:
        return 0
    INF = float("inf")
    m = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = INF
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i][0] * dims[k][1] * dims[j][1]
                if cost < m[i][j]:
                    m[i][j] = cost
    return m[0][n - 1]
```

</details>

## Walk-through

`p = [10, 20, 30, 40]`. `n = 3`. (Matrices A, B, C).

Call `solve(1, 3)` (Solve ABC).
- Try `k=1`: `solve(1,1) + solve(2,3) + 10*20*40`.
  - `solve(1,1)` returns `0`.
  - Call `solve(2,3)` (Solve BC).
    - Try `k=2`: `solve(2,2) + solve(3,3) + 20*30*40`.
      - `solve(2,2)` = `0`. `solve(3,3)` = `0`. Cost = `24000`.
    - Returns `24000`. Caches `memo[2][3] = 24000`.
  - Total for `k=1`: `0 + 24000 + 8000 = 32000`.

- Try `k=2`: `solve(1,2) + solve(3,3) + 10*30*40`.
  - Call `solve(1,2)` (Solve AB).
    - Try `k=1`: `solve(1,1) + solve(2,2) + 10*20*30`.
      - `0 + 0 + 6000 = 6000`.
    - Returns `6000`. Caches `memo[1][2] = 6000`.
  - `solve(3,3)` returns `0`.
  - Total for `k=2`: `6000 + 0 + 12000 = 18000`.

Min of `32000` and `18000` is `18000`.
Cache `memo[1][3] = 18000`. Returns `18000`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n^3)$ | $O(n^2)$ |
| **Average** | $O(n^3)$ | $O(n^2)$ |
| **Worst** | $O(n^3)$ | $O(n^2)$ |

The number of unique states in the `memo` table is $O(n^2)$. For each state `(i, j)`, we run a loop of size up to n to try all split points `k`. Therefore, the time complexity is exactly $O(n^3)$.
Space complexity is $O(n^2)$ for the memoization table and $O(n)$ for the recursion stack.

## Variants & optimizations

- **Bottom-Up:** The bottom-up iterative approach avoids the $O(n)$ recursion stack overhead and is marginally faster in practice due to CPU cache locality, but theoretically identical.

## Real-world applications

- **SQL Query Optimization:** Database engines use a heavily modified version of this algorithm to determine the optimal join order for `SELECT * FROM A JOIN B JOIN C`, minimizing intermediate row generation.

## Related algorithms in cOde(n)

- **[dp_13 - Matrix Chain Multiplication](dp_13_matrix-chain-multiplication.md)** — The iterative, bottom-up counterpart.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
