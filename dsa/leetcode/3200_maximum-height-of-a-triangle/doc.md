# Maximum Height of a Triangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3200 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-height-of-a-triangle](https://leetcode.com/problems/maximum-height-of-a-triangle/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-height-of-a-triangle/).

### Goal
Given two piles of colored balls (red and blue), determine the maximum height of a triangle that can be constructed. The triangle is built row by row, where the $i$-th row (1-indexed) must contain exactly $i$ balls of the same color. The colors must alternate between rows. You can choose to start the first row with either red or blue balls.

### Function Contract
**Inputs**

- `red`: An integer representing the total number of red balls available.
- `blue`: An integer representing the total number of blue balls available.

**Return value**

- An integer representing the maximum possible height of the triangle.

### Examples
**Example 1**

- Input: `red = 2, blue = 4`
- Output: `3`

**Example 2**

- Input: `red = 2, blue = 1`
- Output: `2`

**Example 3**

- Input: `red = 1, blue = 1`
- Output: `1`

---

## Solution
### Approach
The problem can be solved using a greedy simulation approach. Since the constraints are small, we can simulate the construction process twice: once starting with a red row and once starting with a blue row. In each simulation, we keep track of the remaining balls of each color and increment the row height as long as we have enough balls of the required color to complete the current row.

### Complexity Analysis
- **Time Complexity**: $O(\sqrt{N + M})$, where $N$ and $M$ are the number of red and blue balls respectively. The height of the triangle grows as $O(\sqrt{N+M})$, and we perform a constant number of simulations.
- **Space Complexity**: $O(1)$, as we only use a few integer variables to track the state of the simulation.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(red: int, blue: int) -> int:
    def get_max_height(first_color: int, second_color: int) -> int:
        height = 0
        row = 1
        while True:
            if row % 2 == 1:
                if first_color >= row:
                    first_color -= row
                else:
                    break
            else:
                if second_color >= row:
                    second_color -= row
                else:
                    break
            height += 1
            row += 1
        return height

    # Try starting with red, then try starting with blue
    return max(get_max_height(red, blue), get_max_height(blue, red))
```
</details>
