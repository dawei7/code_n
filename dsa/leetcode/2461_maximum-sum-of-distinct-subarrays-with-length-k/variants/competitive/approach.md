## General
**Competitive Approach — Maximum Sum of Distinct Subarrays With Length K**

The solution employs Sequential iteration scanning input elements and dynamically updating state. It utilizes Hash Set for $O(1)$ existence checks and duplicate elimination to maintain optimal runtime bounds.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `maximumSubarraySum`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(k)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
