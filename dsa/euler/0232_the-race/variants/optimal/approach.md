# The Race - Optimal Approach

## Algorithm Explanation

Find the probability that Player 2 wins The Race to $100$ points, assuming Player 2 plays optimally to maximize their winning probability.

### Dynamic Programming & Optimal Strategy Choice:
1. **Game State Definition**:
   - Let $V(i, j)$ be Player 2's win probability on Player 1's turn with scores $(i, j)$.
   - Let $W(i, j)$ be Player 2's win probability on Player 2's turn with scores $(i, j)$.
   Base cases: $V(i, j) = 1$ for $j \ge 100$ and $V(i, j) = 0$ for $i \ge 100$.
2. **Turn Transitions**:
   On Player 2's turn choosing $T$ coin tosses ($2^{T-1}$ points on all Heads, prob $2^{-T}$):
   $$W(i, j) = \max_{T \ge 1} \left[ 2^{-T} V(i, j + 2^{T-1}) + (1 - 2^{-T}) V(i, j) \right]$$
   On Player 1's turn at $(i, j)$:
   $$V(i, j) = \frac{1}{2} W(i+1, j) + \frac{1}{2} W(i, j)$$
3. **Closed Form Value Iteration**:
   Solving for $V(i, j)$ under optimal $T$ choice yields:
   $$V(i, j) = \max_{T \ge 1} \left( \frac{2^T W(i+1, j) + V(i, j + 2^{T-1})}{2^T + 1} \right)$$
4. **Execution**:
   Filling the DP table backwards for $i, j \in [0, 99]$ yields Player 2 winning probability $0.84193608$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2 \log_2 N)$ for $N = 100$. Runs in $\approx 0.055\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^2)$ DP state storage.
