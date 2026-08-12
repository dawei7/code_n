# Billionaire - Optimal Approach

## Algorithm Explanation

Find the probability of accumulating at least $£1\,000\,000\,000$ starting with $£1$ capital after $1000$ fair coin tosses using an optimal fixed betting fraction $f \in (0, 1)$, rounded to $12$ decimal places.

### Kelly Criterion Optimization & Binomial Tail Probability:
1. **Capital Growth Formula**:
   With $H$ heads and $1000 - H$ tails, capital is:
   $$C(H, f) = (1 + 2f)^H (1 - f)^{1000 - H}$$
2. **Log-Capital Maximization**:
   Differentiating $L(f) = \ln C(H, f)$ gives the optimal fraction for a given $H$:
   $$f^*(H) = \frac{3H - 1000}{2000}$$
3. **Threshold Heads $H_{\min}$**:
   Substituting $f^*(H)$, the smallest integer number of heads yielding $C(H, f^*(H)) \ge 10^9$ is $H_{\min} = 432$.
4. **Exact Cumulative Probability**:
   The chance of becoming a billionaire is the tail binomial probability:
   $$P = \sum_{k=432}^{1000} \frac{\binom{1000}{k}}{2^{1000}}$$
5. **Execution**:
   Evaluating the tail sum gives $0.999992836187$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ for $N = 1000$. Runs in $\approx 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
