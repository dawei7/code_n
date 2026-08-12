# Non-Abundant Sums - Optimal Approach

## Algorithm Explanation

A number $n$ is **abundant** if the sum of its proper divisors exceeds $n$. All integers $> 28123$ can be expressed as the sum of two abundant numbers.

1. Compute proper divisor sums for $1 \le n \le 28123$ using an $\mathcal{O}(N \log N)$ divisor sieve.
2. Identify all abundant numbers $A = \{n \mid \text{div\_sum}[n] > n\}$.
3. Use a boolean array `is_abundant_sum` to mark all pair sums $a + b \le 28123$ for $a, b \in A$.
4. Sum all integers $1 \le i \le 28123$ for which `is_abundant_sum[i]` is `False`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N + K^2)$ where $N = 28123$ and $K = |A| = 6965$. Runs in under $0.5\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Memory for divisor array and boolean lookup table.
