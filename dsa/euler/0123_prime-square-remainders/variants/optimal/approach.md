# Prime Square Remainders - Optimal Approach

## Algorithm Explanation

Find the least prime index $n$ for which the remainder $r = (p_n - 1)^n + (p_n + 1)^n \pmod{p_n^2}$ first exceeds $10^{10}$.

### Binomial Modulo Reduction:
Using the binomial expansion modulo $p_n^2$:
- For $n$ **even**: $(p_n - 1)^n + (p_n + 1)^n \equiv 2 \pmod{p_n^2}$ (constant 2, never exceeds $10^{10}$).
- For $n$ **odd**: $(p_n - 1)^n + (p_n + 1)^n \equiv 2 n p_n \pmod{p_n^2}$.
  Since $2 n < p_n$ for large $n$, $2 n p_n < p_n^2$, so the exact remainder is:
  $$r = 2 n p_n$$

### Strategy:
1. Sieve prime numbers $p_n$ up to $1,000,000$.
2. Iterate odd indices $n = 1, 3, 5, 7 \dots$.
3. Evaluate remainder $r = 2 n p_n$.
4. Return $n$ as soon as $r > 10^{10}$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where prime index $N \approx 21035$. Runs in $< 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(P)$ - Prime sieve array.
