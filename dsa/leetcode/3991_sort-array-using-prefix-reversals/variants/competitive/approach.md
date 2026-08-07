## General
**Competitive Approach — Sort Array Using Prefix Reversals**

The solution employs Two-Pointer technique iterating from opposing ends or maintaining a sliding window bound. It utilizes Hash Set for $O(1)$ existence checks and duplicate elimination to maintain optimal runtime bounds.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `sortArray`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(Pqn)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(Pn)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
