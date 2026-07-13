# Find Two Non-overlapping Sub-arrays Each With Target Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1477 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-two-non-overlapping-sub-arrays-each-with-target-sum](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/).

### Goal
Find two non-overlapping contiguous subarrays whose sums both equal `target`, minimizing the total of their lengths.

### Function Contract
**Inputs**

- `arr`: a list of positive integers.
- `target`: the required subarray sum.

**Return value**

The minimum combined length, or `-1` if two such non-overlapping subarrays do not exist.

### Examples
**Example 1**

- Input: `arr = [3,2,2,4,3], target = 3`
- Output: `2`

**Example 2**

- Input: `arr = [7,3,4,7], target = 7`
- Output: `2`

**Example 3**

- Input: `arr = [4,3,2,6,2,3,4], target = 6`
- Output: `-1`

---

## Solution
### Approach
Sliding window plus best-prefix DP. As each target-sum window ends, combine its length with the shortest valid window ending before it, then update the best length seen so far.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for prefix best lengths.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(arr, target):
    best_left = [10**9] * len(arr)
    seen = {0: -1}
    prefix = 0
    best = 10**9
    answer = 10**9
    for index, value in enumerate(arr):
        prefix += value
        need = prefix - target
        if need in seen:
            start = seen[need] + 1
            length = index - seen[need]
            if start > 0 and best_left[start - 1] < 10**9:
                answer = min(answer, length + best_left[start - 1])
            best = min(best, length)
        best_left[index] = best
        seen[prefix] = index
    return -1 if answer == 10**9 else answer
```
</details>
