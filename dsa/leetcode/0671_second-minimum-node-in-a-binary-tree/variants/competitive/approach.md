## General
**Competitive Approach — Second Minimum Node In a Binary Tree**

The solution implements an direct algorithm tailored for Second Minimum Node In a Binary Tree. It utilizes Hash Set for $O(1)$ existence checks and duplicate elimination, Priority Queue / Min-Heap (`heapq`) for dynamic minimum/maximum extraction, Binary Tree node traversal (`val`, `left`, `right`) to maintain optimal runtime bounds.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `findSecondMinimumValue`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(H)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
