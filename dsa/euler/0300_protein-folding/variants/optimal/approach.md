# Protein Folding - Optimal Approach

## Algorithm Explanation

Find the average number of H-H contact points in an optimal 2D lattice folding of a random Hydrophobic-Polar (HP) protein string of length $n = 15$.

### 2D Self-Avoiding Walk (SAW) Contact Bitmask Enumeration:
1. **Self-Avoiding Walk Generation**:
   We precompute all 2D self-avoiding walks of length $15$ up to spatial symmetry.
2. **Contact Graph Bitmask Representation**:
   For each walk, non-adjacent lattice neighbors $(i, j)$ ($|i - j| > 1$) form potential H-H contact edges.
   Each walk is represented by a bitmask of potential contact pairs.
3. **Exact Expectation Evaluation**:
   For all $2^{15} = 32768$ binary HP protein strings, we find the maximum number of active H-H contacts over all precomputed walks.
4. **Execution**:
   Summing max H-H contacts across all $2^{15}$ strings and dividing by $32768$ yields the exact average $8.0540771484375$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{SAWs} \cdot 2^N)$ for $N = 15$ and $\approx 100\,000$ SAWs. Runs in $\approx 2.10\text{s}$.
- **Space Complexity:** $\mathcal{O}(\text{SAWs})$ contact mask list.
