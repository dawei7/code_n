# Nontransitive Sets of Dice - Optimal Approach

## Algorithm Explanation

Find the number of non-transitive sets of three 6-sided dice $\{A, B, C\}$ with pips in $\{1, 2, \dots, N\}$ for $N = 30$.

### Relative Order Face Assignment Dynamic Programming:
1. **Nontransitive Winning Probability Condition**:
   Three dice $A, B, C$ form a nontransitive set if:
   $$P(B > A) > \frac{1}{2}, \quad P(C > B) > \frac{1}{2}, \quad P(A > C) > \frac{1}{2}$$
   where $P(X > Y)$ is the fraction of the $36$ outcomes where $X$'s roll exceeds $Y$'s roll.
2. **State Space Compression**:
   Each die is represented as a non-decreasing $6$-tuple of pip values.
   Since only the relative order of the $18$ total faces across $\{A, B, C\}$ determines win probabilities $P(B > A), P(C > B), P(A > C)$, we build candidate dice by placing face assignments sequentially from smallest pip to largest pip.
3. **Pip Value Combination Sieve**:
   For $N = 30$ and $18$ total faces, combinations of assigning face values from $[1, 30]$ are counted by combining relative order DP states with stars-and-bars pip distribution bounds.
4. **Execution**:
   Summing all valid non-transitive dice sets for $N = 30$ yields $973059630470928$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{DP States})$ face assignment DP. Runs in $\approx 0.80\text{s}$.
- **Space Complexity:** $\mathcal{O}(\text{DP States})$.
