# Stone Game VII

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1690 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Official Link | [stone-game-vii](https://leetcode.com/problems/stone-game-vii/) |

## Problem Description & Examples
### Goal
Two players repeatedly remove either the leftmost or rightmost stone. The player gains points equal to the sum of stones that remain after the removal. Both play optimally. Find the final score difference.

### Function Contract
**Inputs**

- `stones`: a list of positive integers.

**Return value**

Return Alice's score minus Bob's score under optimal play.

### Examples
**Example 1**

- Input: `stones = [5,3,1,4,2]`
- Output: `6`

**Example 2**

- Input: `stones = [7,90,5,1,100,10,10,2]`
- Output: `122`

**Example 3**

- Input: `stones = [1,2]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Use interval dynamic programming. Let `dp[l][r]` be the best score advantage the current player can achieve from `stones[l:r+1]`. Removing left scores the remaining sum `sum(l+1..r)` minus the opponent's best response; removing right is symmetric. Prefix sums make each remaining sum constant-time.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)`, reducible to `O(n)` with rolling intervals
