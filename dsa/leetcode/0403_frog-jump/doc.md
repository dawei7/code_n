# Frog Jump

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 403 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/frog-jump/) |

## Problem Description
### Goal
Stones lie at integer positions sorted in ascending order along a river, beginning at position zero. A frog starts on the first stone and must make its first jump exactly one unit, landing on a stone rather than in water.

After a jump of length `k`, the next jump may have positive length $k - 1$, `k`, or $k + 1$. Return `True` when some sequence of legal landings reaches the final stone and `False` otherwise. The frog may skip stones but cannot jump backward or remain in place, and earlier choices affect which jump lengths are available later.

### Function Contract
**Inputs**

- `stones`: strictly increasing stone positions beginning at zero

**Return value**

- Return `True` when some valid jump sequence lands on the final stone; otherwise return `False`.

### Examples
**Example 1**

- Input: `stones = [0,1,3,5,6,8,12,17]`
- Output: `True`

**Example 2**

- Input: `stones = [0,1,2,3,4,8,9,11]`
- Output: `False`

**Example 3**

- Input: `stones = [0,1]`
- Output: `True`
