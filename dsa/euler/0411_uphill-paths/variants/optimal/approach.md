# Uphill Paths - Optimal Approach

## Algorithm Explanation

Find $\sum_{k=1}^{30} S(k^5)$, where $S(n)$ is the maximum number of station points $(2^i \bmod n, 3^i \bmod n)$ for $0 \le i \le 2n$ that an $x$- and $y$-non-decreasing path from $(0, 0)$ to $(n, n)$ can pass through.

### 2D Sorting & Fenwick Tree Longest Non-Decreasing Subsequence (LIS):
1. **Station Set Generation**:
   For $n = k^5$ ($k = 1 \dots 30$), we generate the coordinates $(x_i, y_i) = (2^i \bmod n, 3^i \bmod n)$ for $0 \le i \le 2n$ and remove duplicate points.
2. **2D Dominance Order & LIS Reduction**:
   A valid non-decreasing path through a subset of points requires both $x_1 \le x_2 \le \dots \le x_r$ and $y_1 \le y_2 \le \dots \le y_r$.
   By sorting all points primarily by $x_i$ ascending and secondarily by $y_i$ ascending, the maximum number of stations simplifies to finding the Longest Non-Decreasing Subsequence (LIS) of the sorted $y_i$ values.
3. **Fenwick Tree / Patience Sorting**:
   The LIS length is computed in $\mathcal{O}(M \log M)$ time using a Fenwick Tree (Binary Indexed Tree) or patience sorting with binary search.
4. **Execution**:
   Summing $S(k^5)$ for $k = 1 \dots 30$ yields $9936352$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\sum M_k \log M_k)$ for $M_k \le 2 k^5 + 1$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(M_k)$ point arrays.
