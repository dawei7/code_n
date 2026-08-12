# Coin Partitions - Optimal Approach

## Algorithm Explanation

Find the smallest integer $n$ for which the partition count $p(n)$ is divisible by $1,000,000$.

### Euler's Pentagonal Number Theorem
Computing $p(n)$ using standard DP requires $\mathcal{O}(n^2)$ time. Using Euler's Pentagonal Recurrence, $p(n)$ is calculated in $\mathcal{O}(\sqrt{n})$ steps per term:
$$p(n) = \sum_{k \ne 0} (-1)^{k-1} p(n - g_k)$$
where $g_k = \frac{k(3k - 1)}{2}$ are generalized pentagonal numbers ($k = 1, -1, 2, -2, 3, -3 \dots$).

1. Maintain array `p` of partition numbers modulo $M = 1000000$.
2. Increment $n = 1, 2, 3 \dots$.
3. Compute $p(n) \bmod M$ using the pentagonal recurrence until $p(n) \equiv 0 \pmod M$.
4. Return $n$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \sqrt{N})$ where $N = 55374$. Runs in $< 0.45\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Modular partition array `p`.
