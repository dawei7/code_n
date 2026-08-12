# Maximum Product of Parts - Optimal Approach

## Algorithm Explanation

Find $\sum_{N=5}^{10000} D(N)$ where $D(N) = -N$ if the maximum product $M(N) = (N/k)^k$ is a terminating decimal, and $D(N) = N$ if non-terminating.

### Calculus Optimization of $P(k) = (N/k)^k$:
Let $g(k) = \ln P(k) = k \ln N - k \ln k$.
Differentiating with respect to $k$:
$$g'(k) = \ln(N/k) - 1 = 0 \implies k = N / e$$

Since $k$ must be an integer, the optimal $k$ is either $k_1 = \lfloor N / e \rfloor$ or $k_2 = k_1 + 1$.
Compare $k_1 \ln(N / k_1)$ and $k_2 \ln(N / k_2)$ to select $k = \arg\max P(k)$.

### Terminating Decimal Condition:
The fraction $N / k$ yields a terminating decimal $(N / k)^k$ if and only if the reduced denominator $d = k / \gcd(N, k)$ has no prime factors other than $2$ and $5$.

1. Divide $d = k / \gcd(N, k)$ repeatedly by $2$ and $5$.
2. If $d = 1$, $M(N)$ is terminating $\implies D(N) = -N$.
3. If $d > 1$, $M(N)$ is non-terminating $\implies D(N) = N$.

Sum $D(N)$ for $N \in [5, 10000]$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N_{\text{max}} \log N_{\text{max}})$ for $N_{\text{max}} = 10000$. Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant space.
