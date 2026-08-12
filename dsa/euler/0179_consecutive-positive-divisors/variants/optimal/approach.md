# Consecutive Positive Divisors - Optimal Approach

## Algorithm Explanation

Find the total number of integers $1 < n < 10^7$ such that $n$ and $n + 1$ have the same number of positive divisors ($d(n) = d(n+1)$).

### Sieve Divisor Counting:
1. **Divisor Array Pre-filling**:
   Initialize integer array `div_count` of size $N + 1$ ($N = 10^7$).
   Iterate step size $i \in [1, N]$:
   - For all multiples $j \in [i, N]$ with step $i$: `div_count[j] += 1`
2. **Consecutive Equal Matching**:
   Iterate $n \in [2, N - 1]$:
   - Increment count whenever `div_count[n] == div_count[n + 1]`.

For $N = 10^7$, total harmonic sieve steps $\sum_{i=1}^N \frac{N}{i} \approx N \ln N \approx 1.6 \times 10^8$ ops.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ where $N = 10^7$. Runs in $\approx 15\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Integer divisor count array.
