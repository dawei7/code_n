# Maximum Frequency of an Element After Performing Operations I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3346 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-frequency-of-an-element-after-performing-operations-i](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/).

### Goal
Given an array of integers, you are allowed to modify each element at most once by adding or subtracting a value up to `k`. Additionally, you can perform at most `numOperations` total modifications across the entire array. The objective is to determine the maximum possible frequency of any single integer after these operations are applied.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `k`: An integer representing the maximum range of modification for each element.
- `numOperations`: An integer representing the maximum number of elements that can be modified.

**Return value**

- An integer representing the maximum frequency of any value after performing at most `numOperations` modifications.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], k = 1, numOperations = 1`
- Output: `2`

**Example 2**

- Input: `nums = [1, 4, 8, 13], k = 5, numOperations = 3`
- Output: `3`

**Example 3**

- Input: `nums = [9, 11, 12, 15], k = 2, numOperations = 0`
- Output: `1`

---

## Solution
### Approach
The problem is solved using a combination of **Frequency Counting** and **Difference Arrays (Sweep Line)**. Since we want to find a target value `x` that maximizes frequency, we observe that any `nums[i]` can become `x` if `|nums[i] - x| <= k`. This defines an interval `[nums[i] - k, nums[i] + k]` where `x` could potentially be formed. By using a difference array, we track how many numbers can reach a specific value `x` without modification (original frequency) versus how many require an operation. We then iterate through all possible candidate values to find the maximum frequency.

### Complexity Analysis
- **Time Complexity**: `O(N log N)` due to sorting the unique values and processing the difference array, where `N` is the length of the input array.
- **Space Complexity**: `O(N)` to store the frequency map and the difference array coordinates.

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
