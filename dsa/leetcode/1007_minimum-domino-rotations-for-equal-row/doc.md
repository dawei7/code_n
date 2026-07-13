# Minimum Domino Rotations For Equal Row

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1007 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-domino-rotations-for-equal-row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/).

### Goal
Each domino has a top and bottom value. You may rotate individual dominoes to swap top and bottom. Return the minimum rotations needed so all top values are equal or all bottom values are equal, or `-1` if impossible.

### Function Contract
**Inputs**

- `tops`: List[int]
- `bottoms`: List[int]

**Return value**

int - minimum rotations, or `-1`

### Examples
**Example 1**

- Input: `tops = [2, 1, 2, 4, 2, 2], bottoms = [5, 2, 6, 2, 3, 2]`
- Output: `2`

**Example 2**

- Input: `tops = [3, 5, 1, 2, 3], bottoms = [3, 6, 3, 3, 4]`
- Output: `-1`

**Example 3**

- Input: `tops = [1, 1, 1], bottoms = [1, 2, 3]`
- Output: `0`

---

## Solution
### Approach
Greedy candidate validation.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1007: Minimum Domino Rotations For Equal Row."""


def solve(tops: list[int], bottoms: list[int]) -> int:
    def rotations(target: int) -> int:
        top_moves = 0
        bottom_moves = 0
        for top, bottom in zip(tops, bottoms):
            if top != target and bottom != target:
                return 10**9
            if top != target:
                top_moves += 1
            if bottom != target:
                bottom_moves += 1
        return min(top_moves, bottom_moves)

    best = min(rotations(tops[0]), rotations(bottoms[0]))
    return -1 if best == 10**9 else best
```
</details>
