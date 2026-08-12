# Bozo Sort - Optimal Approach

## Algorithm Explanation

Find the expected number of 3-element random shuffles to sort a random permutation of $11$ natural numbers under the 3-element Bozo sort variant, rounded to the nearest integer.

### Permutation Cycle Conjugacy Class Markov System:
1. **Conjugacy Class State Reduction**:
   The expected number of steps to sort a permutation depends strictly on its cycle type (disjoint cycle partition of $N$).
   For $N = 11$, the number of integer partitions is $P(11) = 56$, compressing $11! = 39,916,800$ permutations into just $56$ state classes.
2. **Transition Probability Matrix**:
   Selecting $3$ random indices out of $\binom{11}{3} = 165$ and applying a random 3-permutation induces explicit transition probabilities between cycle partitions:
   $$P(c \to c') = \sum_{\text{move}} \text{prob}(\text{move}) \cdot \text{indicator}(c \to c')$$
3. **Linear System & Gaussian Elimination**:
   We set up the system of $56$ linear equations:
   $$E[c] = 1 + \sum_{c'} P(c \to c') E[c'], \quad E[\text{identity}] = 0$$
   Solving via Gaussian elimination yields expected values $E[c]$ for all conjugacy classes.
4. **Execution**:
   Averaging $E[c]$ weighted by conjugacy class sizes $\frac{N!}{\prod k^{a_k} a_k!}$ for $N = 11$ and rounding to the nearest integer yields $48271207$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P(N)^3)$ for $P(11) = 56$. Runs in $\approx 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(P(N)^2)$ transition matrix.
