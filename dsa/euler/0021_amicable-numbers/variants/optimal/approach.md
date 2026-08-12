# Amicable Numbers - Optimal Approach

## Algorithm Explanation

Two distinct numbers $a$ and $b$ are an **amicable pair** if $d(a) = b$ and $d(b) = a$, where $d(n)$ is the sum of proper divisors of $n$.

1. Precompute proper divisor sum $d(i)$ for all $1 \le i < 10000$.
2. For each $a < 10000$, let $b = d(a)$.
3. If $a \ne b$, $b < 10000$, and $d(b) == a$, then $a$ is an amicable number.
4. Sum all valid $a$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \sqrt{N})$ where $N = 10000$. Runs in under $0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Precomputed array of $d(i)$ values.
