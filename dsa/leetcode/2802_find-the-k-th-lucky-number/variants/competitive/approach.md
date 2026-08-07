## General
**Competitive Approach — Find The K-th Lucky Number**

The solution implements an direct algorithm tailored for Find The K-th Lucky Number. Key implementation techniques include Bitwise manipulation (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `kthLuckyNumber`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(log k)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(log k)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
