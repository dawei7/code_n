# Minimum Cost for Cutting Cake II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3219 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-cost-for-cutting-cake-ii](https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/).

### Goal
Given a grid of size `m x n`, you need to cut the cake into `1 x 1` individual squares. You are provided with the costs to make horizontal cuts and vertical cuts. Each cut spans the entire current piece of cake. When you make a cut, the cost is multiplied by the number of segments that cut currently intersects. The objective is to determine the minimum total cost to reduce the entire cake into `1 x 1` pieces.

### Function Contract
**Inputs**

- `m`: An integer representing the number of rows.
- `n`: An integer representing the number of columns.
- `horizontalCut`: A list of integers where `horizontalCut[i]` is the cost of the `i`-th horizontal cut.
- `verticalCut`: A list of integers where `verticalCut[j]` is the cost of the `j`-th vertical cut.

**Return value**

- An integer representing the minimum total cost to cut the cake into `1 x 1` squares.

### Examples
**Example 1**

- Input: `m = 3, n = 2, horizontalCut = [1, 3], verticalCut = [5]`
- Output: `13`

**Example 2**

- Input: `m = 2, n = 2, horizontalCut = [7], verticalCut = [4]`
- Output: `15`

---

## Solution
### Approach
The problem is solved using a **Greedy Strategy**. The key insight is that a cut made earlier will be multiplied by the number of pieces it crosses. To minimize the total cost, we should always prioritize making the most expensive cuts as early as possible, because they will be multiplied by fewer segments if performed later. By sorting both cut arrays in descending order and iterating through them, we can decide at each step whether to perform the next most expensive horizontal or vertical cut, updating the count of segments crossed accordingly.

### Complexity Analysis
- **Time Complexity**: `O(M log M + N log N)`, where `M` and `N` are the lengths of the horizontal and vertical cut arrays, respectively. This is dominated by the sorting step.
- **Space Complexity**: `O(1)` (excluding the input storage), as we only use a few variables to track the number of segments and the total cost.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(m: int, n: int, horizontal_cut: list[int], vertical_cut: list[int]) -> int:
    # Sort cuts in descending order to apply the greedy strategy
    horizontal_cut = sorted(horizontal_cut, reverse=True)
    vertical_cut = sorted(vertical_cut, reverse=True)

    h_idx = 0
    v_idx = 0

    # Number of segments currently created
    h_segments = 1
    v_segments = 1

    total_cost = 0

    # Process cuts until all are used
    while h_idx < len(horizontal_cut) and v_idx < len(vertical_cut):
        # If the current horizontal cut is more expensive, perform it
        if horizontal_cut[h_idx] >= vertical_cut[v_idx]:
            total_cost += horizontal_cut[h_idx] * v_segments
            h_segments += 1
            h_idx += 1
        else:
            # Otherwise, perform the vertical cut
            total_cost += vertical_cut[v_idx] * h_segments
            v_segments += 1
            v_idx += 1

    # Add remaining horizontal cuts
    while h_idx < len(horizontal_cut):
        total_cost += horizontal_cut[h_idx] * v_segments
        h_idx += 1

    # Add remaining vertical cuts
    while v_idx < len(vertical_cut):
        total_cost += vertical_cut[v_idx] * h_segments
        v_idx += 1

    return total_cost
```
</details>
