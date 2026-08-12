# Ordered Radicals - Optimal Approach

## Algorithm Explanation

Find $E(10000)$, the $10000^{\text{th}}$ element when integers $1 \le n \le 100000$ are sorted primarily by radical value $\operatorname{rad}(n)$ and secondarily by $n$.

### Radical Definition & Sieve:
The radical $\operatorname{rad}(n)$ is the product of distinct prime factors dividing $n$.

1. **Radical Sieve**:
   - Initialize array `rad[x] = 1` for $x \in [1, 100000]$.
   - For each prime $p \le 100000$ (`rad[p] == 1`), multiply `rad[j] *= p` for all multiples $j = p, 2p, 3p \dots$.
2. **Tuple Sorting**:
   - Construct pairs $(\operatorname{rad}(n), n)$ for $n \in [1, 100000]$.
   - Sort tuples lexicographically.
3. Return the $n$-value of the $10000^{\text{th}}$ element (0-indexed position $9999$).

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ where $N = 100000$. Runs in $< 0.08\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Radical array and tuple list.
