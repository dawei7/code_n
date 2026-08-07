## General
**Competitive Approach — Minimum Cost to Convert String II**

The solution employs Sequential iteration scanning input elements and dynamically updating state. It utilizes Hash Map / Dictionary for $O(1)$ average lookup and frequency tracking, Priority Queue / Min-Heap (`heapq`) for dynamic minimum/maximum extraction, Dynamic Programming table / Memoization store to reuse intermediate subproblem results to maintain optimal runtime bounds. Key implementation techniques include Bitwise manipulation (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `minimumCost`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(M^3 + N^2 + S)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(M^2 + N + S)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
