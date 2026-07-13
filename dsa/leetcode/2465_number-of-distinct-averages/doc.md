# Number of Distinct Averages

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2465 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-distinct-averages](https://leetcode.com/problems/number-of-distinct-averages/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-distinct-averages/).

### Goal
Given an array of even length, repeatedly remove the minimum and maximum elements from the current array, calculate their average, and store it. The objective is to determine how many unique average values are generated through this process until the array is empty.

### Function Contract
**Inputs**

- `nums`: A list of integers where the length is always even.

**Return value**

- An integer representing the count of unique averages calculated.

### Examples
**Example 1**

- Input: `nums = [4,1,4,0,3,5]`
- Output: `2`
- Explanation: Averages are (0+5)/2=2.5, (1+4)/2=2.5, (3+4)/2=3.5. Unique values: {2.5, 3.5}. Count: 2.

**Example 2**

- Input: `nums = [1,100]`
- Output: `1`
- Explanation: Average is (1+100)/2=50.5. Unique values: {50.5}. Count: 1.

**Example 3**

- Input: `nums = [1,1,0,0]`
- Output: `1`
- Explanation: Averages are (0+1)/2=0.5, (0+1)/2=0.5. Unique values: {0.5}. Count: 1.

---

## Solution
### Approach
The problem is solved using a **Sorting + Two Pointers** approach. By sorting the array first, the minimum and maximum elements at any step are always located at the current left and right pointers. A **Hash Set** is then used to store the calculated averages to ensure only unique values are counted.

### Complexity Analysis
- **Time Complexity**: `O(n log n)` due to the initial sorting of the array, where `n` is the number of elements. The two-pointer traversal takes `O(n)`.
- **Space Complexity**: `O(n)` to store the unique averages in a set.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the number of distinct averages by repeatedly pairing
    the minimum and maximum elements of the array.
    """
    nums.sort()
    distinct_averages = set()

    left = 0
    right = len(nums) - 1

    while left < right:
        avg = (nums[left] + nums[right]) / 2
        distinct_averages.add(avg)
        left += 1
        right -= 1

    return len(distinct_averages)
```
</details>
