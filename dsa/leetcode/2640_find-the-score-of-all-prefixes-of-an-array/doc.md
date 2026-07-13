# Find the Score of All Prefixes of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2640 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-score-of-all-prefixes-of-an-array](https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/).

### Goal
Given an array of integers, calculate the "score" for every prefix of the array. The score of a prefix is defined as the sum of the "converted" elements of that prefix. An element is converted by adding the current element to the maximum value encountered in the prefix up to that point. The final output is an array where each index `i` contains the cumulative score of the prefix ending at `i`.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- A list of integers (`List[int]`) representing the score of each prefix.

### Examples
**Example 1**

- Input: `nums = [2, 3, 7, 6, 1]`
- Output: `[4, 10, 24, 36, 42]`

**Example 2**

- Input: `nums = [1, 1, 2, 4, 8, 16]`
- Output: `[2, 4, 8, 16, 32, 64]`

**Example 3**

- Input: `nums = [10, 2, 5, 1]`
- Output: `[20, 22, 32, 34]`

---

## Solution
### Approach
The problem utilizes a **Prefix Sum** approach combined with **Running Maximum** tracking. By maintaining the maximum value seen so far as we iterate through the array, we can compute the converted value for each index in constant time and accumulate these values to form the prefix score.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass through the array.
- **Space Complexity**: `O(n)` to store the resulting array of scores.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> List[int]:
    """
    Calculates the score of all prefixes of an array.
    The score of a prefix is the sum of (nums[i] + max(nums[0...i])) for all i.
    """
    n = len(nums)
    scores = [0] * n

    current_max = 0
    running_score = 0

    for i in range(n):
        # Update the maximum value encountered so far
        if nums[i] > current_max:
            current_max = nums[i]

        # The converted value is nums[i] + current_max
        # The prefix score is the cumulative sum of these converted values
        running_score += (nums[i] + current_max)
        scores[i] = running_score

    return scores
```
</details>
