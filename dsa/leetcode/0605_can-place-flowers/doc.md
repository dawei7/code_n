# Can Place Flowers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 605 |
| Difficulty | Easy |
| Topics | Array, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/can-place-flowers/) |

## Problem Description
### Goal
You have a long flowerbed represented by a binary array `flowerbed`, where `1` means a plot already contains a flower and `0` means it is empty. Flowers cannot be planted in adjacent plots, and the initial flowerbed already obeys this no-adjacent-flowers rule.

Given an integer `n`, return `True` if at least `n` new flowers can be planted without violating the rule, and `False` otherwise. Existing flowers cannot be moved, and a newly planted flower must have no occupied plot immediately to its left or right; positions beyond either end of the array count as empty boundaries.

### Function Contract
**Inputs**

- `flowerbed: list[int]`: plots where `1` is occupied and `0` is empty; existing flowers are nonadjacent
- `n: int`: number of new flowers required

**Return value**

- `True` when a legal placement of at least `n` flowers exists; otherwise `False`

### Examples
**Example 1**

- Input: `flowerbed = [1,0,0,0,1], n = 1`
- Output: `True`

**Example 2**

- Input: `flowerbed = [1,0,0,0,1], n = 2`
- Output: `False`

**Example 3**

- Input: `flowerbed = [0], n = 1`
- Output: `True`
