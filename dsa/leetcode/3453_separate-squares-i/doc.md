# Separate Squares I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3453 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [separate-squares-i](https://leetcode.com/problems/separate-squares-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/separate-squares-i/).

### Goal
Given a list of axis-aligned squares defined by their bottom-left coordinates and side lengths, determine the horizontal line $y = k$ that divides the total area of all squares into two equal halves.

### Function Contract
**Inputs**

- `squares`: A list of lists, where each inner list `[x, y, l]` represents a square with its bottom-left corner at `(x, y)` and side length `l`.

**Return value**

- A float representing the y-coordinate $k$ such that the sum of the areas of the parts of the squares below $y = k$ equals the sum of the areas of the parts of the squares above $y = k$.

### Examples
**Example 1**

- Input: `squares = [[0,0,1],[2,2,1]]`
- Output: `1.5`

**Example 2**

- Input: `squares = [[0,0,2],[1,1,1]]`
- Output: `1.1666666667`

**Example 3**

- Input: `squares = [[0,0,1],[1,1,1]]`
- Output: `0.5`

---

## Solution
### Approach
The problem is solved using **Binary Search on the Answer**. Since the total area below a horizontal line $y=k$ is a monotonically increasing function of $k$, we can search for the value $k$ within the range $[min(y), max(y+l)]$. For a chosen $k$, we calculate the area of each square intersecting the line $y=k$ by clipping the square's vertical range $[y, y+l]$ against $[0, k]$.

### Complexity Analysis
- **Time Complexity**: $O(N \log(\frac{max\_coord}{\epsilon}))$, where $N$ is the number of squares, $max\_coord$ is the range of coordinates, and $\epsilon$ is the required precision (typically $10^{-5}$).
- **Space Complexity**: $O(1)$, as we only store a few variables for the binary search bounds and the calculated area.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(squares: list[list[int]]) -> float:
    def get_area_below(k: float) -> float:
        total_area = 0.0
        for x, y, l in squares:
            # The square spans [y, y + l]
            # We want the intersection of [y, y + l] and [0, k]
            bottom = y
            top = y + l
            if k > bottom:
                overlap = min(k, top) - bottom
                total_area += overlap * l
        return total_area

    total_sum = sum(l * l for x, y, l in squares)
    target = total_sum / 2.0

    low = min(s[1] for s in squares)
    high = max(s[1] + s[2] for s in squares)

    # Perform binary search for 100 iterations to ensure high precision
    for _ in range(100):
        mid = (low + high) / 2
        if get_area_below(mid) < target:
            low = mid
        else:
            high = mid

    return high
```
</details>
