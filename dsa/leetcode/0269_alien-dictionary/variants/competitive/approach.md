## General
**Competitive Approach — Alien Dictionary**

The solution employs Depth-First Search (DFS) / Backtracking to recursively explore state choices. It utilizes Hash Map / Dictionary for $O(1)$ average lookup and frequency tracking, Hash Set for $O(1)$ existence checks and duplicate elimination, Double-ended queue (`collections.deque`) for efficient $O(1)$ element insertion and removal to maintain optimal runtime bounds. Key implementation techniques include Bitwise manipulation (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `alienOrder`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(c + e)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(a + e)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
