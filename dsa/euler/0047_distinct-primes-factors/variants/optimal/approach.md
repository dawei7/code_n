# Distinct Primes Factors - Optimal Approach

## Algorithm Explanation

Find the first integer of four consecutive integers $\{x, x+1, x+2, x+3\}$ that each possess exactly $4$ distinct prime factors.

### Sieve Strategy:
1. Allocate an integer array `factors` up to $N = 200000$.
2. Run a modified Sieve of Eratosthenes: whenever `factors[i] == 0` (indicating $i$ is prime), increment `factors[j]` for all multiples $j = i, 2i, 3i, \dots$.
3. Iterate $i$ sequentially: maintain a streak counter of numbers with `factors[i] == 4`.
4. When streak reaches $4$, return $i - 3$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log \log N)$ where $N = 200000$. Runs in $< 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Factor count lookup array.
