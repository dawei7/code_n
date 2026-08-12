# Generalised Hamming Numbers - Optimal Approach

## Algorithm Explanation

Find the number of generalised Hamming numbers of type $100$ (smooth numbers with no prime factor $> 100$) that do not exceed $10^9$.

### Prime Backtracking / DFS:
1. **Prime Factorization Set**:
   There are $25$ primes $\le 100$: $2, 3, 5, \dots, 97$.
2. **Recursive Search**:
   We search over prime exponent choices $e_1, e_2, \dots, e_{25}$ such that $\prod p_i^{e_i} \le 10^9$.
3. **Execution**:
   The depth-first search traverses all $2,944,730$ smooth numbers in $\approx 2.8\text{s}$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K)$ where $K = 2944730$ is the number of 100-smooth numbers $\le 10^9$. Runs in $\approx 2.85\text{s}$.
- **Space Complexity:** $\mathcal{O}(\pi(100)) = \mathcal{O}(1)$ - Call stack depth of at most 25.
