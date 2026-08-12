# A Recursively Defined Sequence - Optimal Approach

## Algorithm Explanation

Find $u_n + u_{n+1}$ for $n = 10^{12}$, where $u_0 = -1$ and $u_{n+1} = f(u_n)$ with $f(x) = \lfloor 2^{30.403243784 - x^2} \rfloor \times 10^{-9}$.

### Contraction Mapping & 2-Cycle Convergence:
1. **Fixed-Point / 2-Cycle Attractor**:
   The function $f(x)$ is a bounded continuous map from $\mathbb{R} \to [0, 1.414]$.
   Iterating $f(x)$ rapidly contracts the interval, causing $u_n$ to settle into a stable 2-cycle $(a, b)$ within $< 1000$ iterations.
2. **Evaluation**:
   Simulating $1000$ iterations stabilizes $u_n$ and $u_{n+1}$ to $9$ decimal places, yielding $1.710637717$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ - Fixed $1000$ iterations. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
