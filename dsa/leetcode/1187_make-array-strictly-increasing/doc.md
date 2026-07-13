# Make Array Strictly Increasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1187 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [make-array-strictly-increasing](https://leetcode.com/problems/make-array-strictly-increasing/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/make-array-strictly-increasing/).

### Goal
Replace any elements of `arr1` with elements chosen from `arr2` so that `arr1` becomes strictly increasing. Each replacement costs one operation. Return the minimum number of operations.

### Function Contract
**Inputs**

- `arr1`: the array that must become strictly increasing.
- `arr2`: replacement values that may be reused only as selected values during operations.

**Return value**

The minimum number of replacements needed, or `-1` if no strictly increasing result is possible.

### Examples
**Example 1**

- Input: `arr1 = [1,5,3,6,7]`, `arr2 = [1,3,2,4]`
- Output: `1`

**Example 2**

- Input: `arr1 = [1,5,3,6,7]`, `arr2 = [4,3,1]`
- Output: `2`

**Example 3**

- Input: `arr1 = [1,5,3,6,7]`, `arr2 = [1,6,3,3]`
- Output: `-1`

---

## Solution
### Approach
Dynamic programming with ordered states and binary search.

### Complexity Analysis
- **Time Complexity**: `O(n * s * log m)` where `s` is the number of live DP states and `m = len(unique(arr2))`.
- **Space Complexity**: `O(s)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from bisect import bisect_right


def solve(arr1, arr2):
    candidates = sorted(set(arr2))
    states = {-1: 0}
    for value in arr1:
        next_states = {}
        for previous, operations in states.items():
            if value > previous:
                next_states[value] = min(next_states.get(value, float("inf")), operations)
            index = bisect_right(candidates, previous)
            if index < len(candidates):
                replacement = candidates[index]
                next_states[replacement] = min(next_states.get(replacement, float("inf")), operations + 1)
        states = next_states
        if not states:
            return -1
    return min(states.values())
```
</details>
