# Find Indices of Stable Mountains

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3285 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-indices-of-stable-mountains](https://leetcode.com/problems/find-indices-of-stable-mountains/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-indices-of-stable-mountains/).

### Goal
Identify all indices `i` (where `i > 0`) in an array of mountain heights such that the mountain immediately preceding it (at index `i - 1`) has a height strictly greater than a given threshold value `threshold`.

### Function Contract
**Inputs**

- `height`: A list of integers representing the heights of a sequence of mountains.
- `threshold`: An integer representing the height limit for stability.

**Return value**

- A list of integers containing all indices `i` (1-indexed or 0-indexed based on problem constraints, here 1 to n-1) where `height[i-1] > threshold`.

### Examples
**Example 1**

- Input: `height = [1, 2, 3, 4, 5], threshold = 2`
- Output: `[3, 4]`

**Example 2**

- Input: `height = [10, 1, 10, 1, 10], threshold = 3`
- Output: `[1, 3]`

**Example 3**

- Input: `height = [10, 1, 10, 1, 10], threshold = 10`
- Output: `[]`

---

## Solution
### Approach
Linear scan (Iteration). The problem requires a single pass through the array starting from the second element to check the condition against the previous element.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the `height` array, as we iterate through the list exactly once.
- **Space Complexity**: `O(k)`, where `k` is the number of stable mountains found, required to store the resulting list of indices.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(height: List[int], threshold: int) -> List[int]:
    """
    Finds indices i such that height[i-1] > threshold.
    The range of i is from 1 to len(height) - 1.
    """
    stable_indices = []

    # We start from index 1 because the condition depends on height[i-1]
    for i in range(1, len(height)):
        if height[i - 1] > threshold:
            stable_indices.append(i)

    return stable_indices
```
</details>
