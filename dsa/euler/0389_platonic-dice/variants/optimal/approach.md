# Platonic Dice - Optimal Approach

## Algorithm Explanation

Find the variance of $I$, the final sum of 20-sided dice rolled in a 5-stage Platonic dice sequence ($T \to C \to O \to D \to I$), rounded to 4 decimal places.

### Law of Total Expectation & Total Variance:
1. **Random Sum Variance Formula**:
   For a random sum $S_N = \sum_{i=1}^N X_i$ of $N$ i.i.d. random variables $X$ (independent of $N$):
   $$\operatorname{E}[S_N] = \operatorname{E}[N] \cdot \operatorname{E}[X]$$
   $$\operatorname{Var}(S_N) = \operatorname{E}[N] \cdot \operatorname{Var}(X) + \operatorname{Var}(N) \cdot (\operatorname{E}[X])^2$$
2. **Single Die Parameters**:
   For a uniform $k$-sided die $X_k$:
   $$\operatorname{E}[X_k] = \frac{k + 1}{2}, \quad \operatorname{Var}(X_k) = \frac{k^2 - 1}{12}$$
3. **5-Stage Cascade Propagation**:
   - **Stage 1 ($T$, 4-sided)**: $\operatorname{E}[T] = 2.5$, $\operatorname{Var}(T) = 1.25$.
   - **Stage 2 ($C$, 6-sided)**: $\operatorname{E}[C] = 8.75$, $\operatorname{Var}(C) = 22.60416667$.
   - **Stage 3 ($O$, 8-sided)**: $\operatorname{E}[O] = 39.375$, $\operatorname{Var}(O) = 503.671875$.
   - **Stage 4 ($D$, 12-sided)**: $\operatorname{E}[D] = 255.9375$, $\operatorname{Var}(D) = 21749.3828125$.
   - **Stage 5 ($I$, 20-sided)**: $\operatorname{Var}(I) = \operatorname{E}[D] \operatorname{Var}(X_{20}) + \operatorname{Var}(D) (\operatorname{E}[X_{20}])^2 = 2406376.3623$.
4. **Execution**:
   Evaluating the cascade variance closed-form yields $2406376.3623$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ closed-form calculation. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
