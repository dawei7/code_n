# Best Time to Buy and Sell Stock with Cooldown

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 309 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) |

## Problem Description
### Goal
You are given one stock price for each day. You may complete any number of buy-then-sell transactions, but can hold at most one share at a time. After selling a share, the following day is a cooldown during which buying is forbidden.

Return the maximum total profit achievable by the end of the price history. A sale must occur after its purchase, transactions cannot overlap, and a new purchase may occur only after the full cooldown day has passed. You may skip any day or make no trades when gains are unavailable. Return only the best profit, not the schedule of actions.

### Function Contract
**Inputs**

- `prices`: a nonempty list where `prices[i]` is the stock price on day `i`

**Return value**

The maximum achievable profit after the final day.

### Examples
**Example 1**

- Input: `prices = [1,2,3,0,2]`
- Output: `3`

**Example 2**

- Input: `prices = [49,27,3]`
- Output: `0`

**Example 3**

- Input: `prices = [37,49]`
- Output: `12`
