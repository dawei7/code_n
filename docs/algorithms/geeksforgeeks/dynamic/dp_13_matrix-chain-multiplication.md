# Matrix Chain Multiplication

| | |
|---|---|
| **ID** | `dp_13` |
| **Category** | dynamic |
| **Complexity (required)** | $O(N^3)$ Time, $O(N^2)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 6/10 |
| **Wikipedia** | [Matrix chain multiplication](https://en.wikipedia.org/wiki/Matrix_chain_multiplication) |

## Problem statement

Given a sequence of matrices, find the most efficient way to multiply these matrices together.
Matrix multiplication is associative, meaning `A * (B * C)` yields the same mathematical result as `(A * B) * C`. However, the *number of scalar multiplications* required can differ drastically depending on the grouping!
Multiplying a P x Q matrix by a Q x R matrix requires P x Q x R scalar multiplications.
Given an array `p` representing the dimensions of N matrices such that the i-th matrix has dimension `p[i-1] x p[i]`, find the minimum number of scalar multiplications needed to multiply the entire chain.

**Input:** An array of integers `p` of length N+1.
**Output:** An integer representing the minimum scalar multiplications.

## When to use it

- The canonical introduction to **Interval DP** (also known as Range DP).
- Use this whenever a problem asks you to optimally parenthesize, group, or merge adjacent elements in an array.

## Approach

**1. Define the State:**
Let `dp[i][j]` be the minimum number of scalar multiplications needed to multiply the chain of matrices from matrix `i` to matrix `j`.

**2. Find the Base Cases:**
If `i == j`, there is only one matrix! The cost to multiply a single matrix by nothing is 0.
`dp[i][i] = 0` for all i.

**3. Find the Transition (The recurrence relation):**
To multiply a chain of matrices from `i` to `j`, we must make a final multiplication that joins two sub-chains. We can split the chain at some index `k` (where i \le k < j).
The cost to do this split at `k` is:
- The optimal cost to compute the left sub-chain: `dp[i][k]`
- The optimal cost to compute the right sub-chain: `dp[k+1][j]`
- The cost to multiply the two resulting matrices together: The resulting left matrix will have dimensions `p[i-1] x p[k]`, and the right matrix will be `p[k] x p[j]`. Multiplying them costs `p[i-1] * p[k] * p[j]`.

We try ALL possible split points `k`, and take the minimum!
`dp[i][j] = min( dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j] )` for all i \le k < j.

**4. Build the Table (Bottom-Up by Length):**
This is the trickiest part of Interval DP! You CANNOT just loop `i` from 0 to N and `j` from 0 to N.
To calculate `dp[1][4]`, you need `dp[1][2]` and `dp[3][4]`. You must calculate all intervals of length 2 first, then length 3, then length 4!
The outer loop must iterate over the `length` of the interval.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_13: Matrix Chain Multiplication.

dp[i][j] = min cost of multiplying matrices i..j.
"""


def solve(p):
    n = len(p) - 1
    if n <= 1:
        return 0
    INF = float("inf")
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = INF
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[0][n - 1]
```

</details>

## Walk-through

`p = [10, 20, 30, 40]`. There are 3 matrices (A, B, C).
A is 10 x 20, B is 20 x 30, C is 30 x 40.
`n = 3`. `dp` is 4 x 4 initialized to 0.

1. **Length = 2:**
   - **i = 1, j = 2 (AB):**
     - k = 1: `dp[1][1] + dp[2][2] + p[0]*p[1]*p[2]`
     - = 0 + 0 + 10 x 20 x 30 = 6000. `dp[1][2] = 6000`.
   - **i = 2, j = 3 (BC):**
     - k = 2: `dp[2][2] + dp[3][3] + p[1]*p[2]*p[3]`
     - = 0 + 0 + 20 x 30 x 40 = 24000. `dp[2][3] = 24000`.

2. **Length = 3:**
   - **i = 1, j = 3 (ABC):**
     - k = 1 (Evaluate as A(BC)): `dp[1][1] + dp[2][3] + p[0]*p[1]*p[3]`
       - = 0 + 24000 + 10 x 20 x 40 = 24000 + 8000 = 32000.
     - k = 2 (Evaluate as (AB)C): `dp[1][2] + dp[3][3] + p[0]*p[2]*p[3]`
       - = 6000 + 0 + 10 x 30 x 40 = 6000 + 12000 = 18000.
     - Minimum is 18000. `dp[1][3] = 18000`.

Result `dp[1][3]` is 18000. ✓ (Grouping as (AB)C is almost twice as fast!).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^3)$ | $O(N^2)$ |
| **Average** | $O(N^3)$ | $O(N^2)$ |
| **Worst** | $O(N^3)$ | $O(N^2)$ |

The nested loops define $O(N^2)$ intervals `(i, j)`. For every interval, the `k` loop runs up to N times. Total time complexity is strictly $O(N^3)$.
Space complexity is $O(N^2)$ for the 2D DP matrix.

## Variants & optimizations

- **Printing the Parenthesization:** If you need to return a string like `"(A(BC))"`, you must maintain a second N x N matrix `split[i][j]` that records the integer `k` that yielded the minimum cost. Then, recursively reconstruct the string!
- **Burst Balloons:** An incredibly hard LeetCode Hard problem that is mathematically identical to Matrix Chain Multiplication. You iterate lengths and try picking a balloon `k` to be the *last* balloon to pop in the interval!

## Real-world applications

- **Database Query Optimizers:** Determining the optimal join order for complex SQL statements (e.g., `A JOIN B JOIN C`) to minimize intermediate table creation overhead.

## Related algorithms in cOde(n)

- **[dp_14 - Palindromic Partitioning](dp_14_palindromic-partitioning.md)** — Another Interval DP that optimizes cuts over a continuous string.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
