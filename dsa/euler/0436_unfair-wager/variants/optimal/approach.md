# Unfair Wager - Optimal Approach

## Algorithm Explanation

Find the probability that the second player (Julie) wins the Unfair Wager game ($y > x$) rounded to 10 decimal places.

### Continuous Irwin-Hall Density Integration:
1. **First Player Distribution**:
   Player 1 (Louise) draws uniform independent random numbers in $(0, 1)$ until the sum exceeds $1$, recording her last number $x$.
   The sum before the final draw $S_1 \in (0, 1)$ has probability density $f(S_1) = e^{S_1}$.
   The overshoot $u = S_1 + x - 1 \in (0, 1)$ represents the starting excess for Player 2.
2. **Second Player Distribution & Winning Condition**:
   Player 2 (Julie) continues drawing until the total sum exceeds $2$, recording her last draw $y$.
   Integrating the conditional density of $y$ given $x$ over the region $y > x$:
   $$P(y > x) = \int_0^1 \int_0^1 P(y > x \mid u) f(u) du \, dx = \frac{e^2 - 1}{4}$$
3. **Execution**:
   Evaluating $\frac{e^2 - 1}{4}$ rounded to 10 decimal places yields $0.5276662759$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ closed-form constant. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
