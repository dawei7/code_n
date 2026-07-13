# Count Number of Teams

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1395 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-number-of-teams](https://leetcode.com/problems/count-number-of-teams/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-number-of-teams/).

### Goal
Count teams of three soldiers chosen in increasing index order where ratings are either strictly increasing or strictly decreasing.

### Function Contract
**Inputs**

- `rating`: a list of distinct soldier ratings.

**Return value**

The number of valid three-person teams.

### Examples
**Example 1**

- Input: `rating = [2,5,3,4,1]`
- Output: `3`

**Example 2**

- Input: `rating = [2,1,3]`
- Output: `0`

**Example 3**

- Input: `rating = [1,2,3,4]`
- Output: `4`

---

## Solution
### Approach
Middle-index counting. Treat each soldier as the middle member, count smaller/larger ratings on the left and right, then add increasing and decreasing combinations.

### Complexity Analysis
- **Time Complexity**: `O(n^2)` with direct counting around each middle index.
- **Space Complexity**: `O(1)` extra.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1395: Count Number of Teams."""


def solve(rating: list[int]) -> int:
    total = 0
    n = len(rating)
    for mid in range(n):
        left_less = left_greater = right_less = right_greater = 0
        for i in range(mid):
            if rating[i] < rating[mid]:
                left_less += 1
            else:
                left_greater += 1
        for i in range(mid + 1, n):
            if rating[i] < rating[mid]:
                right_less += 1
            else:
                right_greater += 1
        total += left_less * right_greater + left_greater * right_less
    return total
```
</details>
