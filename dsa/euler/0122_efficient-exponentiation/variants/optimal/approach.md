# Efficient Exponentiation - Optimal Approach

## Algorithm Explanation

Find $\sum_{k=1}^{200} m(k)$ where $m(k)$ is the minimum number of multiplications required to compute $n^k$.

### Addition Chain Problem:
Computing $n^k$ in the minimal number of multiplications is equivalent to finding the shortest **addition chain** for $k$:
A sequence $1 = a_0 < a_1 < a_2 < \dots < a_m = k$ where each element $a_i = a_j + a_l$ ($0 \le j \le l < i$).

### Iterative Deepening DFS (IDDFS) & Star Chains:
1. Initialize `min_mults[k] = infinity` for $k \in [1, 200]$.
2. Perform **Iterative Deepening Depth-First Search (IDDFS)** with increasing max depth bound `max_depth = 1, 2, 3 \dots`.
3. Generate **star-chain** additions by combining the latest term `chain[-1]` with any previous element in `chain`.
4. Prune branches where $a_{next} > 200$ or current depth $\ge \text{min\_mults}[a_{next}]$.
5. Stop IDDFS when all $m(k)$ for $k \le 200$ have been determined. Sum $m(k)$ for $k = 1 \dots 200$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{IDDFS Tree})$ with depth bound $M \le 11$. Runs in $< 0.18\text{s}$.
- **Space Complexity:** $\mathcal{O}(M)$ - Stack depth memory.
