# Probability of a Two Boxes Having The Same Number of Distinct Balls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1467 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Backtracking, Combinatorics, Probability and Statistics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [probability-of-a-two-boxes-having-the-same-number-of-distinct-balls](https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/).

### Goal
Distribute colored balls equally between two boxes by choosing half of all balls. Compute the probability that both boxes contain the same number of distinct colors.

### Function Contract
**Inputs**

- `balls`: `balls[i]` is the count of balls of color `i`.

**Return value**

The probability as a floating-point value.

### Examples
**Example 1**

- Input: `balls = [1,1]`
- Output: `1.0`

**Example 2**

- Input: `balls = [2,1,1]`
- Output: `0.66667`

**Example 3**

- Input: `balls = [1,2,1,2]`
- Output: `0.6`

---

## Solution
### Approach
Backtracking with combinatorics. For each color, choose how many balls go to the first box, multiply by the combination count, and accumulate favorable assignments where both boxes end with equal size and equal distinct-color counts.

### Complexity Analysis
- **Time Complexity**: `O(product(balls[i] + 1))`
- **Space Complexity**: `O(c)` for recursion depth over `c` colors.

### Reference Implementations
<details>
<summary>python</summary>

```python
from functools import lru_cache
from math import comb


def solve(balls):
    total = sum(balls)
    if len(balls) > 8 or total > 48:
        return 0.0
    half = total // 2
    if total % 2:
        return 0.0
    colors = len(balls)
    total_ways = comb(total, half)

    @lru_cache(None)
    def dfs(index, left_count, left_distinct, right_distinct):
        if index == colors:
            return 1 if left_count == half and left_distinct == right_distinct else 0
        ways = 0
        count = balls[index]
        for left in range(count + 1):
            if left_count + left > half:
                break
            right = count - left
            ways += (
                comb(count, left)
                * dfs(index + 1, left_count + left, left_distinct + (left > 0), right_distinct + (right > 0))
            )
        return ways

    return dfs(0, 0, 0, 0) / total_ways if total_ways else 0.0
```
</details>
