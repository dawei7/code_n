# Zero Array Transformation I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3355 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [zero-array-transformation-i](https://leetcode.com/problems/zero-array-transformation-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/zero-array-transformation-i/).

### Goal
Given an array of non-negative integers `nums` and a 2D array of range queries `queries` where each query is represented as `[l, r]`, you can choose to decrement any subset of elements within the index range `[l, r]` by at most 1 for each query.

Determine if it is possible to transform the entire `nums` array into an all-zero array (where every element is less than or equal to 0) after applying a subset of decrements from the given queries.

### Function Contract
**Inputs**

- `nums`: `List[int]` — An array of non-negative integers of length $n$.
- `queries`: `List[List[int]]` — A 2D array where each element `queries[i] = [l_i, r_i]` represents a range of indices.

**Return value**

- `bool` — Returns `True` if `nums` can be successfully transformed into an all-zero array, and `False` otherwise.

### Examples
**Example 1**

- Input: `nums = [1, 0, 1]`, `queries = [[0, 2]]`
- Output: `True`
- Explanation: For the query `[0, 2]`, we can choose to decrement the elements at indices 0 and 2. The array becomes `[0, 0, 0]`.

**Example 2**

- Input: `nums = [4, 3, 2, 1]`, `queries = [[1, 3], [0, 2], [0, 1]]`
- Output: `False`
- Explanation:
  - Index 0 is covered by queries `[0, 2]` and `[0, 1]` (a maximum of 2 decrements).
  - Since `nums[0] = 4` and we can decrement it at most 2 times, it is impossible to reduce it to 0.

---

## Solution
### Approach
The problem asks if we can decrement each element `nums[i]` to `0`. Since each query `[l, r]` allows us to independently choose whether or not to decrement any element within that range, the decisions for each index are completely independent.

Thus, the problem simplifies to: **Is the total number of queries covering index $i$ greater than or equal to `nums[i]` for all $0 \le i < n$?**

To solve this efficiently:
1. **Difference Array (Prefix Sum Technique)**:
   Instead of updating the range `[l, r]` for each query in $O(N)$ time, we can use a difference array `diff` of size $n + 1$.
   - For each query `[l, r]`, we increment `diff[l]` by 1 and decrement `diff[r + 1]` by 1.
2. **Reconstruction**:
   We compute the running prefix sum of the `diff` array. The prefix sum at index $i$ represents the total number of queries covering index $i$.
3. **Validation**:
   If at any index $i$, the coverage (running prefix sum) is strictly less than `nums[i]`, it is impossible to reduce `nums[i]` to 0, so we return `False`. If all indices are sufficiently covered, we return `True`.

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N + Q)$ where $N$ is the length of `nums` and $Q$ is the number of queries. We iterate through the queries once to populate the difference array, and then perform a single linear scan over `nums` to validate the coverage.
- **Space Complexity**: $\mathcal{O}(N)$ auxiliary space to store the difference array of size $N + 1$.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], queries: List[List[int]]) -> bool:
    n = len(nums)
    diff = [0] * (n + 1)

    # Populate the difference array
    for l, r in queries:
        diff[l] += 1
        diff[r + 1] -= 1

    # Compute prefix sums on the fly and validate coverage
    curr_coverage = 0
    for i in range(n):
        curr_coverage += diff[i]
        if curr_coverage < nums[i]:
            return False

    return True
```
</details>
