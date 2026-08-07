## General
**Competitive Approach — Count Nodes That Are Great Enough**

The solution employs Binary Search over a sorted range or search space, continuously halving the candidate window. It utilizes Binary Tree node traversal (`val`, `left`, `right`) to maintain optimal runtime bounds.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `__init__`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(nk)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(nk)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
