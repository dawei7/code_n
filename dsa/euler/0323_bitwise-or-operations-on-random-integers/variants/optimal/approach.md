# Bitwise-OR Operations on Random Integers - Optimal Approach

## Algorithm Explanation

Find the expected value $\mathbb{E}[N]$ of the number of steps $N$ until $x_N = 2^{32} - 1$ under $x_0 = 0, x_i = x_{i-1} \mid y_{i-1}$ where $y_i$ are independent random uniform $32$-bit integers, rounded to 10 decimal places.

### Independent Bit Tail Probability Summation:
1. **Bit Independence & Cumulative Probability**:
   For any single bit, the probability of remaining $0$ after $k$ random OR operations is $2^{-k}$.
   Since all $32$ bits are independent and uniform:
   $$P(N \le k) = \left( 1 - 2^{-k} \right)^{32}$$
2. **Expectation Tail Formula**:
   By the expectation formula for non-negative integer random variables:
   $$\mathbb{E}[N] = \sum_{k=0}^{\infty} P(N > k) = \sum_{k=0}^{\infty} \left( 1 - (1 - 2^{-k})^{32} \right)$$
3. **Execution**:
   Summing the tail probabilities for $k = 0 \dots 100$ converges to double precision accuracy, yielding $\mathbb{E}[N] = 6.3551758451$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K)$ for $K = 100$. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
