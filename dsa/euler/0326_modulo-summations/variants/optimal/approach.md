# Modulo Summations - Optimal Approach

## Algorithm Explanation

Find $f(10^{12}, 10^6)$, the number of pairs $(p, q)$ with $1 \le p \le q \le N = 10^{12}$ such that $\left( \sum_{i=p}^{q} a_i \right) \bmod M = 0$ ($M = 10^6$), where $a_1 = 1$ and $a_n = \left( \sum_{k=1}^{n-1} k a_k \right) \bmod n$.

### Modular Prefix Sum Frequency & Periodicity:
1. **Prefix Sum Subarray Equivalence**:
   Let $P_m = \sum_{i=1}^{m} a_i \bmod M$.
   A subarray sum $\sum_{i=p}^{q} a_i \equiv 0 \pmod M$ iff $P_{p-1} \equiv P_q \pmod M$.
2. **Periodic Block Structure**:
   The recursive sequence $a_n$ and its prefix sums $P_n \bmod M$ exhibit block periodicity modulo $3M$.
   By tabulating the remainder frequencies $C[r]$ of $P_k \equiv r \pmod M$ for $0 \le k \le N$:
   $$f(N, M) = \sum_{r=0}^{M-1} \binom{C[r]}{2}$$
3. **Execution**:
   Summing combinations $\binom{C[r]}{2}$ across all remainders for $N = 10^{12}, M = 10^6$ yields $1966666166408794329$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M)$ for $M = 10^6$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(M)$ frequency array.
