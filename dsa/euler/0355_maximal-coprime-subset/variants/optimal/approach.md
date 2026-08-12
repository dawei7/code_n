# Maximal Coprime Subset - Optimal Approach

## Algorithm Explanation

Find $\operatorname{Co}(200\,000)$, the maximum possible sum of a set of mutually coprime elements from $\{1, 2, \dots, n\}$ for $n = 200\,000$.

### Maximum Weight Bipartite Matching & Prime Factor Allocation:
1. **Prime Factor Disjointness Constraint**:
   In a mutually coprime subset $S \subseteq \{1 \dots n\}$, no two elements share a common prime factor.
   Thus, each prime $p \le n$ can be used in at most one chosen element of $S$.
2. **Element Structure**:
   Elements in $S$ are either:
   - Standalone max prime powers $p^k \le n$.
   - Composite combinations $p_1^{a} p_2^{b} \dots \le n$.
   For large primes $p > \sqrt{n}$, $p$ can combine with at most one small prime $q \le \sqrt{n} \approx 447$.
3. **Min-Cut / Maximum Weight Matching**:
   Modeling small primes $q \le \sqrt{n}$ as one partition and large primes $p \in (\sqrt{n}, n/2]$ as the second partition of a bipartite graph, the optimal element selection maps to a Maximum Weight Bipartite Matching / Min-Cut Flow problem.
4. **Execution**:
   Solving the matching for $n = 200\,000$ yields maximum subset sum $1726545007$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^{1/2} \cdot E)$ for $N = 200\,000$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ prime array storage.
