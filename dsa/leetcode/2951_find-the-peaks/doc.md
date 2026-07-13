# Find the Peaks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2951 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-peaks](https://leetcode.com/problems/find-the-peaks/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-peaks/).

### Goal
Identify all indices in a given integer array that represent "peaks." A peak is defined as an element that is strictly greater than its immediate neighbors. Note that the first and last elements of the array cannot be peaks because they lack two neighbors.

### Function Contract
**Inputs**

- `mountain`: A list of integers (`List[int]`) representing the elevation profile.

**Return value**

- A list of integers (`List[int]`) containing the indices of all identified peaks in increasing order.

### Examples
**Example 1**

- Input: `mountain = [2, 4, 4]`
- Output: `[]`

**Example 2**

- Input: `mountain = [1, 4, 3, 8, 5]`
- Output: `[1, 3]`

**Example 3**

- Input: `mountain = [1, 2, 3, 4, 5]`
- Output: `[]`

---

## Solution
### Approach
The problem utilizes a **Linear Scan (Enumeration)** approach. By iterating through the array from index `1` to `n-2` (where `n` is the length of the array), we perform a constant-time comparison for each element against its left and right neighbors to determine if it satisfies the peak condition.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of elements in the input array, as we perform a single pass through the list.
- **Space Complexity**: `O(k)`, where `k` is the number of peaks found, required to store the resulting indices. In the worst case, this is `O(n)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(mountain: List[int]) -> List[int]:
    """
    Finds all indices i such that mountain[i-1] < mountain[i] > mountain[i+1].
    """
    peaks = []
    # A peak cannot be the first or last element, so we iterate from 1 to len-2
    for i in range(1, len(mountain) - 1):
        if mountain[i - 1] < mountain[i] > mountain[i + 1]:
            peaks.append(i)
    return peaks
```
</details>
