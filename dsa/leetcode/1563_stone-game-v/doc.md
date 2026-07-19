# Stone Game V

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1563 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/stone-game-v/) |

## Problem Description
### Goal

Several stones form a row, and `stoneValue[i]` is the positive value of stone `i`. During each round, Alice splits the current row into two nonempty contiguous rows. Bob compares their total values and discards the row with the larger sum. Alice gains the sum of the row that remains, and play continues using that row.

When the two sums are equal, Bob lets Alice choose which side to discard. The game ends when only one stone remains. Starting from score zero, return the maximum total score Alice can obtain by choosing every split optimally.

### Function Contract
**Inputs**

- `stoneValue`: An array of $N$ positive integers, where $1 \le N \le 500$ and $1 \le \texttt{stoneValue[i]} \le 10^6$.
- Stone order is fixed; each split divides the current contiguous interval between two adjacent stones.

**Return value**

Return Alice's maximum attainable total score under Bob's prescribed discard rule.

### Examples
**Example 1**

- Input: `stoneValue = [6,2,3,4,5,5]`
- Output: `18`

**Example 2**

- Input: `stoneValue = [7,7,7,7,7,7,7]`
- Output: `28`

**Example 3**

- Input: `stoneValue = [4]`
- Output: `0`
