# Water Bottles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1518 |
| Difficulty | Easy |
| Topics | Math, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/water-bottles/) |

## Problem Description
### Goal

Begin with `numBottles` full bottles of water. Drinking any full bottle increases the consumed total by one and leaves one empty bottle. A market repeatedly allows exactly `numExchange` empty bottles to be traded for one new full bottle, which can then be drunk and may contribute to another later exchange.

Choose exchanges to maximize the total number of bottles consumed and return that total. Full bottles do not expire and exchanging empties has no competing use, so every affordable exchange can be taken; leftover empties that do not reach the exchange threshold cannot produce more water.

### Function Contract
**Inputs**

- `numBottles`: The initial number of full bottles, with $1 \leq \texttt{numBottles} \leq 100$.
- `numExchange`: The number of empties required for one full bottle, with $2 \leq \texttt{numExchange} \leq 100$.

**Return value**

Return the maximum total number of full bottles that can be drunk after performing every profitable exchange.

### Examples
**Example 1**

- Input: `numBottles = 9, numExchange = 3`
- Output: `13`
- Explanation: Drinking 9 gives 9 empties, which produce 3 more bottles and then 1 final bottle.

**Example 2**

- Input: `numBottles = 15, numExchange = 4`
- Output: `19`
- Explanation: The successive exchange rounds contribute 3 bottles and then 1 bottle.

**Example 3**

- Input: `numBottles = 5, numExchange = 6`
- Output: `5`
- Explanation: The five empties never reach the exchange threshold.
