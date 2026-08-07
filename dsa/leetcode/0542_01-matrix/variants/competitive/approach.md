## General
**Competitive Approach — 01 Matrix**

The solution employs Breadth-First Search (BFS) using queue-based level-order traversal. It utilizes Double-ended queue (`collections.deque`) for efficient $O(1)$ element insertion and removal, Dynamic Programming table / Memoization store to reuse intermediate subproblem results to maintain optimal runtime bounds.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `updateMatrix`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(rows \cdot cols)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(rows \cdot cols)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
