# Maximum Students Taking Exam

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1349 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Matrix, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-students-taking-exam](https://leetcode.com/problems/maximum-students-taking-exam/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-students-taking-exam/).

### Goal
Seat as many students as possible in a classroom grid. Broken seats cannot be used, and no student may sit directly left/right of another student or diagonally behind another student in the previous row.

### Function Contract
**Inputs**

- `seats`: grid of `"."` usable seats and `"#"` broken seats.

**Return value**

The maximum number of students who can take the exam.

### Examples
**Example 1**

- Input: `seats = [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]`
- Output: `4`

**Example 2**

- Input: `seats = [[".","#"],["#","#"],["#","."],["#","#"],[".","#"]]`
- Output: `3`

**Example 3**

- Input: `seats = [["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]]`
- Output: `10`

---

## Solution
### Approach
Bitmask dynamic programming by row.

### Complexity Analysis
- **Time Complexity**: `O(rows * states^2)` where `states <= 2^cols`.
- **Space Complexity**: `O(states)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(seats):
    rows = len(seats)
    cols = len(seats[0]) if rows else 0
    valid_by_row = []
    for r in range(rows):
        blocked = 0
        for c in range(cols):
            if seats[r][c] == "#":
                blocked |= 1 << c
        masks = []
        for mask in range(1 << cols):
            if mask & blocked or mask & (mask << 1):
                continue
            masks.append(mask)
        valid_by_row.append(masks)

    dp = {0: 0}
    for masks in valid_by_row:
        next_dp = {}
        for mask in masks:
            count = mask.bit_count()
            best = 0
            for prev, value in dp.items():
                if mask & (prev << 1) or mask & (prev >> 1):
                    continue
                best = max(best, value + count)
            next_dp[mask] = best
        dp = next_dp
    return max(dp.values(), default=0)
```
</details>
