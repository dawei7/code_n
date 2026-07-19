# Random Pick Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 398 |
| Difficulty | Medium |
| Topics | Hash Table, Math, Reservoir Sampling, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/random-pick-index/) |

## Problem Description
### Goal
Construct a selector from an integer array that may contain duplicate values. For each `pick(target)` call, the target is guaranteed to occur, and the method must return one zero-based index whose stored value equals that target.

Choose uniformly among all matching positions, so every occurrence of the requested value has equal probability on each call. Repeated calls make fresh selections without consuming, rearranging, or modifying positions. Equal values at different indices remain distinct candidates. The app adapter supplies a sequence of targets and returns selected indices, while the native object exposes one stateful random call at a time.

### Function Contract
**Inputs**

- `nums`: the stored integer array
- `targets`: for the app adapter, the chronological target values passed to successive pick operations

**Return value**

- The app adapter returns one valid randomly selected index for each target. Native LeetCode calls `pick(target)` separately.

### Examples
**Example 1**

- Input: `nums = [1,2,3,3,3], targets = [3,1,3]`
- Output: one valid result is `[2,0,4]`

**Example 2**

- Input: `nums = [7], targets = [7,7]`
- Output: `[0,0]`

**Example 3**

- Input: `nums = [-1,4,-1], targets = [-1,4]`
- Output: one valid result is `[2,1]`
