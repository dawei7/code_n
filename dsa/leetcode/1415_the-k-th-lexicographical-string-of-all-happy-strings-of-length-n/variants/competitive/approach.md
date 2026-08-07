## General
**Competitive Approach — The k-th Lexicographical String of All Happy Strings of Length n**

The solution implements an direct algorithm tailored for The k-th Lexicographical String of All Happy Strings of Length n.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `getHappyString`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
