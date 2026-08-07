## General
**Competitive Approach — Find the Count of Numbers Which Are Not Special**

The solution employs Two-Pointer technique iterating from opposing ends or maintaining a sliding window bound.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `linear_sieve_of_eratosthenes`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(sqrt(r) log log sqrt(r))$ — Operation count proportional to input scale.
- **Space Complexity**: $O(sqrt(r))$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
