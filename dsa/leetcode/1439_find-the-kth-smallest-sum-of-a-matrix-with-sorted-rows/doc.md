# Find the Kth Smallest Sum of a Matrix With Sorted Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1439 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/).

### Goal
Given a matrix whose rows are sorted in non-decreasing order, choose exactly one value from each row. Return the `k`th smallest possible sum among all such choices.

### Function Contract
**Inputs**

- `mat`: a row-sorted integer matrix.
- `k`: the one-based rank of the desired sum.

**Return value**

The `k`th smallest row-pick sum.

### Examples
**Example 1**

- Input: `mat = [[1,3,11],[2,4,6]], k = 5`
- Output: `7`

**Example 2**

- Input: `mat = [[1,3,11],[2,4,6]], k = 9`
- Output: `17`

**Example 3**

- Input: `mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7`
- Output: `9`

---

## Solution
### Approach
Iterative k-way merge with a bounded heap/list. Maintain the smallest `k` sums after processing each row by combining the current candidates with that row and truncating back to `k`.

### Complexity Analysis
- **Time Complexity**: `O(m * k * n log(k n))` for `m` rows and `n` columns with straightforward bounded merging.
- **Space Complexity**: `O(k n)` during each merge, reducible to `O(k)` with heap pruning.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq


def solve(mat, k):
    sums = [0]
    for row in mat:
        if not isinstance(row, list):
            row = [row]
        row = sorted(row)
        merged = []
        for base in sums:
            for value in row:
                merged.append(base + value)
        sums = heapq.nsmallest(max(1, k), merged)
    return sorted(sums)[max(0, min(k, len(sums)) - 1)] if sums else 0
```
</details>
