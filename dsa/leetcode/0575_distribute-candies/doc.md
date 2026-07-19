# Distribute Candies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 575 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [LeetCode](https://leetcode.com/problems/distribute-candies/) |

## Problem Description
### Goal
Alice has `n` candies, where `candyType[i]` identifies the type of the `i`th candy and `n` is even. Following her doctor's advice, she may eat only $n / 2$ of the candies, but she may choose which individual candies make up that allowance.

Return the maximum number of different types of candies Alice can eat while still respecting the $n / 2$ limit. Multiple candies of one type occupy multiple positions in her allowance but increase the number of different types only once.

### Function Contract
**Inputs**

- `candyType: list[int]`: an even-length list where equal integers represent candies of the same type

**Return value**

- An integer giving the maximum possible number of distinct types among exactly `len(candyType) / 2` chosen candies

### Examples
**Example 1**

- Input: `candyType = [1, 1, 2, 2, 3, 3]`
- Output: `3`

**Example 2**

- Input: `candyType = [1, 1, 2, 3]`
- Output: `2`

**Example 3**

- Input: `candyType = [6, 6, 6, 6]`
- Output: `1`
