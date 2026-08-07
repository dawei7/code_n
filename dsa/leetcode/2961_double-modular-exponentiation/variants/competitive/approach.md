## General
**Competitive Approach — Double Modular Exponentiation**

The solution employs Sequential iteration scanning input elements and dynamically updating state.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `getGoodIndices`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(V(log B + log C))$ — Operation count proportional to input scale.
- **Space Complexity**: $O(V)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
