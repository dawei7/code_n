# Maximum Sum Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2736 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Stack, Binary Indexed Tree, Segment Tree, Sorting, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-sum-queries](https://leetcode.com/problems/maximum-sum-queries/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-sum-queries/).

### Goal
Given two integer arrays `nums1` and `nums2` of length $n$, and a 2D array `queries` where each query is represented as `[xi, yi]`, find the maximum sum `nums1[j] + nums2[j]` for any index $j$ ($0 \le j < n$) such that `nums1[j] >= xi` and `nums2[j] >= yi`.

If no such index $j$ exists for a query, the answer for that query should be `-1`. Return an array containing the answers to all queries in their original order.

### Function Contract
**Inputs**
- `nums1`: `List[int]`, an array of integers of length $n$.
- `nums2`: `List[int]`, an array of integers of length $n$.
- `queries`: `List[List[int]]`, a list of queries where each query is a pair of integers `[xi, yi]`.

**Return value**
- `List[int]`, an array of size `len(queries)` containing the maximum sum for each query, or `-1` if no valid index exists.

### Examples
**Example 1**
- Input: `nums1 = [4,3,1,2]`, `nums2 = [2,4,9,5]`, `queries = [[4,1],[1,3],[2,5]]`
- Output: `[6,10,7]`

**Example 2**
- Input: `nums1 = [3,2,5]`, `nums2 = [2,1,5]`, `queries = [[4,1],[1,4],[2,5]]`
- Output: `[10,10,10]`

**Example 3**
- Input: `nums1 = [2,1]`, `nums2 = [3,4]`, `queries = [[3,3]]`
- Output: `[-1]`

---

## Solution
### Approach
The problem can be solved efficiently using an offline query processing strategy combined with a monotonic stack and binary search.

1. **Offline Processing**: Since the queries do not depend on each other, we can sort both the pairs `(nums1[j], nums2[j])` and the queries in descending order of their first coordinate ($x$). This allows us to process queries such that the set of candidate pairs satisfying the condition `nums1[j] >= xi` only grows.
2. **Monotonic Stack**: As we iterate through the sorted queries, we insert all valid pairs into a monotonic stack. The stack maintains pairs of `(y, sum)` where `sum = x + y`. To optimize queries, we keep the stack sorted such that as $y$ increases, the sum strictly decreases. Any pair that is dominated by another pair (i.e., has both smaller or equal $y$ and smaller or equal sum) is discarded.
3. **Binary Search**: For each query `(xi, yi)`, after inserting all valid pairs with `x >= xi`, we can find the maximum sum for `y >= yi` by performing a binary search on the monotonic stack. Since the stack is sorted by $y$ ascending, the first element with $y >= yi$ will have the maximum sum in the valid suffix.

### Complexity Analysis
- **Time Complexity**: $O((N + Q) \log N + Q \log Q)$ where $N$ is the length of `nums1` and `nums2`, and $Q$ is the number of queries. Sorting the pairs takes $O(N \log N)$ time, and sorting the queries takes $O(Q \log Q)$ time. Each pair is pushed and popped from the monotonic stack at most once, taking $O(N)$ total time. For each of the $Q$ queries, we perform a binary search on the stack of size at most $N$, which takes $O(\log N)$ time.
- **Space Complexity**: $O(N + Q)$ to store the sorted pairs, the sorted queries with their original indices, the monotonic stack, and the final answer array.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
    # Pair up nums1 and nums2 and sort them by nums1 descending
    pairs = sorted(zip(nums1, nums2), key=lambda x: x[0], reverse=True)

    # Sort queries by xi descending, keeping track of original indices
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][0], reverse=True)

    ans = [-1] * len(queries)
    stack = []  # Will store tuples of (y, x + y)
    pair_idx = 0
    n = len(pairs)

    for q_idx, (xi, yi) in sorted_queries:
        # Add all pairs with x >= xi to the monotonic stack
        while pair_idx < n and pairs[pair_idx][0] >= xi:
            x, y = pairs[pair_idx]
            val = x + y
            # Maintain monotonic stack: y ascending, val descending
            while stack and stack[-1][1] <= val:
                stack.pop()
            if not stack or stack[-1][0] < y:
                stack.append((y, val))
            pair_idx += 1

        # Binary search for the first element in stack with y >= yi
        low = 0
        high = len(stack) - 1
        best_val = -1
        while low <= high:
            mid = (low + high) // 2
            if stack[mid][0] >= yi:
                best_val = stack[mid][1]
                high = mid - 1
            else:
                low = mid + 1
        ans[q_idx] = best_val

    return ans
```
</details>
