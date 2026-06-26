# Steps to Make Array Non-decreasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2289 |
| Difficulty | Medium |
| Topics | Array, Linked List, Dynamic Programming, Stack, Monotonic Stack, Simulation |
| Official Link | [steps-to-make-array-non-decreasing](https://leetcode.com/problems/steps-to-make-array-non-decreasing/) |

## Problem Description & Examples
### Goal
In each simultaneous step, remove every element smaller than the element immediately to its left. Return the number of steps until the array becomes nondecreasing.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

The number of simultaneous deletion rounds.

### Examples
**Example 1**

- Input: `nums = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]`
- Output: `3`

**Example 2**

- Input: `nums = [4, 5, 7, 7, 13]`
- Output: `0`

**Example 3**

- Input: `nums = [3, 2, 1]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Scan left to right with a decreasing monotonic stack of pairs `(value, removal_round)`. For a new value, pop all preceding values no greater than it while taking the maximum of their rounds. If a larger value remains, the new value disappears one round after that maximum; otherwise it survives with round zero. The largest assigned round is the answer.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
