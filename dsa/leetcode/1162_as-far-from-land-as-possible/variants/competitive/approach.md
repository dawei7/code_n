## General
**Competitive Approach — As Far from Land as Possible**

The solution employs Breadth-First Search (BFS) using queue-based level-order traversal. It utilizes Double-ended queue (`collections.deque`) for efficient $O(1)$ element insertion and removal to maintain optimal runtime bounds.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `maxDistance`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(n^2)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
