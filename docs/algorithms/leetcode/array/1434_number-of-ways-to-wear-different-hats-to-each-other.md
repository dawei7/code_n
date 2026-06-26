# Number of Ways to Wear Different Hats to Each Other

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1434 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Official Link | [number-of-ways-to-wear-different-hats-to-each-other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/) |

## Problem Description & Examples
### Goal
Count how many ways to assign hats so every person gets exactly one hat they like and no two people wear the same hat.

### Function Contract
**Inputs**

- `hats`: `hats[i]` lists the hat numbers liked by person `i`.

**Return value**

The number of valid assignments modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `hats = [[3,4],[4,5],[5]]`
- Output: `1`

**Example 2**

- Input: `hats = [[3,5,1],[3,5]]`
- Output: `4`

**Example 3**

- Input: `hats = [[1,2,3],[2,3,5],[1,3,5]]`
- Output: `8`

---

## Underlying Base Algorithm(s)
Bitmask dynamic programming over hats. Process hat numbers and update masks of people already assigned; for each hat, either skip it or assign it to one compatible unassigned person.

---

## Complexity Analysis
- **Time Complexity**: `O(H * 2^p * p)`, where `H` is the number of possible hats and `p` is the number of people.
- **Space Complexity**: `O(2^p)`
