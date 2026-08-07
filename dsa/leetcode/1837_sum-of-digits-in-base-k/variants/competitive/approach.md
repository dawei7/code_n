## General
**Competitive Approach — Sum of Digits in Base K**

The solution implements an direct algorithm tailored for Sum of Digits in Base K.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `sumBase`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(\log_k n)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
