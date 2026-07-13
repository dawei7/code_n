# Find the Number of Distinct Colors Among the Balls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3160 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-number-of-distinct-colors-among-the-balls](https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/).

### Goal
Given a sequence of queries where each query assigns a specific color to a ball at a given index, track the total number of unique colors currently present on the balls after each assignment. If a ball already has a color, it is overwritten by the new one.

### Function Contract
**Inputs**

- `limit`: An integer representing the maximum index of a ball (balls are indexed from 0 to `limit`).
- `queries`: A list of lists, where each inner list `[ball, color]` represents an update operation.

**Return value**

- A list of integers where the $i$-th element is the count of distinct colors present on the balls after the $i$-th query.

### Examples
**Example 1**

- Input: `limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]`
- Output: `[1, 2, 2, 3]`

**Example 2**

- Input: `limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]`
- Output: `[1, 2, 2, 3, 4]`

**Example 3**

- Input: `limit = 1, queries = [[0,1],[0,4],[1,2],[1,2],[0,3]]`
- Output: `[1, 1, 2, 2, 3]`

---

## Solution
### Approach
The problem is solved using a simulation approach supported by two Hash Maps (dictionaries in Python). One map tracks the current color of each ball (`ball_to_color`), and the other tracks the frequency of each color currently in use (`color_counts`). This allows for $O(1)$ updates and lookups per query.

### Complexity Analysis
- **Time Complexity**: $O(Q)$, where $Q$ is the number of queries, as each query involves constant-time dictionary operations.
- **Space Complexity**: $O(Q + L)$, where $Q$ is the number of queries and $L$ is the number of balls, to store the mappings of balls to colors and the counts of each color.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(limit: int, queries: list[list[int]]) -> list[int]:
    ball_to_color = {}
    color_counts = defaultdict(int)
    results = []

    for ball, color in queries:
        # If the ball already has a color, decrement the count of the old color
        if ball in ball_to_color:
            old_color = ball_to_color[ball]
            color_counts[old_color] -= 1
            if color_counts[old_color] == 0:
                del color_counts[old_color]

        # Update the ball's color and increment the count of the new color
        ball_to_color[ball] = color
        color_counts[color] += 1

        # The number of distinct colors is the number of keys in color_counts
        results.append(len(color_counts))

    return results
```
</details>
