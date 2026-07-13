# Maximum Frequency of an Element After Performing Operations II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3347 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-frequency-of-an-element-after-performing-operations-ii](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/).

### Goal
Given an array of integers `nums`, an integer `k`, and an integer `numOperations`, you can modify at most `numOperations` elements in the array. For each chosen element, you can change its value to any integer `x` such that `|nums[i] - x| <= k`. The objective is to find the maximum possible frequency of any single integer after performing at most `numOperations` such modifications.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `k`: An integer representing the maximum allowed distance for modification.
- `numOperations`: An integer representing the maximum number of elements that can be modified.

**Return value**

- An integer representing the maximum frequency of any value after performing the operations.

### Examples
**Example 1**

- Input: `nums = [1, 4, 5], k = 1, numOperations = 2`
- Output: `2`

**Example 2**

- Input: `nums = [1, 2, 6, 10], k = 1, numOperations = 1`
- Output: `2`

**Example 3**

- Input: `nums = [10, 12, 11, 13, 14], k = 1, numOperations = 3`
- Output: `5`

---

## Solution
### Approach
The problem is solved using a combination of **Difference Arrays** (or coordinate compression/sweep-line) and **Sliding Window**. Since we want to find a target value `x` that maximizes frequency, we observe that any `x` will be "covered" by an original `nums[i]` if `nums[i] - k <= x <= nums[i] + k`. We use a difference array to track how many elements can reach a specific value `x` without using an operation, and how many can reach it using one operation. By sliding a window of size `2k + 1` over the sorted unique values, we calculate the maximum frequency efficiently.

### Complexity Analysis
- **Time Complexity**: `O(N log N)` due to sorting the input array and processing the unique intervals.
- **Space Complexity**: `O(N)` to store the difference array and the sorted unique values.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter


def solve(nums: list[int], k: int, numOperations: int) -> int:
    counts = Counter(nums)
    events = []
    candidates = set()

    for value, frequency in counts.items():
        left = value - k
        right = value + k
        events.append((left, frequency))
        events.append((right + 1, -frequency))
        candidates.add(left)
        candidates.add(right)
        candidates.add(value)

    events.sort()
    event_index = 0
    reachable = 0
    best = 0

    for target in sorted(candidates):
        while event_index < len(events) and events[event_index][0] <= target:
            reachable += events[event_index][1]
            event_index += 1
        unchanged = counts.get(target, 0)
        best = max(best, unchanged + min(numOperations, reachable - unchanged))

    return best
```
</details>
