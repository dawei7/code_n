# Minimum Moves to Equal Array Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 453 |
| Difficulty | Medium |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/) |

## Problem Description
### Goal
Given a nonempty integer array of length `n`, one move chooses exactly $n - 1$ positions and increments each chosen value by one. Repeat this operation until every array element has the same value.

Return the minimum number of moves required. Choosing all but one position is algebraically equivalent to decrementing the unchosen value relative to the others, so the optimal total is determined by distances above the original minimum rather than by raising everything toward the maximum. Negative starting values are allowed. The function returns only the move count and need not construct the final equalized array.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array

**Return value**

- The minimum number of allowed moves required to make every element equal

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `3`

**Example 2**

- Input: `nums = [1, 1, 1]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 2]`
- Output: `1`
