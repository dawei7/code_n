## General
**Competitive Approach — Longest Uncommon Subsequence I**

The solution implements an direct algorithm tailored for Longest Uncommon Subsequence I.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `findLUSlength`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(|a| + |b|)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
