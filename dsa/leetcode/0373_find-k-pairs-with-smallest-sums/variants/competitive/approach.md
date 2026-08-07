## General
**Competitive Approach — Find K Pairs with Smallest Sums**

The solution employs Sequential iteration scanning input elements and dynamically updating state. It utilizes Double-ended queue (`collections.deque`) for efficient $O(1)$ element insertion and removal, Priority Queue / Min-Heap (`heapq`) for dynamic minimum/maximum extraction to maintain optimal runtime bounds.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `kSmallestPairs`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(k \log \min(k,m))$ — Operation count proportional to input scale.
- **Space Complexity**: $O(\min(k,m))$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
