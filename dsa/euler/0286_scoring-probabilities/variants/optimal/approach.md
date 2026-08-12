# Scoring Probabilities - Optimal Approach

## Algorithm Explanation

Find the real constant $q > 50$ such that the probability of scoring exactly $20$ points in $50$ basketball shots at distances $x = 1, 2, \dots, 50$ (where probability of scoring from distance $x$ is $p_x(q) = 1 - x / q$) is equal to $0.02$, rounded to 10 decimal places.

### Dynamic Programming Probability Evaluation & Bisection:
1. **Dynamic Programming Probability Distribution**:
   For a fixed $q > 50$, let `dp[k]` be the probability of scoring $k$ points after considering shots at distances $1 \dots x$.
   The state transition is:
   $$\text{dp}_{\text{next}}[k] = \text{dp}[k] \cdot \frac{x}{q} + \text{dp}[k-1] \cdot \left( 1 - \frac{x}{q} \right)$$
2. **Monotonic Bisection Root Finding**:
   The probability $P_{20}(q)$ of scoring exactly $20$ points decreases monotonically as $q$ increases from $50$.
   We use binary search / bisection over $q \in (50, 100)$ to find $q$ where $P_{20}(q) = 0.02$.
3. **Execution**:
   Bisection converges after $100$ iterations to $q = 52.6494571953$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2 \cdot K)$ for $N = 50$ shots and $K = 100$ bisection steps. Runs in $\approx 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ DP array.
