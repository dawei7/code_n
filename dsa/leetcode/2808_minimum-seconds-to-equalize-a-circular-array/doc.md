# Minimum Seconds to Equalize a Circular Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2808 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-seconds-to-equalize-a-circular-array](https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/).

### Goal
Given a circular array of integers, in each second, you can replace any element with its immediate neighbors (left or right). Determine the minimum number of seconds required to make all elements in the array equal to the same value.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the circular array.

**Return value**

- An integer representing the minimum seconds needed to make all elements equal.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 2]`
- Output: `1`

**Example 2**

- Input: `nums = [2, 1, 3, 3, 2]`
- Output: `2`

**Example 3**

- Input: `nums = [5, 5, 5, 5]`
- Output: `0`

---

## Solution
### Approach
The problem can be solved by identifying the maximum gap between occurrences of each unique number in the circular array. For a specific value $x$, if the indices where $x$ appears are $i_1, i_2, \dots, i_k$, the time required to fill the gaps between these occurrences is $\lfloor \text{gap} / 2 \rfloor$. Because the array is circular, the gap between the last occurrence and the first occurrence (wrapping around) must also be considered. We calculate this for every unique number and return the minimum of these maximum gaps.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the array. We iterate through the array once to store indices and once more to calculate the gaps for each unique element.
- **Space Complexity**: $O(n)$ to store the indices of each unique element in a hash map.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict
import math

def solve(nums: list[int]) -> int:
    n = len(nums)
    indices = defaultdict(list)

    for i, val in enumerate(nums):
        indices[val].append(i)

    min_seconds = n

    for val in indices:
        pos = indices[val]
        # Calculate gaps between consecutive occurrences
        max_gap = 0
        for i in range(len(pos) - 1):
            max_gap = max(max_gap, pos[i+1] - pos[i] - 1)

        # Account for circular gap (last element to first element)
        circular_gap = (n - 1 - pos[-1]) + pos[0]
        max_gap = max(max_gap, circular_gap)

        # The time to fill a gap of size 'g' is ceil(g / 2)
        # which is equivalent to (g + 1) // 2
        seconds_needed = (max_gap + 1) // 2
        min_seconds = min(min_seconds, seconds_needed)

    return min_seconds
```
</details>
