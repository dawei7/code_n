# Count Number of Nice Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1248 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-number-of-nice-subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-number-of-nice-subarrays/).

### Goal
Count contiguous subarrays containing exactly `k` odd numbers.

### Function Contract
**Inputs**

- `nums`: integer array.
- `k`: required number of odd elements.

**Return value**

The number of subarrays with exactly `k` odd values.

### Examples
**Example 1**

- Input: `nums = [1,1,2,1,1]`, `k = 3`
- Output: `2`

**Example 2**

- Input: `nums = [2,4,6]`, `k = 1`
- Output: `0`

**Example 3**

- Input: `nums = [2,2,2,1,2,2,1,2,2,2]`, `k = 2`
- Output: `16`

---

## Solution
### Approach
Prefix sum frequency counting.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` in the worst case.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter


def solve(nums, k):
    counts = Counter({0: 1})
    odd_prefix = 0
    answer = 0
    for value in nums:
        odd_prefix += value % 2
        answer += counts[odd_prefix - k]
        counts[odd_prefix] += 1
    return answer
```
</details>
