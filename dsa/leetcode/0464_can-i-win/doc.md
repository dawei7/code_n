# Can I Win

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 464 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming, Bit Manipulation, Memoization, Game Theory, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/can-i-win/) |

## Problem Description
### Goal
Two players alternate selecting unused integers from `1` through `maxChoosableInteger`, with the first player moving first. Each selected value is added to a shared running total and then becomes unavailable for the rest of the game.

The player whose choice first makes the total reach or exceed `desiredTotal` wins immediately. Assuming optimal play, return whether the first player can force a win against every response. If the sum of all available integers cannot reach the target, return `False`; if the target is already nonpositive, no selection is needed. The result concerns strategy, not one fixed play sequence.

### Function Contract
**Inputs**

- `maxChoosableInteger`: the available integers are `1` through this value, and each may be chosen once
- `desiredTotal`: the running-total threshold that immediately wins the game

**Return value**

- `True` if the first player has a strategy that wins against every opponent response; otherwise `False`

### Examples
**Example 1**

- Input: `maxChoosableInteger = 10, desiredTotal = 11`
- Output: `False`

**Example 2**

- Input: `maxChoosableInteger = 10, desiredTotal = 0`
- Output: `True`

**Example 3**

- Input: `maxChoosableInteger = 10, desiredTotal = 1`
- Output: `True`
