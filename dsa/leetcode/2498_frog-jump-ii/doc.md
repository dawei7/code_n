# Frog Jump II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2498 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [frog-jump-ii](https://leetcode.com/problems/frog-jump-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/frog-jump-ii/).

### Goal
A frog needs to travel from the first stone to the last stone and then return to the first stone. The frog must visit every stone exactly once during the round trip. The goal is to minimize the maximum jump distance (the "cost") encountered during the entire journey.

### Function Contract
**Inputs**

- `stones`: A strictly increasing list of integers representing the positions of stones on a 1D path.

**Return value**

- An integer representing the minimum possible value for the maximum jump distance across the entire round trip.

### Examples
**Example 1**

- Input: `stones = [0, 2, 5, 6, 7]`
- Output: `5`

**Example 2**

- Input: `stones = [0, 3, 9]`
- Output: `9`

---

## Solution
### Approach
The problem can be solved using a **Greedy** approach. By alternating stones between the forward and backward paths, we can ensure that the frog skips every other stone in each direction. The maximum jump distance will be the maximum of either the distance between adjacent stones (if we were forced to jump to the immediate next one) or the distance between stones separated by one index (e.g., `stones[i+2] - stones[i]`).

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of stones, as we iterate through the array once to calculate the gaps.
- **Space Complexity**: `O(1)`, as we only store the maximum jump value and do not require additional data structures proportional to the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(stones: List[int]) -> int:
    """
    To minimize the maximum jump, we should distribute the stones such that
    the frog jumps over one stone whenever possible.

    For any three consecutive stones i, i+1, i+2, the frog must jump
    at least stones[i+2] - stones[i] to ensure the round trip is covered
    efficiently. The only exception is the start and end of the array.
    """
    n = len(stones)

    # If there are only two stones, the only jump is the distance between them.
    if n == 2:
        return stones[1] - stones[0]

    # The maximum jump will be at least the distance between stones[i+2] and stones[i]
    # because one path will take stones[i] -> stones[i+2] and the other will
    # visit stones[i+1].
    max_jump = 0

    # Check gaps of size 2 (skipping one stone)
    for i in range(n - 2):
        max_jump = max(max_jump, stones[i + 2] - stones[i])

    # Also consider the jump between the first two and last two stones
    # (though these are covered by the loop logic, it's good to be explicit)
    max_jump = max(max_jump, stones[1] - stones[0])
    max_jump = max(max_jump, stones[n - 1] - stones[n - 2])

    return max_jump
```
</details>
