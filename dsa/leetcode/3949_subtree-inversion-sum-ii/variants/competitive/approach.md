## General
**Competitive Approach — Subtree Inversion Sum II**

The solution employs Depth-First Search (DFS) / Backtracking to recursively explore state choices. It utilizes Dynamic Programming table / Memoization store to reuse intermediate subproblem results to maintain optimal runtime bounds.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `subtreeInversionSum`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(nk)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(nk)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
