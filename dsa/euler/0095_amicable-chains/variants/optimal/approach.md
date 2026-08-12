# Amicable Chains - Optimal Approach

## Algorithm Explanation

Find the smallest element in the longest non-exceeding amicable chain below $1,000,000$.

An amicable chain is a sequence where each term is the sum of the proper divisors of the previous term, eventually returning to the initial term.

### Two-Phase Strategy:
1. **Proper Divisor Sum Sieve**:
   - Initialize array `sum_div[x] = 0` for $x \le 1,000,000$.
   - Iterate $i \in [1, 500,000]$ and add $i$ to all multiples $j = 2i, 3i \dots$.
2. **Cycle Detection Trajectory Tracing**:
   - Maintain a boolean `visited` lookup array.
   - For unvisited starting terms $i$, follow $x \leftarrow \text{sum\_div}[x]$ until $x > 10^6$, $x = 0$, or a cycle is detected.
   - For valid cycles, compute cycle length and update the global maximum chain length and minimum cycle element.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ where $N = 1000000$. Runs in $< 0.45\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Sieve and visited arrays.
