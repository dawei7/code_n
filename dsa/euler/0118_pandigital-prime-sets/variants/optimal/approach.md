# Pandigital Prime Sets - Optimal Approach

## Algorithm Explanation

Find the number of distinct sets containing each of the digits $1 \dots 9$ exactly once such that all elements of the set are prime.

### Permutation & Ordered Partition Search:
1. Iterate all $9! = 362,880$ permutations of digits $(1 \dots 9)$.
2. Partition each permutation into integer slices via recursive backtracking.
3. **Symmetry Breaking (Unique Set Ordering)**:
   - Enforce that consecutive prime elements in a partition must be strictly increasing: $p_1 < p_2 < \dots < p_k$.
   - This ensures each unique subset of primes is counted exactly once regardless of permutation order.
4. Verify primality of each integer slice using fast deterministic primality testing.
5. Accumulate and return the total count of valid prime sets.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(9! \cdot K)$ where $9! = 362880$ and $K$ is average valid partition depth. Runs in $< 0.4\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary stack depth is at most $9$.
