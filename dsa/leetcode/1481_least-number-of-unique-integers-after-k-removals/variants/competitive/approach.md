## General
**Competitive Approach — Least Number of Unique Integers after K Removals**

The solution employs Sequential iteration scanning input elements and dynamically updating state. It utilizes Hash Map / Dictionary for $O(1)$ average lookup and frequency tracking to maintain optimal runtime bounds.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `findLeastNumOfUniqueInts`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(N \log U)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(U)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
