# Maximum Segment Sum After Removals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2382 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Union-Find, Prefix Sum, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-segment-sum-after-removals](https://leetcode.com/problems/maximum-segment-sum-after-removals/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-segment-sum-after-removals/).

### Goal
Given an array of integers and a sequence of removal indices, determine the maximum segment sum of the remaining array after each removal. A segment is defined as a contiguous subarray of non-removed elements. When an element is removed, it effectively splits a segment into two smaller segments (or removes it entirely).

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `removeQueries`: A list of integers representing the indices to be removed sequentially.

**Return value**

- A list of integers where the $i$-th element represents the maximum segment sum after the $i$-th removal.

### Examples
**Example 1**

- Input: `nums = [1, 2, 5, 6, 1], removeQueries = [0, 3, 2, 4, 1]`
- Output: `[14, 7, 2, 2, 0]`

**Example 2**

- Input: `nums = [3, 2, 11, 1], removeQueries = [3, 2, 1, 0]`
- Output: `[16, 5, 3, 0]`

**Example 3**

- Input: `nums = [5, 9, 2], removeQueries = [1, 0, 2]`
- Output: `[5, 2, 0]`

---

## Solution
### Approach
The problem is solved efficiently by processing the removals in **reverse order**. Instead of splitting segments, we start with an empty array and "add" elements back in the order opposite to the queries. This transforms the problem into a **Disjoint Set Union (DSU)** task, where we merge adjacent segments and track the maximum sum dynamically.

### Complexity Analysis
- **Time Complexity**: $O(N \cdot \alpha(N))$, where $N$ is the length of the array and $\alpha$ is the inverse Ackermann function, due to the DSU operations.
- **Space Complexity**: $O(N)$ to store the DSU parent pointers, segment sums, and the status of removed elements.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], remove_queries: list[int]) -> list[int]:
    n = len(nums)
    parent = list(range(n))
    sums = [0] * n
    exists = [False] * n
    ans = [0] * n

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            sums[root_j] += sums[root_i]

    current_max = 0
    results = []

    # Process in reverse: adding elements back
    for i in reversed(range(n)):
        results.append(current_max)
        idx = remove_queries[i]
        exists[idx] = True
        sums[idx] = nums[idx]

        # Check left neighbor
        if idx > 0 and exists[idx - 1]:
            union(idx, idx - 1)
        # Check right neighbor
        if idx < n - 1 and exists[idx + 1]:
            union(idx, idx + 1)

        current_max = max(current_max, sums[find(idx)])

    return results[::-1]
```
</details>
