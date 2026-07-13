# Minimum Difference Between Largest and Smallest Value in Three Moves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1509 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-difference-between-largest-and-smallest-value-in-three-moves](https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/).

### Goal
Change at most three array elements to any values so the difference between the
largest and smallest remaining values is as small as possible.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

The minimum possible `max(nums) - min(nums)` after at most three changes.

### Examples
**Example 1**

- Input: `nums = [5, 3, 2, 4]`
- Output: `0`

**Example 2**

- Input: `nums = [1, 5, 0, 10, 14]`
- Output: `1`

**Example 3**

- Input: `nums = [6, 6, 0, 1, 1, 4, 6]`
- Output: `2`

---

## Solution
### Approach
If the array has four or fewer values, all extremes can be neutralized, so the
answer is `0`. Otherwise sort the array and try the four ways to spend three
moves across the smallest and largest ends: change three largest, two largest
and one smallest, one largest and two smallest, or three smallest. Take the
minimum remaining spread.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`.
- **Space Complexity**: `O(1)` extra space if sorting in place.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums):
    if len(nums) <= 4:
        return 0
    nums = sorted(nums)
    return min(nums[-4 + i] - nums[i] for i in range(4))
```
</details>
