# Min Max Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2293 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [min-max-game](https://leetcode.com/problems/min-max-game/) |

## Problem Description & Examples
### Goal
Repeatedly halve an array whose length is a power of two. For new index `i`, use the minimum of source pair `2i, 2i+1` when `i` is even and the maximum when `i` is odd. Return the final value.

### Function Contract
**Inputs**

- `nums`: an integer array of power-of-two length.

**Return value**

The sole value remaining after all rounds.

### Examples
**Example 1**

- Input: `nums = [1, 3, 5, 2, 4, 8, 2, 2]`
- Output: `1`

**Example 2**

- Input: `nums = [3]`
- Output: `3`

**Example 3**

- Input: `nums = [5, 4]`
- Output: `4`

---

## Underlying Base Algorithm(s)
Simulate rounds in place or into a temporary array. For each destination index, apply the parity-selected min or max to its source pair, then make the new half-length prefix active. Continue until one element remains.

---

## Complexity Analysis
- **Time Complexity**: `O(n)` across all geometrically shrinking rounds
- **Space Complexity**: `O(1)` auxiliary space with in-place updates
