# Jump Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 55 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/jump-game/) |

## Problem Description
### Goal
You start at index zero of a nonempty array. At index `i`, the value `nums[i]` gives the maximum number of positions a jump may advance; any shorter forward jump that stays within the array is also legal.

Determine whether some sequence of jumps can reach the final index and return that boolean result. A zero can stop progress unless it can be jumped over from an earlier position. A one-element array is already at its destination and is therefore reachable even when its only value is zero.

### Function Contract
**Inputs**

- `nums`: a nonempty `List[int]` of maximum jump lengths

**Return value**

`True` exactly when some sequence of legal jumps reaches the final index.

### Examples
**Example 1**

- Input: `nums = [2,3,1,1,4]`
- Output: `True`

**Example 2**

- Input: `nums = [3,2,1,0,4]`
- Output: `False`

**Example 3**

- Input: `nums = [0]`
- Output: `True`
