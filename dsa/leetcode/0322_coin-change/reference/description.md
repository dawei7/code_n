## Description

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the fewest number of coins that you need to make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.
### Function Contract

**Inputs**

- `coins`: The array of positive coin denominations.
- `amount`: The nonnegative target total.

**Return value**

Return the minimum number of coins needed to total `amount`, or `-1` when the amount is unreachable.

### Examples

#### Example 1

- **Input:** $coins = [1,2,5], amount = 11$
- **Output:** `3`
- **Explanation:** 11 = 5 + 5 + 1
#### Example 2

- **Input:** $coins = [2], amount = 3$
- **Output:** `-1`
#### Example 3

- **Input:** $coins = [1], amount = 0$
- **Output:** `0`
### Constraints

- $1 \le \text{coins.length} \le 12$

- $1 \le \text{coins}[i] \le 2^{31} - 1$

- $0 \le amount \le 10^{4}$