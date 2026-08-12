# Arranged Probability - Optimal Approach

## Algorithm Explanation

Find the number of blue discs $b$ in the first configuration with total discs $N > 10^{12}$ for which the probability of drawing two blue discs without replacement is exactly $P(BB) = \frac{1}{2}$.

### Pell Equation Reduction:
Probability relation:
$$\frac{b(b - 1)}{N(N - 1)} = \frac{1}{2} \implies 2b^2 - 2b = N^2 - N$$

Completing squares:
$$2(2b - 1)^2 = (2N - 1)^2 + 1 \implies (2N - 1)^2 - 2(2b - 1)^2 = -1$$

This is a negative Pell equation $y^2 - 2x^2 = -1$ where $y = 2N - 1$ and $x = 2b - 1$.

### Matrix Recurrence Relation:
Transitions between consecutive integer solutions $(b_k, N_k)$:
$$b_{k+1} = 3 b_k + 2 N_k - 2$$
$$N_{k+1} = 4 b_k + 3 N_k - 3$$

Starting with initial valid solution $(b_1, N_1) = (15, 21)$, iterate until $N > 10^{12}$ and return $b$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log L)$ logarithmic iterations where $L = 10^{12}$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
