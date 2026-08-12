# Sums of Square Reciprocals - Optimal Approach

## Algorithm Explanation

Find the total number of ways to express $\frac{1}{2}$ as a sum of reciprocal squares $\sum_{k \in S} \frac{1}{k^2} = \frac{1}{2}$ using distinct integers $S \subseteq \{2, 3, \dots, 80\}$.

### Prime Factor Cancellation & Cross-Multiple Consistency:
For any prime $p \ge 5$, a non-empty subset of multiples $\{m \cdot p\}$ can appear in $S$ if and only if $\sum \frac{1}{m^2}$ has $p$ in its numerator (canceling out $p^2$ in the denominator).

1. **Pruning Unusable Primes**:
   - Primes $> 40$ have no multiple pairs to cancel.
   - Primes $19, 23, 29, 31, 37$ have $0$ valid canceling subsets of multiples $\le 80$.
2. **Cross-Prime Shared Multiples Consistency**:
   - Multiples like $77$ (shared by $7$ and $11$) and $\{35, 55, 65, 70\}$ (shared by $5$ and higher primes) must be consistently included or excluded across prime factor sub-problems.
3. **Structured Grouping & Precomputation**:
   - Precompute valid 17, 13, 11, 7 prime combinations enforcing $77 \in c_{11} \iff 77 \in c_7$.
   - Precompute a map of valid 5-group completions conditioned on fixed shared elements $\{35, 55, 65, 70\}$.
   - Precompute all $2^{17} = 131,072$ subset sums of base $\{2, 3\}$ numbers into frequency map `base_23_sums`.
   - Perform $\mathcal{O}(1)$ lookup across valid composite selections.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{ValidCombos}_{\text{Consistent}} \cdot U_5)$ where $U_5 \le 132$. Runs in $\approx 3.9\text{s}$.
- **Space Complexity:** $\mathcal{O}(2^{17})$ - Frequency map of base $\{2,3\}$ subset sums.
