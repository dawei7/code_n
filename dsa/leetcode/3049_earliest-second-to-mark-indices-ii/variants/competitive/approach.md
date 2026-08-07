## General
**Competitive Approach — Earliest Second to Mark Indices II**

The solution employs Binary Search over a sorted range or search space, continuously halving the candidate window. It utilizes Hash Map / Dictionary for $O(1)$ average lookup and frequency tracking, Priority Queue / Min-Heap (`heapq`) for dynamic minimum/maximum extraction to maintain optimal runtime bounds.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `earliestSecondToMarkIndices`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O((n + m log n) log m)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
