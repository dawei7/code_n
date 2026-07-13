# Minimum Number of Increments on Subarrays to Form a Target Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1526 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-increments-on-subarrays-to-form-a-target-array](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/).

### Goal
Starting from an all-zero array, each operation increments every value in one
chosen contiguous subarray by `1`. Find the fewest operations needed to build
`target`.

### Function Contract
**Inputs**

- `target`: the desired array of positive integers.

**Return value**

The minimum number of increment-subarray operations.

### Examples
**Example 1**

- Input: `target = [1, 2, 3, 2, 1]`
- Output: `3`

**Example 2**

- Input: `target = [3, 1, 1, 2]`
- Output: `4`

**Example 3**

- Input: `target = [3, 1, 5, 4, 2]`
- Output: `7`

---

## Solution
### Approach
Every increase above the previous height must start new operations at that
position. Add `target[0]`, then for each later index add
`max(0, target[i] - target[i - 1])`.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(target):
    if not target:
        return 0
    total = max(0, target[0])
    for i in range(1, len(target)):
        if target[i] > target[i - 1]:
            total += target[i] - target[i - 1]
    return total
```
</details>
