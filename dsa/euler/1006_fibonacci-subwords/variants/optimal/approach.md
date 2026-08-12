# Fibonacci Subwords - Optimal Approach

## Algorithm Explanation

Find $\Psi(10^{18}) \bmod 101001001$ where $\Psi(k)$ is the sum of squares of the $k+1$ Fibonacci subwords of length $k$.

Using matrix exponentiation and subword structure of the Sturmian Fibonacci word.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log K)$ matrix exponentiation.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory.
