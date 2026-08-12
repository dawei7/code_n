# Prime Pair Connection - Optimal Approach

## Algorithm Explanation

Find $\sum S$ for every pair of consecutive primes $(p_1, p_2)$ with $5 \le p_1 \le 1,000,000$, where $S$ is the smallest positive integer that ends in $p_1$ and is divisible by $p_2$.

### Modular Congruence Linear Solver:
Let $m = 10^{\lceil \log_{10}(p_1 + 1) \rceil}$ be the smallest power of 10 greater than $p_1$.
The integer $S$ ending in $p_1$ takes the form $S = k \cdot m + p_1$ for $k \ge 0$.

Divisibility requirement:
$$S \equiv 0 \pmod{p_2} \implies k \cdot m + p_1 \equiv 0 \pmod{p_2}$$
$$k \cdot m \equiv -p_1 \pmod{p_2}$$

Since $p_2 \ge 7$ is prime and $\gcd(m, p_2) = 1$, modular inverse $m^{-1} \pmod{p_2}$ exists:
$$k \equiv (-p_1 \cdot m^{-1}) \bmod p_2$$

Calculate $k$ via `pow(m, -1, p2)` in $\mathcal{O}(\log p_2)$ time, evaluate $S = k \cdot m + p_1$, and sum across all prime pairs.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P \log P)$ where $P = \pi(10^6) \approx 78498$. Runs in $< 0.12\text{s}$.
- **Space Complexity:** $\mathcal{O}(\text{Limit})$ - Prime sieve array.
