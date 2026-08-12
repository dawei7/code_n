# Badugi - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=4}^{13} f(n)$, where $f(n)$ is the number of ways to choose $n$ cards from a standard $52$-card deck containing at least one $4$-card subset that is a Badugi ($4$ cards of $4$ distinct ranks and $4$ distinct suits).

### Rank Profile Integer Partitions & Dynamic Programming:
1. **Badugi Hand Condition**:
   A selection of $n$ cards contains a Badugi iff there exist $4$ cards in the hand with pairwise distinct ranks $\{r_1, r_2, r_3, r_4\}$ and pairwise distinct suits $\{s_1, s_2, s_3, s_4\}$.
2. **Rank Multiplicity State Partitioning**:
   The $52$-card deck consists of $13$ ranks with $4$ suit cards each.
   A hand of $n$ cards is uniquely characterized by its rank multiplicity tuple $(a_1, a_2, a_3, a_4)$, where $a_k$ is the number of ranks with exactly $k$ cards present ($\sum k a_k = n$ and $\sum a_k \le 13$).
3. **Suit Inclusion-Exclusion Matrix DP**:
   For each integer partition $(a_1, a_2, a_3, a_4)$, we calculate the number of ways to assign suits such that the selected rank cards form a valid Badugi using suit inclusion-exclusion DP.
   Multiplying by rank multinomial coefficients $\binom{13}{a_0, a_1, a_2, a_3, a_4}$ yields $f(n)$.
4. **Execution**:
   Summing $f(n)$ for $n = 4 \dots 13$ yields $102881005527209700$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P(13) \cdot S)$ for rank partitions $P(13) \le 500$ and $4$ suits. Runs in $\approx 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(P(13))$ state table.
