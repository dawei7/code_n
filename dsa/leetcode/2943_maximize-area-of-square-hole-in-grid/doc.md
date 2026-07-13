# Maximize Area of Square Hole in Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2943 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximize-area-of-square-hole-in-grid](https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/).

### Goal
Given a grid defined by horizontal and vertical bars, identify the largest possible square hole that can be formed by removing a contiguous sequence of bars. A square hole is created by removing $k$ consecutive horizontal bars and $k$ consecutive vertical bars, resulting in a square of side length $k+1$.

### Function Contract
**Inputs**

- `n`: An integer representing the number of horizontal bars (excluding the boundary).
- `m`: An integer representing the number of vertical bars (excluding the boundary).
- `hBars`: A list of integers representing the positions of horizontal bars.
- `vBars`: A list of integers representing the positions of vertical bars.

**Return value**

- An integer representing the maximum area of the square hole that can be formed.

### Examples
**Example 1**

- Input: `n = 2, m = 1, hBars = [2, 3], vBars = [2]`
- Output: `4`

**Example 2**

- Input: `n = 1, m = 1, hBars = [2], vBars = [2]`
- Output: `4`

**Example 3**

- Input: `n = 2, m = 3, hBars = [2, 3], vBars = [2, 3, 4]`
- Output: `9`

---

## Solution
### Approach
The problem reduces to finding the longest sequence of consecutive integers in the provided bar lists. By sorting the bars and identifying the maximum number of consecutive segments, we determine the maximum side length $k+1$ of a square. The area is then the square of the minimum of the maximum consecutive horizontal and vertical segments.

### Complexity Analysis
- **Time Complexity**: $O(N \log N + M \log M)$, where $N$ and $M$ are the lengths of `hBars` and `vBars` respectively, due to the sorting step.
- **Space Complexity**: $O(1)$ (excluding the input storage), as we only track the current and maximum consecutive sequences.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
    def get_max_consecutive(bars: list[int]) -> int:
        if not bars:
            return 1
        bars.sort()
        max_seq = 1
        current_seq = 1
        for i in range(1, len(bars)):
            if bars[i] == bars[i - 1] + 1:
                current_seq += 1
            else:
                current_seq = 1
            max_seq = max(max_seq, current_seq)
        return max_seq + 1

    max_h = get_max_consecutive(hBars)
    max_v = get_max_consecutive(vBars)

    side = min(max_h, max_v)
    return side * side
```
</details>
