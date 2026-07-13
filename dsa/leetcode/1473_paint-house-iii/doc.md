# Paint House III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1473 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [paint-house-iii](https://leetcode.com/problems/paint-house-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/paint-house-iii/).

### Goal
Paint unpainted houses so exactly `target` neighborhoods are formed, minimizing total paint cost. Already painted houses cannot change color.

### Function Contract
**Inputs**

- `houses`: color `0` means unpainted; positive values are fixed colors.
- `cost`: `cost[i][c]` is the cost to paint house `i` with color `c + 1`.
- `m`: number of houses.
- `n`: number of colors.
- `target`: required number of neighborhoods.

**Return value**

The minimum total cost, or `-1` if the target neighborhood count is impossible.

### Examples
**Example 1**

- Input: `houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3`
- Output: `9`

**Example 2**

- Input: `houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3`
- Output: `11`

**Example 3**

- Input: `houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3`
- Output: `-1`

---

## Solution
### Approach
Dynamic programming by house index, last color, and neighborhood count. For each house, try the allowed colors and add a neighborhood when the color differs from the previous house.

### Complexity Analysis
- **Time Complexity**: `O(m * target * n^2)`
- **Space Complexity**: `O(target * n)` with rolling rows.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(houses, cost, m, n, target):
    houses = list(houses)
    m = min(len(houses), int(m)) if isinstance(m, int) and m > 0 else len(houses)
    houses = houses[:m]
    colors = max(1, int(n) if isinstance(n, int) and n > 0 else max((len(row) for row in cost if isinstance(row, list)), default=1))
    target = max(1, min(int(target), m)) if m else 0
    prices = []
    for i in range(m):
        row = cost[i] if i < len(cost) and isinstance(cost[i], list) else []
        padded = [abs(int(row[j])) if j < len(row) else 10**6 for j in range(colors)]
        prices.append(padded)
    inf = 10**18
    dp = {(0, 0): 0}
    for i, painted in enumerate(houses):
        next_dp = {}
        available = [painted] if isinstance(painted, int) and 1 <= painted <= colors else range(1, colors + 1)
        for color in available:
            paint_cost = 0 if painted == color else prices[i][color - 1]
            for (prev, groups), value in dp.items():
                new_groups = groups + (color != prev)
                if new_groups <= target:
                    key = (color, new_groups)
                    candidate = value + paint_cost
                    if candidate < next_dp.get(key, inf):
                        next_dp[key] = candidate
        dp = next_dp
    answer = min((value for (color, groups), value in dp.items() if groups == target), default=inf)
    return -1 if answer == inf else answer
```
</details>
