# Minimum Levels to Gain More Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3096 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-levels-to-gain-more-points](https://leetcode.com/problems/minimum-levels-to-gain-more-points/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-levels-to-gain-more-points/).

### Goal
Given an array of game levels where each level is represented by 1 (win) or 0 (loss), determine the minimum number of levels the first player must complete to ensure their total score is strictly greater than the second player's total score. The game must be split into two non-empty parts, where the first player takes the first $k$ levels and the second player takes the remaining levels. If no such split exists, return -1.

### Function Contract
**Inputs**

- `possible`: A list of integers where each element is either 0 or 1.

**Return value**

- An integer representing the minimum number of levels (1-indexed) the first player must play, or -1 if it is impossible to achieve a higher score than the second player.

### Examples
**Example 1**

- Input: `possible = [1, 0, 1, 0]`
- Output: `1`

**Example 2**

- Input: `possible = [1, 1, 1, 1, 1]`
- Output: `3`

**Example 3**

- Input: `possible = [0, 0]`
- Output: `-1`

---

## Solution
### Approach
The problem is solved using the **Prefix Sum** technique. By pre-calculating the total sum of the array, we can determine the second player's score in constant time for any given split point. We iterate through the array once, maintaining a running sum for the first player and subtracting that from the total sum to find the second player's score, checking the condition at each step.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input array. We perform one pass to calculate the total sum and a second pass to evaluate the split points.
- **Space Complexity**: $O(1)$, as we only use a few integer variables to track the running sums and the total sum.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(possible: list[int]) -> int:
    # Convert 0s to -1s to represent losses, as per game rules
    # Total score is sum of (1 if win else -1)
    n = len(possible)
    total_sum = 0
    for x in possible:
        total_sum += 1 if x == 1 else -1

    current_player_sum = 0
    # We must split into two non-empty parts, so the first player
    # can take at most n-1 levels.
    for i in range(n - 1):
        val = 1 if possible[i] == 1 else -1
        current_player_sum += val
        remaining_sum = total_sum - current_player_sum

        if current_player_sum > remaining_sum:
            return i + 1

    return -1
```
</details>
