# Distribute Elements Into Two Arrays I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3069 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [distribute-elements-into-two-arrays-i](https://leetcode.com/problems/distribute-elements-into-two-arrays-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/distribute-elements-into-two-arrays-i/).

### Goal
Given an array of integers, distribute its elements into two separate arrays based on a specific rule: the first element goes to the first array, the second goes to the second array, and subsequent elements are appended to the array whose last element is greater, or to the first array if the last elements are equal.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- A list formed by concatenating the final `arr1` followed by the final `arr2`.

### Examples
**Example 1**

- Input: `nums = [2, 1, 3]`
- Output: `[2, 3, 1]`

**Example 2**

- Input: `nums = [5, 4, 3, 8]`
- Output: `[5, 3, 4, 8]`

**Example 3**

- Input: `nums = [3, 3, 3, 3]`
- Output: `[3, 3, 3, 3]`

---

## Solution
### Approach
The problem is solved using a direct simulation approach. By maintaining two lists and tracking their last elements, we iterate through the input array once and apply the conditional logic to determine the destination of each element.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass over the elements.
- **Space Complexity**: `O(n)`, as we store all elements of the input array across the two resulting lists.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> List[List[int]]:
    if not nums:
        return [[], []]

    arr1 = [nums[0]]
    arr2 = [nums[1]]

    for i in range(2, len(nums)):
        if arr1[-1] > arr2[-1]:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])

    return arr1 + arr2
```
</details>
