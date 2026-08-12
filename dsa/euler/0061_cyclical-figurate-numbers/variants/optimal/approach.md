# Cyclical Figurate Numbers - Optimal Approach

## Algorithm Explanation

Find the sum of six 4-digit cyclic numbers representing each polygonal type: Triangle ($P_3$), Square ($P_4$), Pentagonal ($P_5$), Hexagonal ($P_6$), Heptagonal ($P_7$), and Octagonal ($P_8$).

### Backtracking Strategy:
1. Pre-generate all $4$-digit numbers ($1000 \le V \le 9999$) for each polygonal type $k \in [3 \dots 8]$, storing `(val, prefix_2, suffix_2)`.
2. Fix $P_8$ (Octagonal numbers) as the chain starting point to break cycle rotation symmetry.
3. Perform Depth-First Search (DFS):
   - Match current element's suffix with next element's prefix (`curr_suffix == next_prefix`).
   - Ensure each polygonal type $3 \dots 8$ is selected exactly once.
   - Validate cycle closure: `chain[-1].suffix == chain[0].prefix`.
4. Sum the $6$ cyclic numbers.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(5! \cdot K)$ with aggressive prefix matching pruning. Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary stack memory.
