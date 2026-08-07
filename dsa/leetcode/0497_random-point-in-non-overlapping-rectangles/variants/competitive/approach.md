## General
**Competitive Approach — Random Point in Non-overlapping Rectangles**

The solution employs Sequential iteration scanning input elements and dynamically updating state. Key implementation techniques include Functional Python iterators (`zip`, `map`, `filter`) for concise element pair evaluation.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `__init__`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(r + d \log r)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(r + d)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
