# Skew-cost Coding - Optimal Approach

## Algorithm Explanation

Find the minimum total cost $\operatorname{Cost}(10^9)$ of a prefix-free code of size $10^9$, where bit `'0'` costs $1$ penny and bit `'1'` costs $4$ pence.

### Greedy Huffman Leaf-Expansion:
1. **Tree Expansion Recurrence**:
   Expanding a leaf node of cost $C$ replaces it with two children of costs $C + 1$ and $C + 4$.
   The net size increases by $1$, and the total code cost increases by $C + 5$.
2. **Batch Greedy Expansion**:
   To minimize total cost, we always expand leaves of the current minimum cost $C$.
   Maintaining leaf counts `count[C]` allows expanding all leaves of cost $C$ in a single batch.
3. **Execution**:
   Expanding batches until total size reaches $N = 10^9$ takes $< 50$ iterations, yielding $\operatorname{Cost}(10^9) = 64564225042$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_\phi N)$ where $\phi \approx 1.38$ is the growth factor. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log_\phi N)$ map storage.
