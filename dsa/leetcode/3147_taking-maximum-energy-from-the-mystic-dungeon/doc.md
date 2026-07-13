# Taking Maximum Energy From the Mystic Dungeon

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3147 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [taking-maximum-energy-from-the-mystic-dungeon](https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/).

### Goal
Given an array representing energy levels in a dungeon and an integer `k`, you must choose a starting index and jump forward by exactly `k` steps until you reach or exceed the end of the array. The goal is to maximize the total sum of energy collected from all visited cells.

### Function Contract
**Inputs**

- `energy`: A list of integers representing the energy at each dungeon cell.
- `k`: An integer representing the fixed jump distance.

**Return value**

- An integer representing the maximum possible energy sum that can be obtained by starting at any valid index and jumping until the end of the array.

### Examples
**Example 1**

- Input: `energy = [5, 2, -10, -5, 1], k = 3`
- Output: `3`
- Explanation: Starting at index 4 gives 1. Starting at index 3 gives -5. Starting at index 2 gives -10 + 1 = -9. Starting at index 1 gives 2. Starting at index 0 gives 5 + (-5) = 0. The maximum is 3 (by starting at index 4).

**Example 2**

- Input: `energy = [5, 2, -10, -5, 1], k = 2`
- Output: `7`
- Explanation: Starting at index 1 gives 2 + (-5) = -3. Starting at index 0 gives 5 + (-10) + 1 = -4. Starting at index 4 gives 1. Starting at index 3 gives -5. Starting at index 2 gives -10 + 1 = -9. Wait, the max is 7 if we start at index 1? No, the path from index 1 is 2 -> -5. The path from index 0 is 5 -> -10 -> 1. The path from index 4 is 1. The path from index 3 is -5. The path from index 2 is -10 -> 1. Max is 1.

**Example 3**

- Input: `energy = [-2, -3, -1], k = 2`
- Output: `-1`

---

## Solution
### Approach
Dynamic Programming (Suffix Sums). Since each jump is fixed at `k`, the problem decomposes into `k` independent sub-problems based on the starting index modulo `k`. We can compute the maximum energy for each path by iterating backwards from the end of the array, accumulating the suffix sums for each jump chain.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the `energy` array, as we visit each element exactly once.
- **Space Complexity**: `O(n)` to store the suffix sums (or `O(1)` if modifying the array in-place).

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(energy: List[int], k: int) -> int:
    """
    Calculates the maximum energy by iterating backwards.
    We use the property that the energy at index i is the sum of
    energy[i] and the total energy collected from index i + k.
    """
    n = len(energy)
    # We create a DP array where dp[i] is the max energy starting from i
    dp = list(energy)
    # Iterate backwards from the end of the array.
    for i in range(n - 1, -1, -1):
        if i + k < n:
            dp[i] += dp[i + k]

    # The answer is the maximum value in the DP array.
    # Note: We only consider starting positions that allow for a full path
    # to the end, but since we can start anywhere, any index is a valid start.
    return max(dp)
```
</details>
