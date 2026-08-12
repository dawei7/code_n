# Prime Cube Partnership - Optimal Approach

## Algorithm Explanation

Find the number of primes $p < 1,000,000$ for which there exists a positive integer $n$ such that $n^3 + n^2 p = m^3$ is a perfect cube.

### Cubical Algebraic Factorization:
Factorizing the equation:
$$n^2(n + p) = m^3$$

For $n^2(n + p)$ to form a perfect cube with prime $p$, $n$ must be a perfect cube $n = k^3$:
$$k^6(k^3 + p) = m^3 \implies k^3 + p = (k + 1)^3$$

Expanding $(k + 1)^3 - k^3$:
$$p = 3k^2 + 3k + 1$$

Thus, prime $p$ must be a difference of consecutive cubes $p = (k+1)^3 - k^3$.

### Search Strategy:
Iterate $k = 1, 2, 3 \dots$, compute $p = 3k^2 + 3k + 1$, check primality, and increment count while $p < 10^6$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\sqrt{\text{Limit}})$ where $\text{Limit} = 10^6$ ($k \le 577$). Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
