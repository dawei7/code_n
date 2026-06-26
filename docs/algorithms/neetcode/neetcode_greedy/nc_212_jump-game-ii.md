## Problem Description & Examples
### Goal
You are given a 0-indexed array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:
- `0 <= j <= nums[i]` and `i + j < n`

Return the minimum number of jumps to reach `nums[n - 1]`. You may assume that you can always reach the last index.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - minimum jumps

### Examples
**Example 1**

- Input: `nums = [2, 3, 1, 1, 4]`
- Output: `2`

**Example 2**

- Input: `nums = [4, 1]`
- Output: `1`

**Example 3**

- Input: `nums = [5, 1]`
- Output: `1`

---

## Underlying Base Algorithm(s)
- [Gas station](greedy_06_gas-station.md)
- [Jump game](greedy_07_jump-game.md)
- [Candy distribution](greedy_08_candy-distribution.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
