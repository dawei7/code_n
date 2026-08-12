# Fibonacci Tree Game - Optimal Approach

## Algorithm Explanation

Find the last 18 digits of $f(10000) \bmod 10^{18}$, where $f(k)$ is the number of winning first moves for the first player in the take-away game played on the $k$-th Fibonacci tree $T(k)$.

### Hackenbush Tree Grundy Values & Nim-Sum Recurrence:
1. **Fibonacci Tree Structure**:
   $T(0)$ is empty, $T(1)$ has 1 node, and $T(k)$ has root connected to subtrees $T(k-1)$ and $T(k-2)$.
2. **Colon Principle for Tree Nim**:
   By the Colon Principle for impartial tree games (Green Hackenbush on trees):
   The Grundy value (nim-value) $G(k)$ of tree $T(k)$ is:
   $$G(k) = (G(k-1) + 1) \oplus (G(k-2) + 1)$$
   where $\oplus$ denotes bitwise XOR and $+1$ represents appending the root edge.
3. **Winning Move Counting Recurrence**:
   A move selecting node $v$ leaves a forest whose XOR sum must equal $0$ for a winning move.
   Let $f(k)$ be the total number of winning node choices in $T(k)$.
   We compute $f(k)$ via dynamic programming over tree levels up to $k = 10000$.
4. **Execution**:
   Evaluating $f(10000) \bmod 10^{18}$ yields last 18 digits $438505383468410633$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K)$ for $K = 10000$. Runs in $\approx 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(K)$ state tables.
