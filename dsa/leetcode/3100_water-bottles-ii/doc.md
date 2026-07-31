# Water Bottles II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3100 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [water-bottles-ii](https://leetcode.com/problems/water-bottles-ii/) |

## Problem Description

### Goal

You initially have `numBottles` full water bottles and an exchange price of `numExchange` empty bottles. In one operation, you may drink any number of full bottles, turning each one into an empty bottle. Alternatively, you may trade exactly the current `numExchange` empty bottles for one full bottle; after that exchange, the price increases by one.

Each exchange is a single batch at its current price. You cannot perform several exchanges using the same price—for example, three empty bottles and a price of one do not buy three full bottles before the price changes.

Return the maximum total number of full bottles that can be drunk by choosing the sequence of drinking and exchange operations optimally.

### Function Contract

**Inputs**

- `numBottles`: The number $n$ of full bottles initially available, where $1 \le n \le 100$.
- `numExchange`: The initial number of empty bottles required for one exchange, where $1 \le \texttt{numExchange} \le 100$.

**Return value**

- The maximum number of bottles that can be drunk under the increasing exchange-price rule.

### Examples

**Example 1**

- Input: `numBottles = 13, numExchange = 6`
- Output: `15`
- Explanation: Drinking the initial bottles gives thirteen empties. Exchanges at prices six and seven are possible, producing two more bottles; the next price is eight and too few empties remain.

**Example 2**

- Input: `numBottles = 10, numExchange = 3`
- Output: `13`
- Explanation: Three successive exchanges are possible at prices three, four, and five, so three bottles are added to the initial ten.
