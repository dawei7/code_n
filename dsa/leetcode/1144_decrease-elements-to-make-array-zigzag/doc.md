# Decrease Elements To Make Array Zigzag

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1144 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [decrease-elements-to-make-array-zigzag](https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/).

### Goal
Decrease array elements by one per operation until the array alternates between valleys and peaks. Return the fewest operations needed.

### Function Contract
**Inputs**

- `nums`: integer array.

**Return value**

The minimum number of decrement operations needed so that either all even indices are valleys or all odd indices are valleys.

### Examples
**Example 1**

- Input: `nums = [1,2,3]`
- Output: `2`

**Example 2**

- Input: `nums = [9,6,1,6,2]`
- Output: `4`

**Example 3**

- Input: `nums = [2,1,2]`
- Output: `0`

---

## Solution
### Approach
Greedy local adjustment.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums):
    n = len(nums)

    def cost_for_valleys(parity):
        total = 0
        for i, value in enumerate(nums):
            if i % 2 != parity:
                continue
            limit = float("inf")
            if i > 0:
                limit = min(limit, nums[i - 1])
            if i + 1 < n:
                limit = min(limit, nums[i + 1])
            if value >= limit:
                total += value - limit + 1
        return total

    return min(cost_for_valleys(0), cost_for_valleys(1))
```
</details>
