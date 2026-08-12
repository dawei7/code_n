# Twenty-two Foolish Primes - Optimal Approach

## Algorithm Explanation

Find the probability that exactly 22 prime number discs (out of 25 prime discs $\le 100$) are away from their natural positions in a random permutation of disks $1 \dots 100$, rounded to 12 decimal places.

### Partial Derangement & Inclusion-Exclusion:
1. **Prime Count**:
   There are $P = 25$ primes up to $100$. Exactly 22 deranged primes means exactly $3$ primes are fixed points ($P - 22 = 3$).
2. **Inclusion-Exclusion Summation**:
   Selecting $3$ fixed primes in $\binom{25}{3}$ ways, the remaining $97$ positions (containing 22 prime items) are constrained such that no additional prime occupies its natural position:
   $$W = \binom{25}{3} \sum_{m=0}^{22} (-1)^m \binom{22}{m} (100 - 3 - m)!$$
3. **Probability Calculation**:
   Dividing $W$ by total permutations $100!$ yields:
   $$\text{Prob} = \frac{\binom{25}{3}}{100!} \sum_{m=0}^{22} (-1)^m \binom{22}{m} (97 - m)! = 0.001887854841$$

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P)$ for $P = 22$. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
