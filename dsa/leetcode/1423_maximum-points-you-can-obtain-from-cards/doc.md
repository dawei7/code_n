# Maximum Points You Can Obtain from Cards

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1423 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-points-you-can-obtain-from-cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/).

### Goal
Take exactly `k` cards from either the left end or right end of the row. Maximize the sum of the taken card points.

### Function Contract
**Inputs**

- `cardPoints`: a list of card values.
- `k`: the number of cards that must be taken.

**Return value**

The maximum total points obtainable by taking `k` end cards.

### Examples
**Example 1**

- Input: `cardPoints = [1,2,3,4,5,6,1], k = 3`
- Output: `12`

**Example 2**

- Input: `cardPoints = [2,2,2], k = 2`
- Output: `4`

**Example 3**

- Input: `cardPoints = [9,7,7,9,7,7,9], k = 7`
- Output: `55`

---

## Solution
### Approach
Complement sliding window. Taking `k` cards from the ends is the same as leaving one contiguous middle block of length `n - k`; minimize that block's sum and subtract it from the total.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(card_points, k):
    n = len(card_points)
    k = max(0, min(int(k), n))
    if k == n:
        return sum(card_points)
    window = n - k
    current = sum(card_points[:window])
    best_middle = current
    for right in range(window, n):
        current += card_points[right] - card_points[right - window]
        best_middle = min(best_middle, current)
    return sum(card_points) - best_middle
```
</details>
