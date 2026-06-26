# Last Moment Before All Ants Fall Out of a Plank

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1503 |
| Difficulty | Medium |
| Topics | Array, Brainteaser, Simulation |
| Official Link | [last-moment-before-all-ants-fall-out-of-a-plank](https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/) |

## Problem Description & Examples
### Goal
Find the last time at which any ant falls off a plank. Ants move at the same
speed, and when two ants meet, the result is equivalent to them passing through
each other.

### Function Contract
**Inputs**

- `n`: the length of the plank, with ends at `0` and `n`.
- `left`: positions of ants moving left.
- `right`: positions of ants moving right.

**Return value**

The maximum fall time among all ants.

### Examples
**Example 1**

- Input: `n = 4, left = [4, 3], right = [0, 1]`
- Output: `4`

**Example 2**

- Input: `n = 7, left = [], right = [0, 1, 2, 3, 4, 5, 6, 7]`
- Output: `7`

**Example 3**

- Input: `n = 5, left = [2], right = [3]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Collisions do not change the set of fall times because swapping directions is
equivalent to ants passing through. A left-moving ant at position `x` falls after
`x` seconds, and a right-moving ant at position `x` falls after `n - x` seconds.
Take the maximum of those distances.

---

## Complexity Analysis
- **Time Complexity**: `O(len(left) + len(right))`.
- **Space Complexity**: `O(1)`.
