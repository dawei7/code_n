# Totient Permutation - Optimal Approach

## Algorithm Explanation

Find the value $n < 10^7$ for which $\phi(n)$ is a digit permutation of $n$ and the ratio $\frac{n}{\phi(n)}$ is minimized.

### Mathematical Reduction
To minimize $\frac{n}{\phi(n)} = \prod_{p \mid n} \frac{p}{p-1}$:
1. Prime numbers $n$ yield $\phi(n) = n - 1$, but $n$ and $n - 1$ cannot be digit permutations of each other due to differing digit sums.
2. The optimal candidate form must be a **semiprime** $n = p_1 \cdot p_2$ composed of two distinct primes close to $\sqrt{10^7} \approx 3162$.

For $n = p_1 \cdot p_2$:
$$\phi(n) = (p_1 - 1)(p_2 - 1)$$

### Search Strategy:
- Generate primes in range $[2000, 5000]$ around $\sqrt{10^7}$.
- Test pairs $p_1 < p_2$ such that $n = p_1 \cdot p_2 < 10^7$.
- Calculate ratio $\frac{n}{\phi(n)}$ and verify `sorted(str(n)) == sorted(str(phi))`.
- Return $n$ yielding the global minimum ratio.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P^2)$ where $P \approx 300$ primes around $\sqrt{N}$. Runs in $< 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(P)$ - Prime list storage.
