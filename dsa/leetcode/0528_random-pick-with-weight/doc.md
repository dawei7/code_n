# Random Pick with Weight

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 528 |
| Difficulty | Medium |
| Topics | Array, Math, Binary Search, Prefix Sum, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/random-pick-with-weight/) |

## Problem Description
### Goal
Construct a picker from an array `w` of positive integer weights. Let $w_i$ be the weight at index $i$ and $W=\sum_j w_j$. The required selection probability for index $i$ is $w_i/W$, rather than an equal share among indices.

Each `pickIndex()` call must return a valid zero-based index according to that distribution, making a fresh random selection without modifying the weights. Larger weights must be proportionally more likely, while equal weights have equal probability. The method returns an index rather than its weight, and repeated calls need not avoid indices selected earlier.

### Function Contract
**Inputs**

- `weights`: positive integer weights for the indices
- `random_values`: app-local reproducible draws in the half-open interval `[0, 1)`; the native LeetCode interface generates these draws internally

**Return value**

- For the app adapter, the selected index for every supplied draw, in order

### Examples
**Example 1**

- Input: `weights = [1], random_values = [0.0, 0.5, 0.999]`
- Output: `[0, 0, 0]`

**Example 2**

- Input: `weights = [1, 3], random_values = [0.0, 0.249, 0.25, 0.999]`
- Output: `[0, 0, 1, 1]`

**Example 3**

- Input: `weights = [3, 1, 2], random_values = [0.1, 0.49, 0.5, 0.66, 0.67, 0.99]`
- Output: `[0, 0, 1, 1, 2, 2]`
