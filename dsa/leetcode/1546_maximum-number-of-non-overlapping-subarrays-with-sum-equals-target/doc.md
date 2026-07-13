# Maximum Number of Non-Overlapping Subarrays With Sum Equals Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1546 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-non-overlapping-subarrays-with-sum-equals-target](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/).

### Goal
Find the maximum number of non-overlapping contiguous subarrays whose sum equals
`target`.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `target`: the desired subarray sum.

**Return value**

The largest count of pairwise non-overlapping target-sum subarrays.

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 1, 1], target = 2`
- Output: `2`

**Example 2**

- Input: `nums = [-1, 3, 5, 1, 4, 2, -9], target = 6`
- Output: `2`

**Example 3**

- Input: `nums = [3, 4, 7, 2, -3, 1, 4, 2], target = 7`
- Output: `3`

---

## Solution
### Approach
Scan with prefix sums and a set of prefix sums seen since the end of the last
chosen subarray. If `prefix - target` is present, a valid subarray ends here;
greedily take it, increment the answer, and reset the set so future subarrays do
not overlap.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(n)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums, target):
    seen = {0}
    prefix = 0
    count = 0
    for num in nums:
        prefix += num
        if prefix - target in seen:
            count += 1
            seen = {0}
            prefix = 0
        else:
            seen.add(prefix)
    return count
```
</details>
