# Minimum Cost to Move Chips to The Same Position

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1217 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-cost-to-move-chips-to-the-same-position](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/).

### Goal
Move all chips to one position. Moving a chip by two positions costs `0`, while moving it by one position costs `1`. Return the minimum total cost.

### Function Contract
**Inputs**

- `position`: chip positions on a number line.

**Return value**

The minimum cost to gather all chips at one position.

### Examples
**Example 1**

- Input: `position = [1,2,3]`
- Output: `1`

**Example 2**

- Input: `position = [2,2,2,3,3]`
- Output: `2`

**Example 3**

- Input: `position = [1,1000000000]`
- Output: `1`

---

## Solution
### Approach
Parity counting and greedy choice.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(position):
    odd = sum(value % 2 for value in position)
    return min(odd, len(position) - odd)
```
</details>
