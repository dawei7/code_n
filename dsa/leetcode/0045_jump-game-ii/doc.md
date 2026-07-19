# Jump Game II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 45 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/jump-game-ii/) |

## Problem Description
### Goal
You begin at index zero of a nonempty array. At position `i`, the nonnegative value `nums[i]` is the greatest number of indices that one jump may move forward; any shorter positive jump within the array is also allowed.

Return the minimum number of jumps needed to reach the final index. The input guarantees that some legal sequence reaches it, so no impossible-result marker is needed. A one-element array already starts at its destination and therefore requires zero jumps.

### Function Contract
**Inputs**

- `nums`: non-empty `List[int]` of non-negative maximum jump lengths

**Return value**

The minimum jump count as an `int`.

### Examples
**Example 1**

- Input: `nums = [2, 3, 1, 1, 4]`
- Output: `2`

**Example 2**

- Input: `nums = [2, 3, 0, 1, 4]`
- Output: `2`

**Example 3**

- Input: `nums = [0]`
- Output: `0`
