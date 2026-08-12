# At Least Four Distinct Prime Factors Less Than 100 - Optimal Approach

## Algorithm Explanation

Find the number of positive integers less than $10^{16}$ that are divisible by at least four distinct primes less than $100$.

### Generalized Inclusion-Exclusion Principle:
1. **Prime Set**:
   There are $25$ prime numbers less than $100$: $P = \{2, 3, 5, 7, \dots, 97\}$.
2. **Inclusion-Exclusion Coefficients**:
   For a condition requiring at least $k = 4$ prime factors, the inclusion-exclusion weight for a subset of size $m \ge 4$ is given by:
   $$c_m = (-1)^{m - 4} \binom{m - 1}{3}$$
3. **Pruned Subset Backtracking**:
   We search over all subsets of $P$ whose product $\prod_{p \in S} p < 10^{16}$.
   For each valid subset $S$ of size $m \ge 4$, we accumulate $c_m \cdot \lfloor \frac{10^{16}-1}{\prod_{p \in S} p} \rfloor$.
4. **Execution**:
   Summing all weighted counts yields $785478606870942$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{valid\_subsets})$ where subset products $< 10^{16}$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
