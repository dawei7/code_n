# Minimum Moves to Make Array Complementary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1674 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-moves-to-make-array-complementary](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/).

### Goal
For every mirrored pair `nums[i]` and `nums[n - 1 - i]`, choose a common target sum so all pairs have that sum. In one move, one number can be changed to any value from `1` to `limit`. Find the minimum number of moves.

### Function Contract
**Inputs**

- `nums`: an even-length integer array.
- `limit`: the maximum allowed value after a replacement.

**Return value**

Return the fewest moves needed to make all mirrored pair sums equal.

### Examples
**Example 1**

- Input: `nums = [1,2,4,3], limit = 4`
- Output: `1`

**Example 2**

- Input: `nums = [1,2,2,1], limit = 2`
- Output: `2`

**Example 3**

- Input: `nums = [1,2,1,2], limit = 2`
- Output: `0`

---

## Solution
### Approach
Use a difference array over possible target sums from `2` to `2 * limit`. Each pair contributes a baseline of two moves, improves to one move across the range reachable by changing one endpoint, and improves to zero moves at its current sum. Prefix the differences to find the total moves for every target and take the minimum.

### Complexity Analysis
- **Time Complexity**: `O(n + limit)`
- **Space Complexity**: `O(limit)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
