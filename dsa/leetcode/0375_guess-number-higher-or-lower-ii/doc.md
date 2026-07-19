# Guess Number Higher or Lower II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 375 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower-ii/) |

## Problem Description
### Goal
A hidden number lies in the inclusive range `1..n`. Each wrong guess `x` costs `x` dollars and reveals whether the target is lower or higher; correctly guessing the target ends the game without an additional wrong-guess cost.

Choose an adaptive strategy whose later guesses may depend on earlier responses. Return the minimum amount of money that guarantees finding the number in the worst case over every possible target. Minimizing the number of guesses alone is insufficient because guesses have different costs. For $n = 1$, no wrong guess is needed and the guaranteed cost is zero.

### Function Contract
**Inputs**

- `n`: the inclusive upper bound of the possible hidden numbers

**Return value**

- The minimum worst-case total cost of a strategy guaranteed to identify every target in `1..n`.

### Examples
**Example 1**

- Input: `n = 10`
- Output: `16`

**Example 2**

- Input: `n = 1`
- Output: `0`

**Example 3**

- Input: `n = 2`
- Output: `1`
