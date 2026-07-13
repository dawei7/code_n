# Best Sightseeing Pair

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1014 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [best-sightseeing-pair](https://leetcode.com/problems/best-sightseeing-pair/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/best-sightseeing-pair/).

### Goal
Choose two sightseeing spots `i < j` to maximize `values[i] + values[j] + i - j`.

### Function Contract
**Inputs**

- `values`: List[int]

**Return value**

int - maximum pair score

### Examples
**Example 1**

- Input: `values = [8, 1, 5, 2, 6]`
- Output: `11`

**Example 2**

- Input: `values = [1, 2]`
- Output: `2`

**Example 3**

- Input: `values = [4, 7, 5, 8]`
- Output: `13`

---

## Solution
### Approach
One-pass dynamic tracking of the best left contribution.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1014: Best Sightseeing Pair."""


def solve(values: list[int]) -> int:
    best_left = values[0]
    answer = 0
    for j in range(1, len(values)):
        answer = max(answer, best_left + values[j] - j)
        best_left = max(best_left, values[j] + j)
    return answer
```
</details>
