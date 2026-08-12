# Sums of Powers of Two - Optimal Approach

## Algorithm Explanation

Find $f(10^{25})$, the number of ways to express $N = 10^{25}$ as a sum of powers of $2$ using each power at most twice.

### Binary Recursion & Stern-Brocot / Calkin-Wilf Sequence:
Let $f(n)$ be the number of valid base-2 representations allowing digit set $\{0, 1, 2\}$.

1. **Base Cases**:
   - $f(0) = 1$
   - $f(1) = 1$
2. **Odd Numbers ($n = 2k + 1$)**:
   The least significant digit $2^0$ MUST be $1$ (since $2k+1$ is odd and higher powers of $2$ are even).
   Subtracting $1$ leaves $2k$, so:
   $$f(2k + 1) = f(k)$$
3. **Even Numbers ($n = 2k$)**:
   The least significant digit $2^0$ can be either $0$ or $2$:
   - If $2^0 = 0$, dividing by $2$ leaves $k \implies f(k)$ ways.
   - If $2^0 = 2$, subtracting $2$ leaves $2k - 2$, dividing by $2$ leaves $k - 1 \implies f(k - 1)$ ways.
   $$f(2k) = f(k) + f(k - 1)$$

Memoized top-down recursion evaluates $f(10^{25})$ in $\mathcal{O}(\log_2 N)$ steps.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_2 N)$ steps ($N = 10^{25}$, $\approx 100$ recursive states). Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log_2 N)$ - Memoization dictionary.
