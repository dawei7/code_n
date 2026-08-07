## General
**Competitive Approach — Number of Common Factors**

The solution implements an direct algorithm tailored for Number of Common Factors.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `commonFactors`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(sqrt(g))$ — Operation count proportional to input scale.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
