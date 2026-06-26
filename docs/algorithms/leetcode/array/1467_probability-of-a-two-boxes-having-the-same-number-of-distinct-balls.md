# Probability of a Two Boxes Having The Same Number of Distinct Balls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1467 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Backtracking, Combinatorics, Probability and Statistics |
| Official Link | [probability-of-a-two-boxes-having-the-same-number-of-distinct-balls](https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/) |

## Problem Description & Examples
### Goal
Distribute colored balls equally between two boxes by choosing half of all balls. Compute the probability that both boxes contain the same number of distinct colors.

### Function Contract
**Inputs**

- `balls`: `balls[i]` is the count of balls of color `i`.

**Return value**

The probability as a floating-point value.

### Examples
**Example 1**

- Input: `balls = [1,1]`
- Output: `1.0`

**Example 2**

- Input: `balls = [2,1,1]`
- Output: `0.66667`

**Example 3**

- Input: `balls = [1,2,1,2]`
- Output: `0.6`

---

## Underlying Base Algorithm(s)
Backtracking with combinatorics. For each color, choose how many balls go to the first box, multiply by the combination count, and accumulate favorable assignments where both boxes end with equal size and equal distinct-color counts.

---

## Complexity Analysis
- **Time Complexity**: `O(product(balls[i] + 1))`
- **Space Complexity**: `O(c)` for recursion depth over `c` colors.
