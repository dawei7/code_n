# Minimum Score by Changing Two Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2567 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-score-by-changing-two-elements](https://leetcode.com/problems/minimum-score-by-changing-two-elements/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-score-by-changing-two-elements/).

### Goal
Given an array of integers, you are allowed to modify exactly two elements to any integer value of your choice. The objective is to minimize the "low-high score," defined as the difference between the maximum and minimum values in the array after performing these two modifications.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`) where the length is at least 3.

**Return value**

- An integer representing the minimum possible difference between the maximum and minimum elements after changing at most two elements.

### Examples
**Example 1**

- Input: `nums = [1, 4, 3]`
- Output: `0`
- Explanation: Change 1 and 4 to 3. The array becomes [3, 3, 3], max - min = 0.

**Example 2**

- Input: `nums = [1, 4, 7, 8, 5]`
- Output: `3`
- Explanation: Change 7 and 8 to 5. The array becomes [1, 4, 5, 5, 5], max - min = 4. Alternatively, change 1 and 8 to 5, array becomes [5, 4, 7, 5, 5], max - min = 3.

**Example 3**

- Input: `nums = [1, 50, 75, 100]`
- Output: `25`
- Explanation: Change 1 and 100 to 50 and 75 respectively. The array becomes [50, 50, 75, 75], max - min = 25.

---

## Solution
### Approach
The problem is solved using a Greedy approach combined with Sorting. Since we want to minimize the range (max - min), we should focus on removing the extreme values (the smallest and largest elements). By sorting the array, we can evaluate the three optimal strategies:
1. Remove the two largest elements.
2. Remove the two smallest elements.
3. Remove one smallest and one largest element.

### Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the sorting step, where N is the length of the input array.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the minimum score by changing at most two elements.
    The strategy is to sort the array and compare the range after
    removing the two smallest, two largest, or one of each.
    """
    n = len(nums)
    if n <= 3:
        return 0

    nums.sort()

    # Option 1: Change the two largest elements to match the third largest
    # The range becomes nums[n-3] - nums[0]
    option1 = nums[n - 3] - nums[0]

    # Option 2: Change the two smallest elements to match the third smallest
    # The range becomes nums[n-1] - nums[2]
    option2 = nums[n - 1] - nums[2]

    # Option 3: Change the smallest and the largest elements
    # The range becomes nums[n-2] - nums[1]
    option3 = nums[n - 2] - nums[1]

    return min(option1, option2, option3)
```
</details>
