## General
**Competitive Approach — Cut Off Trees for Golf Event**

The solution employs Breadth-First Search (BFS) using queue-based level-order traversal. It utilizes Hash Set for $O(1)$ existence checks and duplicate elimination, Double-ended queue (`collections.deque`) for efficient $O(1)$ element insertion and removal, Priority Queue / Min-Heap (`heapq`) for dynamic minimum/maximum extraction to maintain optimal runtime bounds.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `cutOffTree`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(T \log T + TRC)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(RC)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
