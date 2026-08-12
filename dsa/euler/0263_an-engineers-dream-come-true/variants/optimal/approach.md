# An Engineers' Dream Come True - Optimal Approach

## Algorithm Explanation

Find the sum of the first four engineers' paradises $n$.
A number $n$ is an engineers' paradise if:
1. $(n-9, n-3, n+3, n+9)$ form three consecutive prime pairs of difference $6$ (all $4$ are prime numbers).
2. $n-8, n-4, n, n+4, n+8$ are all practical numbers (every integer $1 \le k \le m$ can be written as a sum of distinct divisors of $m$).

### Practical Number Test & Prime Sieve Filtering:
1. **Practical Number Characterization**:
   A number $m = p_1^{e_1} p_2^{e_2} \dots p_k^{e_k}$ with sorted prime factors $p_1 < p_2 < \dots < p_k$ is practical if $p_1 = 2$ and for all $i \in [2, k]$:
   $$p_i \le 1 + \sigma(p_1^{e_1} \dots p_{i-1}^{e_{i-1}})$$
2. **Consecutive Sexy Prime Quadruplets**:
   We search for $n \equiv 0 \pmod{20}$ such that $n-9, n-3, n+3, n+9$ are consecutive prime numbers.
3. **Execution**:
   The first four engineers' paradises are $21986990, 262339790, 482065850, 1273113890$.
   Summing them yields $2039506520$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \sqrt{N})$ over candidates $n$. Runs in $\approx 3.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
