# Elimination Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 390 |
| Difficulty | Medium |
| Topics | Math, Recursion |
| Official Link | [LeetCode](https://leetcode.com/problems/elimination-game/) |

## Problem Description
### Goal
Start with the integers in `[1, n]` sorted in strictly increasing order. On the first pass, move left to right and remove the first remaining number and every other number after it. On the next pass, move right to left and apply the same alternating removal from that end.

Continue switching directions after each pass until only one number remains, then return that survivor. Each round operates on the compact sequence left by the prior round, not on original index parity. Compute the answer without explicitly storing and deleting the full sequence, since `n` may be large.

### Function Contract
**Inputs**

- `n`: the positive inclusive upper bound of the initial sequence

**Return value**

- Return the only number remaining after all alternating elimination rounds.

### Examples
**Example 1**

- Input: `n = 9`
- Output: `6`

**Example 2**

- Input: `n = 1`
- Output: `1`

**Example 3**

- Input: `n = 6`
- Output: `4`
