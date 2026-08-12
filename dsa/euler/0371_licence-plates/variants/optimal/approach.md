# Licence Plates - Optimal Approach

## Algorithm Explanation

Find the expected number of licence plates Seth needs to see to get a winning pair adding to $1000$, rounded to 8 decimal places.

### Markov Chain Absorbing State Expectation DP:
1. **Complementary Number Pair Partition**:
   Out of $1000$ possible 3-digit numbers $[000..999]$:
   - $000$ has no complement adding to $1000$.
   - $500$ is self-complementary ($500 + 500 = 1000$), requiring seeing $500$ twice.
   - $499$ disjoint pairs $(x, 1000-x)$ for $x \in [1, 499]$.
2. **State Space Formulation**:
   Let state $(k, b)$ represent having seen $k$ distinct non-$500$ pair halves ($0 \le k \le 499$) and $b \in \{0, 1\}$ indicating whether $500$ has been seen.
   - From $(k, 0)$:
     - Win prob: $k / 1000$.
     - Transition to $(k, 1)$: $1 / 1000$.
     - Transition to $(k+1, 0)$: $2(499-k) / 1000$.
     - Self-loop: $(k+1) / 1000$.
   - From $(k, 1)$:
     - Win prob: $(k + 1) / 1000$.
     - Transition to $(k+1, 1)$: $2(499-k) / 1000$.
     - Self-loop: $k / 1000$.
3. **Triangular System Evaluation**:
   Backwards DP evaluation from $k = 499$ down to $0$ computes the exact expected value $E(0, 0)$.
4. **Execution**:
   Evaluating $E(0, 0)$ yields $40.66368097$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ for $N = 500$ pairs. Runs in $\approx 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ state DP table.
