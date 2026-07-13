# Longest Unequal Adjacent Groups Subsequence I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2900 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-unequal-adjacent-groups-subsequence-i](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/).

### Goal
Given two arrays of equal length—one containing strings and one containing group identifiers (0 or 1)—construct the longest possible subsequence such that no two adjacent elements in the subsequence belong to the same group.

### Function Contract
**Inputs**

- `words`: A list of strings representing the elements.
- `groups`: A list of integers (0 or 1) representing the group assignment for each corresponding string in `words`.

**Return value**

- A list of strings representing the longest subsequence satisfying the alternating group constraint.

### Examples
**Example 1**

- Input: `words = ["e","a","b"], groups = [0,0,1]`
- Output: `["e","b"]`

**Example 2**

- Input: `words = ["a","b","c","d"], groups = [1,0,1,1]`
- Output: `["a","b","c"]`

**Example 3**

- Input: `words = ["a","b","c","d"], groups = [0,1,0,1]`
- Output: `["a","b","c","d"]`

---

## Solution
### Approach
The problem can be solved using a **Greedy approach**. Since we want the longest subsequence, we iterate through the input arrays and keep track of the group of the last added element. Whenever we encounter an element whose group differs from the last added element's group, we include it in our result. This ensures we capture every possible transition between groups, which is optimal for this constraint.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input arrays, as we perform a single linear scan.
- **Space Complexity**: `O(n)` in the worst case to store the resulting subsequence.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(words: List[str], groups: List[int]) -> List[str]:
    """
    Constructs the longest subsequence where adjacent elements belong to different groups.
    Uses a greedy strategy to pick elements whenever the group changes.
    """
    if not words:
        return []

    result = [words[0]]
    last_group = groups[0]

    for i in range(1, len(words)):
        if groups[i] != last_group:
            result.append(words[i])
            last_group = groups[i]

    return result
```
</details>
