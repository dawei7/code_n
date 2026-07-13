# Convert an Array Into a 2D Array With Conditions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2610 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [convert-an-array-into-a-2d-array-with-conditions](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/).

### Goal
Given an array of integers, construct a 2D array such that every row contains only unique elements from the original array, and all elements from the original array are included in the 2D structure. The goal is to minimize the number of rows required to satisfy these constraints.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- A list of lists of integers (`List[List[int]]`) representing the constructed 2D array.

### Examples
**Example 1**

- Input: `nums = [1,3,4,1,2,3,1]`
- Output: `[[1,3,4,2],[1,3],[1]]`

**Example 2**

- Input: `nums = [1,2,3,4]`
- Output: `[[1,2,3,4]]`

**Example 3**

- Input: `nums = [2,0,0,1,2]`
- Output: `[[2,0,1],[0,2]]`

---

## Solution
### Approach
The problem is solved using a frequency counting approach. By tracking the occurrence count of each integer, we can determine that an element appearing $k$ times must be placed in $k$ distinct rows. We iterate through the frequency map and distribute each element into the $i$-th row, where $i$ corresponds to the current count of that element encountered so far.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the number of elements in the input array. We iterate through the array once to count frequencies and once more to distribute elements into rows.
- **Space Complexity**: $O(n)$, required to store the frequency map and the resulting 2D array structure.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter
from typing import List

def solve(nums: List[int]) -> List[List[int]]:
    """
    Constructs a 2D array from nums such that each row contains unique elements.
    The number of rows is determined by the maximum frequency of any element.
    """
    counts = Counter(nums)
    result = []

    # The maximum frequency of any element dictates the number of rows needed.
    # We iterate through the frequency map and place each instance of a number
    # into a unique row index.
    for num, freq in counts.items():
        for i in range(freq):
            # If the current row index doesn't exist in the result yet, create it.
            if i >= len(result):
                result.append([])
            result[i].append(num)

    return result
```
</details>
